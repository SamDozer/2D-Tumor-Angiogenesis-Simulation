"""Shared building blocks for the notebooks in corrected/notebooks/.

The notebooks import this file (it sits one folder above them), and the
tests in corrected/tests/ check it. Grid quantities are in grid units:
delta_x is the cell size and delta_t the time step.
"""
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------- numerics

def laplacian(f, dx=1.0, bc="periodic"):
    """5-point (3-point in 1D) finite-difference Laplacian of a 1D or 2D array.

    bc="periodic": the grid wraps around, as in the original notebooks.
    bc="noflux":   zero-gradient edges, so nothing enters or leaves the grid.
    """
    if bc == "periodic":
        total = 0
        for axis in range(f.ndim):
            total = total + np.roll(f, 1, axis=axis) + np.roll(f, -1, axis=axis)
    elif bc == "noflux":
        g = np.pad(f, 1, mode="edge")          # ghost cells copy the edge value
        inner = tuple(slice(1, -1) for _ in range(f.ndim))
        total = 0
        for axis in range(f.ndim):
            up = list(inner); up[axis] = slice(2, None)
            down = list(inner); down[axis] = slice(None, -2)
            total = total + g[tuple(up)] + g[tuple(down)]
    else:
        raise ValueError(f"unknown boundary condition {bc!r}")
    return (total - 2 * f.ndim * f) / dx**2


def check_stability(D, dt, dx, ndim=2):
    """The explicit scheme is stable only if D*dt/dx^2 <= 1/(2*ndim)."""
    limit = 1 / (2 * ndim)
    if D * dt / dx**2 > limit:
        raise ValueError(f"unstable: D*dt/dx^2 = {D * dt / dx**2:.3g} > {limit:g}; reduce dt")


# ---------------------------------------------------------- initial states

def grid_indices(l):
    """Row and column index arrays for an l x l grid."""
    return np.meshgrid(np.arange(l), np.arange(l), indexing="ij")


def gaussian(i, j, ci, cj, A, sigma):
    return A * np.exp(-((i - ci)**2 + (j - cj)**2) / (2 * sigma**2))


def three_regions(l=200, A=0.05, sigmas=(15, 25, 12), cutoff=0.0):
    """The three overlapping Gaussian tumour regions used in notebooks 2-6.

    Densities below `cutoff` are set to zero: a Gaussian never reaches exactly
    zero, and with logistic growth its tiny tails would grow everywhere.
    """
    i, j = grid_indices(l)
    s1, s2, s3 = sigmas
    n = gaussian(i, j, l/2, l/2 - 10, A, s1) + gaussian(i, j, l/2, 3*l/4 - 30, A, s2) \
        + gaussian(i, j, 2*l/5, 3*l/5 - 10, A, s3)
    if cutoff:
        n[n < cutoff] = 0.0
    return n


def beta_split(l, left, right):
    """Vessel growth rate beta: one value on the left half, another on the right."""
    beta = np.zeros((l, l))
    beta[:, : l // 2] = left
    beta[:, l // 2 :] = right
    return beta


# ------------------------------------------------------------ model steps

def fk_step(n, D, alpha, n_max, dt, dx=1.0, bc="periodic"):
    """One explicit step of the Fisher-Kolmogorov equation
    dn/dt = D lap(n) + alpha n (1 - n/n_max)."""
    return n + dt * (D * laplacian(n, dx, bc) + alpha * n * (1 - n / n_max))


def vessel_boost(V, gamma):
    """(V - 1)^gamma from the course notes, taken as 0 where no new vessels
    have formed (V = 1). This matters only for gamma = 0, where numpy would
    otherwise evaluate 0**0 = 1."""
    excess = np.maximum(V - 1, 0.0)
    return np.where(excess > 0, excess ** gamma, 0.0)


def irrigation_step(n, V, beta, D, alpha0, alpha1, gamma, n_max, v_max, dt, dx=1.0, bc="periodic"):
    """One explicit step of the irrigation model as written in the course notes:
    dn/dt = D lap(n) + [alpha0 + alpha1 (V-1)^gamma] n (1 - n/n_max)
    dV/dt = beta n V (1 - V/v_max)
    Both fields are updated from the previous step."""
    rate = alpha0 + alpha1 * vessel_boost(V, gamma)
    n_next = n + dt * (D * laplacian(n, dx, bc) + rate * n * (1 - n / n_max))
    V_next = V + dt * beta * n * V * (1 - V / v_max)
    return n_next, V_next


def nutrient_step(n, c, V, beta, D, alpha0, n_max, v_max, D_c, lam, s, dt, substeps, dx=1.0, bc="periodic"):
    """One step of the extension model (notebook 06): vessels supply a nutrient c
    that sets the carrying capacity n_max * c; hypoxic tumour cells grow vessels.
    The fast nutrient is advanced with `substeps` smaller steps."""
    dt_c = dt / substeps
    for _ in range(substeps):
        c = c + dt_c * (D_c * laplacian(c, dx, bc) + s * V * (1 - c) - lam * n * c)
    K = n_max * c
    n_next = n + dt * (D * laplacian(n, dx, bc) + alpha0 * n * (K - n) / n_max)
    V_next = V + dt * beta * n * (1 - c) * (1 - V / v_max)
    return n_next, c, V_next


# ------------------------------------------------------------- analysis

def front_position(n, dx, level=0.5):
    """Position of a 1D front moving right: where n first drops below `level`,
    linearly interpolated between grid points."""
    k = int(np.argmax(n < level))
    if k == 0:
        return np.nan
    x0, x1 = (k - 1) * dx, k * dx
    return x0 + (n[k - 1] - level) / (n[k - 1] - n[k]) * (x1 - x0)


def continuum_speed(D, alpha):
    """Fisher-Kolmogorov front speed in the continuum limit: 2 sqrt(D alpha)."""
    return 2 * np.sqrt(D * alpha)


def lattice_speed(D, alpha, dx):
    """Front speed of the Fisher-Kolmogorov equation on a grid with spacing dx
    (continuous time): the minimum over lambda of
        [alpha + 2 D (cosh(lambda dx) - 1) / dx^2] / lambda.
    It tends to 2 sqrt(D alpha) as dx -> 0 and is faster on coarse grids."""
    lam_star = np.sqrt(alpha / D)
    lams = np.logspace(np.log10(lam_star) - 3, np.log10(50 / dx), 200_000)
    with np.errstate(over="ignore"):
        speeds = (alpha + 2 * D * (np.cosh(lams * dx) - 1) / dx**2) / lams
    return float(speeds.min())


# ------------------------------------------------------------- plotting

def plot_snapshots(frames, title, vmax, ncols, dt, cmap="viridis", label="tumour cell density"):
    """Draw {step: 2D array} as a grid of images with a shared colour bar."""
    nrows = int(np.ceil(len(frames) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.2 * ncols, 3.2 * nrows), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")
    for ax, (step, frame) in zip(axes.flat, frames.items()):
        im = ax.imshow(frame, origin="lower", cmap=cmap, vmin=0, vmax=vmax)
        ax.set_title(f"step {step}  (t = {step * dt:g})")
    fig.colorbar(im, ax=axes, shrink=0.8, label=label)
    fig.suptitle(title)
    plt.show()
