# **2D Tumor Angiogenesis Simulation**

This repository contains a series of models simulating tumor angiogenesis, including tumor cell diffusion, proliferation, and nutrient irrigation via a vascular network. These models aim to study how tumors grow, spread, and receive nutrients from blood vessels, covering various levels of complexity—from simple diffusion models to advanced simulations incorporating dynamic blood vessel growth.

The models are implemented using Python and Jupyter Notebooks, employing the finite difference method to solve diffusion and proliferation equations. Blood vessel growth (irrigation) is also simulated, showing how vessels dynamically develop to supply the tumor with nutrients.

I did this project under the supervision and help of Professor Rui Travasso and Matilda Palmeira , I would like to thank them for their huge efforts with me to be able to complete this project in under a week, it was a part of  the Computational Biology summer school in Coimbra September-2024, it was my first python project ever, However I'm proud I was able to finish it to the end and presenting the work I hope its the start of more upcoming computational biology and maybe neuroscience projects in the future

---

## **Table of Contents**

- [Overview](#overview)
- [Repository Contents](#repository-contents)
  - [1. Angiogenesis Model (Coimbra).ipynb](#1-angiogenesis-model-coimbraipynb)
  - [2. Angiogenesis Model (Coimbra) New Initial Conditions and Diffusion.ipynb](#2-angiogenesis-model-coimbra-new-initial-conditions-and-diffusionipynb)
  - [3. Angiogenesis Model (Coimbra) New Initial Conditions for Proliferation and Small D.ipynb](#3-angiogenesis-model-coimbra-new-initial-conditions-for-proliferation-and-small-dipynb)
  - [4. Angiogenesis Model (Coimbra) New Initial Conditions, Diffusion + Proliferation.ipynb](#4-angiogenesis-model-coimbra-new-initial-conditions-diffusion--proliferationipynb)
  - [5. Final (Diffusion, Proliferation, and Irrigation).ipynb](#5-final-diffusion-proliferation-and-irrigationipynb)
- [How to Run the Models](#how-to-run-the-models)
- [License](#license)

---

## **Overview**

Tumor angiogenesis is crucial for tumor expansion, as the process allows the tumor to grow beyond a size where diffusion alone can sustain it. This process involves inducing the growth of new blood vessels to supply nutrients and oxygen to the tumor. In this repository, we provide models that simulate this process starting with basic diffusion and adding more biological complexity, such as cell proliferation and dynamic blood vessel growth.

Each notebook explores different aspects of tumor angiogenesis:
- **Diffusion**: Tumor cells spread across space.
- **Proliferation**: Cells multiply in response to environmental conditions.
- **Irrigation**: Blood vessels grow to supply nutrients to the tumor.

---

## **Repository Contents**

### 1. **Angiogenesis Model (Coimbra).ipynb**

**Description**:
This is the simplest model in the series, simulating tumor cell diffusion from a smooth, circular region using a Gaussian distribution. The model illustrates how tumor cells spread symmetrically from the center.

**Key Features**:
- **Initial Condition**: Smooth, circular tumor region.
- **Processes Modeled**: Tumor cell diffusion across a 100x100 grid.
- **Parameters**:
  - \( D = 1 \): Diffusion coefficient.
  - \( A = 0.1 \): Maximum cell density.
  - \( \sigma = 10 \): Tumor width.
- **Visualization**: Symmetric diffusion of the tumor is visualized in real-time during the simulation.

---

### 2. **Angiogenesis Model (Coimbra) New Initial Conditions and Diffusion.ipynb**

**Description**:
This model simulates diffusion starting from three distinct tumor regions, initialized using separate Gaussian distributions. This model represents a more complex and realistic tumor growth pattern.

**Key Features**:
- **Initial Condition**: Three distinct regions with different widths and locations.
- **Processes Modeled**: Diffusion of tumor cells across a 200x200 grid.
- **Parameters**:
  - \( D = 2 \): Higher diffusion rate for faster spread.
  - \( \sigma_1, \sigma_2, \sigma_3 \): Widths of the tumor regions.
  - \( A = 0.05 \): Maximum cell density.
- **Visualization**: Tumor growth is visualized at multiple time steps (100, 480, 860, etc.), showing how the tumor regions interact and spread over time.

---

### 3. **Angiogenesis Model (Coimbra) New Initial Conditions for Proliferation and Small D.ipynb**

**Description**:
This model introduces **cell proliferation** alongside diffusion, simulating slower cell movement with active cell growth. Tumor cells grow according to a logistic model, but their movement is restricted due to a small diffusion coefficient.

**Key Features**:
- **Initial Condition**: Three irregular tumor regions.
- **Processes Modeled**: Slow diffusion and cell proliferation.
- **Parameters**:
  - \( D1 = 0.001 \): Limited diffusion rate.
  - \( \alpha_0 = 2 \): Proliferation rate.
  - \( N_{\text{Max}} = 1 \): Maximum cell carrying capacity.
- **Visualization**: Tumor regions proliferate and diffuse slowly, with snapshots at time steps (100, 480, 860, etc.).

---

### 4. **Angiogenesis Model (Coimbra) New Initial Conditions, Diffusion + Proliferation.ipynb**

**Description**:
This model balances both **diffusion** and **proliferation**. Cells spread moderately through diffusion while actively multiplying through proliferation. The tumor grows from three distinct regions.

**Key Features**:
- **Initial Condition**: Three tumor regions.
- **Processes Modeled**: Moderate diffusion and cell proliferation.
- **Parameters**:
  - \( D = 0.05 \): Moderate diffusion coefficient.
  - \( \alpha_0 = 1 \): Proliferation rate.
  - \( N_{\text{Max}} = 1 \): Maximum cell carrying capacity.
- **Visualization**: Tumor growth is visualized at various time steps (100, 200, 300, ..., 999), showing how diffusion and proliferation interact.

---

### 5. **Final (Diffusion, Proliferation, and Irrigation).ipynb**

**Description**:
This is the most comprehensive model, incorporating **diffusion**, **proliferation**, and a **vascular network** to supply nutrients to the growing tumor. The model dynamically simulates blood vessel growth in response to the tumor's nutrient demands.

**Key Features**:
- **Initial Condition**: Three tumor regions and a uniform vascular network.
- **Processes Modeled**: Diffusion, proliferation, and irrigation (blood vessel growth).
- **Parameters**:
  - \( D = 0.2 \): Diffusion coefficient.
  - \( \alpha_0 = 1 \), \( \alpha_1 = 1 \), \( \Gamma = 0.5 \): Proliferation parameters.
  - \( V_{\text{Max}} = 4 \): Maximum vessel density.
  - **Beta Matrix**: Controls vascular growth rate.
- **Visualization**: Both the tumor and vascular network are visualized at multiple time steps, showing interactions between the tumor and its blood supply.

---

## **How to Run the Models**

### Requirements:

- Python 3.x
- Jupyter Notebook
- Required libraries: `numpy`, `matplotlib`
