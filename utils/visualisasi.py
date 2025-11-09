import numpy as np
import matplotlib.pyplot as plt

def plot_fungsi(f, a, b, title="Grafik Fungsi"):
    """
    Menggambar grafik dari sebuah fungsi f(x) dari x=a ke x=b.
    
    Args:
        f (callable): Fungsi Python yang menerima satu angka (atau array NumPy)
                      dan mengembalikan satu angka (atau array NumPy).
        a (float): Batas kiri plot.
        b (float): Batas kanan plot.
        title (str): Judul untuk grafik.
    """
    try:
        # Buat 100 titik antara a dan b
        x_vals = np.linspace(a, b, 100)
        # Hitung nilai y untuk setiap x
        y_vals = f(x_vals)
        
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f"f(x)")
        
        # Tambahkan garis sumbu x dan y
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        
        # Tampilkan plot
        print("Menampilkan plot... (Tutup jendela plot untuk melanjutkan)")
        plt.show()

    except Exception as e:
        print(f"Error saat membuat plot: {e}")