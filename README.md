# 🧮 Metnum-Solver: Numerical Methods CLI

A modular command-line interface (CLI) program for solving various numerical methods problems. Built with Python, this project is designed for extensibility and ease of use in an educational context.

---

## 💡 Background

This project originated from the need for a centralized tool in a **Numerical Methods** university course. Students often encounter diverse mathematical problems requiring different numerical solution techniques, such as solving systems of linear equations, finding roots of non-linear equations, or calculating definite integrals.

The traditional approach of rewriting computation scripts for each new problem is time-consuming and error-prone. This solver aims to streamline the process by providing a single application where users can:

1.  Run the program.
2.  Select a desired numerical method from a menu.
3.  Interactively input problem-specific data (e.g., matrices, equations).
4.  Obtain the solution directly.

This approach allows users to focus on understanding numerical concepts and analyzing results, rather than repetitive coding setup.

---

## ✨ Key Features

*   **Interactive CLI Menu:** User-friendly text-based interface.
*   **Flexible Equation Input:** Utilizes the **SymPy** library for parsing symbolic function inputs (e.g., `"x**3 - 2*x + 1"`) and automatic derivative calculation.
*   **Data Visualization:** Integrates with **Matplotlib** to plot functions, aiding in the visual analysis of problems.
*   **Modular Structure:** Code is organized into logical components:
    *   `metode/`: Core mathematical algorithms.
    *   `ui/`: User interface and interaction logic.
    *   `utils/`: Helper functions (input parsing, visualization).
*   **Error Handling:** Basic error handling, such as zero pivot detection in Gaussian Elimination.

---

## 📚 Implemented Methods

Currently, this program fully supports:

*   **Systems of Linear Equations (SLE):**
    *   Naive Gaussian Elimination

---

## 🚧 Planned Features

The following methods are planned for future implementation:

*   **Root Finding:**
    *   Newton-Raphson Method
*   **Numerical Integration:**
    *   Trapezoidal Rule

---

## 🚀 Installation and Setup

To run this project, ensure you have **Python 3.8+** installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Metnum-Solver.git # Replace with actual repo URL
    cd Metnum-Solver
    ```
2.  **(Optional but Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Key libraries: `numpy`, `sympy`, `matplotlib`, `scipy`, `ruff`)*

---

## 🏃 How to Run

After installation, start the application from the project's root directory:

```bash
python main.py
```

---