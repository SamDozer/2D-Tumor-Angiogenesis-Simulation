# 2D-Tumor-Angiogenesis-Simulation
2D tumor angiogenesis simulation using Python and Jupyter Notebooks. Models explore tumor cell diffusion, proliferation, and vascular irrigation. Includes multiple initial conditions, diffusion coefficients, and dynamic blood vessel growth for realistic tumor simulation.


This repository contains a series of models simulating tumor angiogenesis, diffusion, proliferation, and interactions with a vascular network (irrigation). These models are designed to study how tumor cells grow, spread, and receive nutrients from blood vessels, and they vary in their complexity, from basic diffusion models to advanced models incorporating dynamic vascular growth.

The models are implemented in Python, using the finite difference method to solve the diffusion and proliferation equations governing tumor growth. They also model how blood vessels grow in response to the tumor's nutrient demands.

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

Tumor angiogenesis is the process by which a tumor induces the growth of new blood vessels to supply itself with nutrients and oxygen. This process is critical for tumor expansion, as it allows the tumor to grow beyond the size at which simple diffusion can support it. In this repository, several models simulate this process, starting with simple diffusion models and progressively adding more biological detail, such as cell proliferation and blood vessel growth.

Each notebook explores a different aspect of tumor angiogenesis:
- **Diffusion**: The spread of tumor cells across space.
- **Proliferation**: The multiplication of tumor cells in response to environmental conditions.
- **Irrigation**: The growth of blood vessels that supply nutrients to the tumor.

---

## **Repository Contents**

### 1. **Angiogenesis Model (Coimbra).ipynb**

**Description**:
- This is the simplest angiogenesis model. It simulates tumor cell diffusion starting from a smooth, circular region. The model uses a Gaussian distribution to initialize the tumor and simulates how tumor cells spread symmetrically from the center.
  
**Key Features**:
- **Initial Condition**: The tumor starts as a smooth, circular region.
- **Processes Modeled**: Diffusion of tumor cells across a 100x100 grid.
- **Main Parameters**:
  - \( D = 1 \): Diffusion coefficient.
  - \( A = 0.1 \): Maximum cell number.
  - \( \sigma = 10 \): Tumor width.
- **Visualization**: The tumor growth is visualized at each time step, showing a symmetric diffusion pattern.

---

### 2. **Angiogenesis Model (Coimbra) New Initial Conditions and Diffusion.ipynb**

**Description**:
- This model simulates the diffusion of tumor cells starting from **three distinct regions**, initialized using separate Gaussian distributions. The model is more complex than the previous one, as it simulates an irregular, multi-region tumor.

**Key Features**:
- **Initial Condition**: The tumor consists of three separate regions with different widths and locations.
- **Processes Modeled**: Diffusion of tumor cells across a 200x200 grid.
- **Main Parameters**:
  - \( D = 2 \): Higher diffusion coefficient, resulting in faster spread.
  - \( \sigma_1, \sigma_2, \sigma_3 \): Widths of the three tumor regions.
  - \( A = 0.05 \): Maximum cell number.
- **Visualization**: The tumor growth is visualized at multiple time steps (100, 480, 860, etc.), showing the interaction and diffusion of tumor regions over time.

---

### 3. **Angiogenesis Model (Coimbra) New Initial Conditions for Proliferation and Small D.ipynb**

**Description**:
- This model introduces **cell proliferation** in addition to diffusion. The diffusion coefficient is small, simulating slow cell movement, but tumor cells proliferate actively based on a logistic growth model.

**Key Features**:
- **Initial Condition**: Three irregular tumor regions.
- **Processes Modeled**: Slow diffusion and cell proliferation.
- **Main Parameters**:
  - \( D1 = 0.001 \): Small diffusion coefficient for limited cell movement.
  - \( \alpha_0 = 2 \): Proliferation rate.
  - \( N_{\text{Max}} = 1 \): Maximum cell carrying capacity.
- **Visualization**: Tumor regions proliferate and slowly diffuse, visualized at selected time steps (100, 480, 860, etc.).

---

### 4. **Angiogenesis Model (Coimbra) New Initial Conditions, Diffusion + Proliferation.ipynb**

**Description**:
- This model balances both **diffusion** and **proliferation**. Cells spread through diffusion while also multiplying through proliferation. The initial tumor shape is the same as in previous models, with three distinct regions.

**Key Features**:
- **Initial Condition**: Three irregular tumor regions.
- **Processes Modeled**: Moderate diffusion and cell proliferation.
- **Main Parameters**:
  - \( D = 0.05 \): Moderate diffusion coefficient.
  - \( \alpha_0 = 1 \): Proliferation rate.
  - \( N_{\text{Max}} = 1 \): Maximum cell carrying capacity.
- **Visualization**: Tumor growth is visualized at various time steps (100, 200, 300, ..., 999), showing the interaction between diffusion and proliferation.

---

### 5. **Final (Diffusion, Proliferation, and Irrigation).ipynb**

**Description**:
- This is the most advanced model, incorporating **diffusion**, **proliferation**, and a **vascular network** (irrigation) that supplies nutrients to the tumor. The model simulates how blood vessels grow in response to the tumor's demand for nutrients, supporting the tumor's expansion.

**Key Features**:
- **Initial Condition**: Three irregular tumor regions and a uniform vascular network.
- **Processes Modeled**: Diffusion, proliferation, and irrigation (blood vessel growth).
- **Main Parameters**:
  - \( D = 0.2 \): Diffusion coefficient.
  - \( \alpha_0 = 1 \), \( \alpha_1 = 1 \), \( \Gamma = 0.5 \): Proliferation parameters.
  - \( V_{\text{Max}} = 4 \): Maximum vessel density.
  - **Beta Matrix**: Controls vascular growth rate in different regions.
- **Visualization**: Both the tumor and the vessel network are visualized at selected time steps (100, 200, 300, ..., 999), showing the interaction between the growing tumor and the vascular system.

---

## **How to Run the Models**

### Requirements:

- Python 3.x
- Jupyter Notebook
- Required libraries: `numpy`, `matplotlib`

### Instructions:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/tumor-angiogenesis-simulation.git
    ```
2. Navigate to the repository folder:
    ```bash
    cd tumor-angiogenesis-simulation
    ```
3. Open the Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
4. Run any of the provided notebooks to explore different tumor growth simulations.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This README provides a detailed overview of the project, descriptions of each file, and instructions for running the simulations. Let me know if you need any further modifications or clarifications!
