import unittest
from kavra import Ag, mse
from ornekler.ve_kapisi import VERI

class KavraTests(unittest.TestCase):
    def test_mse(self):
        self.assertAlmostEqual(mse([0.0, 1.0], [0.0, 0.0]), 0.5)

    def test_mse_rejects_empty(self):
        with self.assertRaises(ValueError):
            mse([], [])

    def test_and_learns(self):
        ag = Ag(2, [4, 1], tohum=7)
        ag.egit(VERI, tur_sayisi=6000, oran=0.7, rapor=0)
        for x, y in VERI:
            self.assertEqual(int(ag.tahmin(x)[0] >= 0.5), int(y[0]))

if __name__ == "__main__":
    unittest.main()
