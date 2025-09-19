# **2D Tumor Angiogenesis Simulation**

This repository contains a series of 2D models simulating tumor angiogenesis, focusing on how tumor cells diffuse, proliferate, and interact with a vascular network for nutrient supply. The models are implemented on a 2D grid, using simplified mathematical representations of biological processes. While the models explore various levels of complexity—ranging from basic diffusion to dynamic blood vessel growth—they remain simplified approximations of real-life tumor behavior and do not aim to be fully 3D or exhaustive in biological realism.

The simulations are done using Python and Jupyter Notebooks, employing the finite difference method to solve the diffusion and proliferation equations that govern tumor growth. Additionally, blood vessel growth (irrigation) is modeled to simulate how vessels dynamically develop to supply nutrients to the tumor. These models serve as educational tools for understanding basic angiogenesis processes in a 2D framework.

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


---

## **Overview**

Tumor angiogenesis is crucial for tumor expansion, as the process allows the tumor to grow beyond a size where diffusion alone can sustain it. This process involves inducing the growth of new blood vessels to supply nutrients and oxygen to the tumor. In this repository, we provide models that simulate this process starting with basic diffusion and adding more biological complexity, such as cell proliferation and dynamic blood vessel growth.

The main equations used in the model include:
- **Fisher-Kolmogorov Equation**: Used to model tumor cell **diffusion** and **proliferation**. The equation combines diffusion, modeled with the Laplacian operator (\( \nabla^2 n \)), and logistic growth for cell proliferation.
- **Vessel Growth Equation**: A separate equation that models the growth of blood vessels as a function of tumor cell density and vessel density. This equation regulates how the vascular network adapts to supply the growing tumor.
- **Gaussian Initialization**: Tumor cells are initially placed in Gaussian-shaped regions, simulating circular or irregular initial tumor shapes.
- **Finite Difference Method**: This method is used to discretize the spatial derivatives (Laplacian) and solve the partial differential equations (PDEs) governing the tumor's growth and the formation of the vascular network.

Each notebook explores different aspects of tumor angiogenesis:
- **Diffusion**: Tumor cells spread across space due to concentration gradients.
- **Proliferation**: Tumor cells multiply based on local cell density and environmental conditions, following logistic growth.
- **Irrigation**: Blood vessels grow dynamically to supply the tumor with nutrients, represented by the vessel density equation.

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

# Acknowledgments

This project was completed under the guidance of Professor Rui Travasso and Matilda Palmeira. I am deeply grateful for their support and insights, which enabled me to complete this project in under a week. This work was part of the Computational Biology Summer School in Coimbra in September 2024, and it also marks my first Python project. I’m proud to present this work and look forward to exploring more projects in computational biology and neuroscience in the future.

