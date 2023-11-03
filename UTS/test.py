import unittest

# Fungsi sederhana yang akan diuji
def bagi(a, b):
    return a / b

# Kelas tes untuk menguji fungsi bagi
class TestBagi(unittest.TestCase):
    def test_bagi_angka_positif(self):
        hasil = bagi(6, 2)
        self.assertEqual(hasil, 3)  # Memeriksa pembagian angka positif
        print(f"Pengujian angka positif: 6 / 2 = {hasil}")

    def test_bagi_angka_negatif(self):
        hasil = bagi(-10, 2)
        self.assertEqual(hasil, -5)  # Memeriksa pembagian angka negatif
        print(f"Pengujian angka negatif: -10 / 2 = {hasil}")

    def test_bagi_nol(self):
        hasil = bagi(0, 7)
        self.assertEqual(hasil, 0)  # Memeriksa pembagian dengan nol
        print(f"Pengujian pembagian dengan nol: 0 / 7 = {hasil}")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestBagi))
    
    if result.wasSuccessful():
        print("Semua tes berhasil dijalankan!")
