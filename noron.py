"""Tek yapay sinir hücresi."""
import random
from .aktivasyon import sigmoid

class Noron:
    def __init__(self, giris_sayisi, rng=None):
        if giris_sayisi < 1:
            raise ValueError("Nöron en az bir girdi almalı.")
        rng = rng or random
        self.agirliklar = [rng.uniform(-1.0, 1.0) for _ in range(giris_sayisi)]
        self.esik = rng.uniform(-1.0, 1.0)
        self.son_girdi = None
        self.son_cikti = None

    def ileri(self, girdiler):
        if len(girdiler) != len(self.agirliklar):
            raise ValueError("Girdi sayısı ağırlık sayısıyla eşleşmeli.")
        self.son_girdi = list(girdiler)
        toplam = sum(x * w for x, w in zip(girdiler, self.agirliklar)) + self.esik
        self.son_cikti = sigmoid(toplam)
        return self.son_cikti
