"""Tests for corrected/angiogenesis.py. Run from the repo root:  python -m pytest corrected"""
import numpy as np
import pytest

import angiogenesis as ag

rng = np.random.default_rng(0)


@pytest.mark.parametrize("bc", ["periodic", "noflux"])
def test_laplacian_of_constant_is_zero(bc):
    assert np.allclose(ag.laplacian(np.full((30, 30), 3.7), bc=bc), 0)


def test_laplacian_is_exact_for_quadratics():
    # the 5-point stencil is exact for x^2 + y^2, whose Laplacian is 4
    dx = 0.5
    x = np.arange(40) * dx
    X, Y = np.meshgrid(x, x, indexing="ij")
    lap = ag.laplacian(X**2 + Y**2, dx=dx)
    assert np.allclose(lap[1:-1, 1:-1], 4.0)


@pytest.mark.parametrize("bc", ["periodic", "noflux"])
def test_diffusion_conserves_total(bc):
    n = rng.random((50, 50))
    total = n.sum()
    for _ in range(300):
        n = n + 0.1 * 1.0 * ag.laplacian(n, bc=bc)
    assert n.sum() == pytest.approx(total, rel=1e-12)


def test_noflux_does_not_wrap_around():
    n = np.zeros((40, 40))
    n[18:22, 0:3] = 1.0                       # blob touching the left edge
    periodic, closed = n.copy(), n.copy()
    for _ in range(200):
        periodic = periodic + 0.2 * ag.laplacian(periodic, bc="periodic")
        closed = closed + 0.2 * ag.laplacian(closed, bc="noflux")
    # periodic: the blob wraps straight onto the right edge; no-flux: only the
    # faint diffusion tail arrives after crossing all 40 cells
    assert periodic[:, -1].sum() > 100 * closed[:, -1].sum()
    assert periodic[:, -1].sum() == pytest.approx(periodic[:, 0].sum(), rel=0.05)


def test_logistic_growth_matches_exact_solution():
    alpha, n0, dt, steps = 1.0, 0.01, 0.001, 5000
    n = np.full((5, 5), n0)
    for _ in range(steps):
        n = ag.fk_step(n, D=0.1, alpha=alpha, n_max=1.0, dt=dt)
    t = dt * steps
    exact = 1 / (1 + (1 / n0 - 1) * np.exp(-alpha * t))
    assert np.allclose(n, exact, rtol=1e-3)


def test_front_speed_approaches_continuum_value():
    D, alpha, dx, dt = 1.0, 1.0, 0.25, 0.01
    x = np.arange(0, 200, dx)
    n = (x < 5).astype(float)
    times, positions = [], []
    for step in range(1, 6001):
        n = ag.fk_step(n, D, alpha, 1.0, dt, dx, bc="noflux")
        if step % 500 == 0:
            times.append(step * dt); positions.append(ag.front_position(n, dx))
    speed = np.polyfit(times[-6:], positions[-6:], 1)[0]
    # pulled fronts approach 2*sqrt(D*alpha) slowly from below
    assert 0.93 * ag.continuum_speed(D, alpha) < speed < 1.01 * ag.continuum_speed(D, alpha)


def test_lattice_speed_limits():
    # fine grid -> continuum value; coarse grid -> faster than continuum
    assert ag.lattice_speed(0.05, 1.0, 1e-3) == pytest.approx(ag.continuum_speed(0.05, 1.0), rel=1e-3)
    assert ag.lattice_speed(0.001, 2.0, 1.0) > 3 * ag.continuum_speed(0.001, 2.0)


def test_unstable_settings_are_rejected():
    ag.check_stability(D=0.2, dt=0.1, dx=1.0)        # 0.02: fine
    with pytest.raises(ValueError):
        ag.check_stability(D=4.0, dt=0.1, dx=1.0)    # 0.4 > 0.25


def test_cutoff_zeroes_the_gaussian_tails():
    n = ag.three_regions(cutoff=1e-3)
    assert n.min() == 0.0
    assert np.all((n == 0) | (n >= 1e-3))


def test_vessel_boost_is_zero_without_new_vessels():
    V = np.array([1.0, 1.0 + 1e-9, 4.0])
    assert ag.vessel_boost(V, 0.0).tolist() == [0.0, 1.0, 1.0]
    assert ag.vessel_boost(V, 0.5)[[0, 2]].tolist() == [0.0, pytest.approx(3**0.5)]


def test_irrigation_without_vessel_growth_is_plain_fisher_kolmogorov():
    n = ag.three_regions(cutoff=1e-3)
    V = np.ones_like(n)
    beta = np.zeros_like(n)
    n_irr, V_irr = ag.irrigation_step(n, V, beta, 0.2, 1, 1, 0.5, 1, 4, 0.1)
    assert np.array_equal(V_irr, V)
    assert np.allclose(n_irr, ag.fk_step(n, 0.2, 1, 1, 0.1))


def test_nutrient_stays_at_one_without_tumour():
    shape = (30, 30)
    n, c, V = np.zeros(shape), np.ones(shape), np.ones(shape)
    _, c_next, _ = ag.nutrient_step(n, c, V, np.zeros(shape), 0.2, 1, 1, 4,
                                    D_c=40, lam=0.625, s=0.0625, dt=0.1, substeps=20)
    assert np.allclose(c_next, 1.0)
