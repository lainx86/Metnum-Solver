import numpy as np
from metode.sistem_persamaan_linear import eliminasi_gauss_naive

def test_eliminasi_gauss_naive_simple():
    """
    Menguji fungsi eliminasi_gauss_naive dengan sistem persamaan linear sederhana.
    """
    A = np.array([[2, 1], [1, 3]])
    b = np.array([4, 7])
    expected_x = np.array([1, 2])
    
    actual_x = eliminasi_gauss_naive(A, b)
    
    # Membandingkan hasil dengan toleransi floating point
    np.testing.assert_allclose(actual_x, expected_x, rtol=1e-5, atol=1e-5)

def test_eliminasi_gauss_naive_larger_system():
    """
    Menguji fungsi eliminasi_gauss_naive dengan sistem yang lebih besar.
    """
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    expected_x = np.array([1, -2, -2]) # Solusi yang diketahui
    
    actual_x = eliminasi_gauss_naive(A, b)
    
    np.testing.assert_allclose(actual_x, expected_x, rtol=1e-5, atol=1e-5)

def test_eliminasi_gauss_naive_zero_pivot():
    """
    Menguji kasus di mana pivot nol akan menyebabkan masalah (meskipun naive tidak menanganinya).
    Ini lebih untuk menunjukkan batasan metode naive.
    """
    A = np.array([[0, 1], [1, 1]])
    b = np.array([1, 2])
    
    # Metode naive akan gagal dengan ZeroDivisionError jika pivot adalah 0
    # Kita bisa menguji bahwa error ini memang terjadi
    try:
        eliminasi_gauss_naive(A, b)
        assert False, "ZeroDivisionError expected but not raised"
    except ZeroDivisionError:
        assert True
    except Exception as e:
        assert False, f"Expected ZeroDivisionError, but got {type(e).__name__}"
