
# --- Impor dari folder 'metode' ---
from metode.sistem_persamaan_linear import eliminasi_gauss_naive

# --- Impor dari folder 'utils' ---
from utils.parser import (
    parse_matriks_interaktif,
    parse_vektor_interaktif,
)

# --- Definisi Sub-Menu ---


def menu_spl():
    """Menangani sub-menu untuk Sistem Persamaan Linear."""
    print("\n--- Menu Eliminasi Gauss ---")
    try:
        n = int(input("Masukkan jumlah variabel (n): "))
        if n <= 0:
            print("Error: n harus bilangan bulat positif.")
            return

        A = parse_matriks_interaktif(n)
        b = parse_vektor_interaktif(n)

        print("\nMatriks A yang Anda masukkan:")
        print(A)
        print("\nVektor b yang Anda masukkan:")
        print(b)

        # Memanggil fungsi logika inti
        print("\nMenghitung solusi...")
        solusi_x = eliminasi_gauss_naive(A, b)

        print("\n--------------------------")
        print("Solusi (x):")
        print(solusi_x)
        print("--------------------------")

    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka.")
    except ZeroDivisionError as e:
        print(f"Error Perhitungan: {e}")
    except Exception as e:
        print(f"Error: Terjadi kesalahan: {e}")


# --- Fungsi Menu Utama ---


def jalankan_menu_utama():
    """Menampilkan dan menjalankan menu utama aplikasi."""
    print("=" * 40)
    print("  Selamat Datang di Kalkulator Numerik")
    print("=" * 40)

    while True:
        print("\nPilih Metode:")
        print("  1. Sistem Persamaan Linear (Eliminasi Gauss)")
        print("  0. Keluar")

        pilihan = input("Masukkan pilihan Anda (0-1): ").strip()

        if pilihan == "1":
            menu_spl()
        # elif pilihan == "2":
        #     menu_cari_akar()
        # elif pilihan == "3":
        #     menu_integrasi()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
