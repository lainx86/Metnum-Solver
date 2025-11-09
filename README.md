# 🧮 Numerical Methods Calculator

A modular command-line interface (CLI) calculator program for solving various numerical methods problems. This project is built with Python and designed to be easily expandable.

---

##  latar Belakang (Background)

This project was created as a tool for a **Numerical Methods** university course. In this course, students often face various mathematical problems requiring different numerical solution methods, such as:

* Solving systems of linear equations (e.g., Gaussian Elimination).
* Finding roots of non-linear equations (e.g., Newton-Raphson Method).
* Calculating definite integrals (e.g., Trapezoidal or Simpson's Rule).

A common challenge is the need to **rewrite computation scripts from scratch** for every new problem or method. This process is time-consuming, inefficient, and prone to errors.

This calculator was born from the idea to **centralize** all these methods into one parent program. The goal is to create a "calculator" where the user (student) simply needs to:

1.  Run a single program.
2.  Select the desired method from a menu.
3.  Enter data (like matrices or equations) interactively.
4.  Get the solution directly.

With this approach, the focus can shift from repetitive code setup to understanding the concepts and analyzing the results of the numerical methods themselves.

---

## ✨ Key Features

* **Interactive CLI Menu:** An easy-to-use text-based interface.
* **Flexible Equation Input:** Uses the **SymPy** library to parse function inputs as strings (e.g., `"x**3 - 2*x + 1"`) and automatically calculate their derivatives.
* **Data Visualization:** Integrates with **Matplotlib** to plot functions, aiding in the visualization of problems like integration or root finding.
* **Modular Structure:** The code is clearly separated into:
    * `metode/`: (The Brain) Core mathematical logic (algorithms).
    * `ui/`: (The Face) User interface logic (menus, input/output).
    * `utils/`: (The Toolbox) Helper functions (input parsers, visualization).
* **Error Handling:** Equipped with basic error handling, such as zero pivot detection in Gaussian Elimination.

---

## 📚 Implemented Methods

Currently, this program supports:

* **Systems of Linear Equations (SLE):**
    * Naive Gaussian Elimination
* **Root Finding:**
    * Newton-Raphson Method *(Core logic in development)*
* **Numerical Integration:**
    * Trapezoidal Rule *(Core logic in development)*

---

## 🚀 Installation and Setup

To run this project on your computer, follow these steps:

1.  Ensure you have **Python 3.8** or newer.
2.  (Optional but recommended) Create and activate a *virtual environment*:
    ```bash
    python -m venv venv
    source venv/bin/activate  # (On Windows: venv\Scripts\activate)
    ```
3.  Install all required libraries from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    *Main libraries: `numpy`, `sympy`, `matplotlib`, `scipy`.*

---

## 🏃 How to Run

To start the application, run the `main.py` file from the project's root directory:

```bash
python main.py
