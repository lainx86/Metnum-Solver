import numpy as np

def eliminasi_gauss_naive(A, b):
    """
    Menyelesaikan sistem persamaan linear Ax = b menggunakan
    metode eliminasi Gauss naif (tanpa pivoting).
    
    Args:
        A (np.array): Matriks koefisien (n x n).
        b (np.array): Vektor hasil (n).
        
    Returns:
        np.array: Vektor solusi x (n).
    """
    
    # --- 1. Inisialisasi & Salin Data ---
    # Salin A dan b agar tidak mengubah data asli!
    # Gunakan astype(float) untuk memastikan semua perhitungan adalah float
    C = A.copy().astype(float)
    r = b.copy().astype(float)
    
    n = len(r)
    x = np.zeros(n)

    # --- 2. Eliminasi Maju (Forward Elimination) ---
    # (Mengubah C menjadi matriks segitiga atas)
    for k in range(n - 1):  # Loop dari k = 0 hingga n-2
        
        # Normalisasi baris pivot (k)
        temp = 1.0 / C[k, k]
        for j in range(k, n):  # Loop dari j = k hingga n-1
            C[k, j] = C[k, j] * temp
        r[k] = r[k] * temp

        # Eliminasi elemen di bawah pivot
        for j in range(k + 1, n):  # Loop untuk setiap baris di bawah pivot
            temp = C[j, k]
            for i in range(k, n):  # Loop untuk setiap kolom di baris j
                C[j, i] = C[j, i] - C[k, i] * temp
            r[j] = r[j] - r[k] * temp

    # --- 3. Substitusi Mundur (Back Substitution) ---

    # Selesaikan untuk x terakhir (x[n-1])
    # Ini diperlukan karena loop eliminasi maju hanya sampai n-2,
    # jadi C[n-1, n-1] belum tentu 1.
    x[n - 1] = r[n - 1] / C[n - 1, n - 1]

    # Selesaikan untuk x lainnya, bergerak mundur
    for i in range(n - 2, -1, -1):  # Loop dari i = n-2 turun ke 0
        sum_val = 0
        for j in range(i + 1, n):  # Loop dari j = i+1 hingga n-1
            sum_val = sum_val + C[i, j] * x[j]
        
        # Seperti yang Anda catat, C[i, i] di sini sudah 1
        # karena normalisasi di langkah 2.
        # sum_val = sum_val / C[i, i] # -> Baris ini bisa dihilangkan
        x[i] = r[i] - sum_val

    # --- 4. Kembalikan Hasil ---
    return x
