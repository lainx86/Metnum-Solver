import numpy as np
import sympy

def parse_matriks_interaktif(n):
    """
    Meminta input matriks dari pengguna baris per baris.
    Contoh input: "1 2 3" atau "1, 2, 3"
    """
    matriks = []
    print(f"  Masukkan {n} angka per baris, pisahkan dengan spasi.")
    for i in range(n):
        while True:
            try:
                # Ganti koma dengan spasi, lalu pisahkan berdasarkan spasi
                str_baris = input(f"    Baris {i+1}: ").replace(',', ' ')
                baris = [float(angka) for angka in str_baris.split()]
                
                if len(baris) != n:
                    print(f"    Error: Harap masukkan tepat {n} angka. Anda memasukkan {len(baris)}.")
                else:
                    matriks.append(baris)
                    break # Lanjut ke baris berikutnya
            except ValueError:
                print("    Error: Input mengandung karakter non-angka. Coba lagi.")
    
    return np.array(matriks, dtype=float)


def parse_vektor_interaktif(n):
    """
    Meminta input vektor dari pengguna dalam satu baris.
    Contoh input: "9 1 6" atau "9, 1, 6"
    """
    print(f"  Masukkan {n} angka, pisahkan dengan spasi.")
    while True:
        try:
            str_vektor = input(f"    Vektor: ").replace(',', ' ')
            vektor = [float(angka) for angka in str_vektor.split()]
            
            if len(vektor) != n:
                 print(f"    Error: Harap masukkan tepat {n} angka. Anda memasukkan {len(vektor)}.")
            else:
                return np.array(vektor, dtype=float) # Keluar dari loop
        except ValueError:
            print("    Error: Input mengandung karakter non-angka. Coba lagi.")


def parse_fungsi_simbolik():
    """
    Mengubah input string (misal "x**2 - 2") menjadi fungsi Python
    yang bisa dihitung (f) dan juga turunannya (df).
    Menggunakan library SymPy.
    """
    str_fungsi = input("  Masukkan fungsi (gunakan 'x' sbg variabel, cth: x**2 - 2): ")
    
    try:
        x = sympy.symbols('x')
        # 1. Ubah string jadi ekspresi simbolik
        #    Gunakan evalf() untuk menyederhanakan jika ada Pi, dll.
        f_simbolik = sympy.sympify(str_fungsi).evalf()
        
        # 2. Cari turunan secara otomatis
        df_simbolik = sympy.diff(f_simbolik, x)
        
        print(f"    Fungsi    (f): {f_simbolik}")
        print(f"    Turunan (f'): {df_simbolik}")
        
        # 3. Ubah ekspresi simbolik menjadi fungsi numerik
        #    Ini adalah fungsi yang bisa dipanggil dengan angka
        f_numerik = sympy.lambdify(x, f_simbolik, 'numpy')
        df_numerik = sympy.lambdify(x, df_simbolik, 'numpy')
        
        return f_numerik, df_numerik
        
    except sympy.SympifyError:
        print("Error: Format fungsi tidak valid.")
        raise ValueError("Gagal mem-parsing fungsi")
    except Exception as e:
        print(f"Error tidak terduga di SymPy: {e}")
        raise