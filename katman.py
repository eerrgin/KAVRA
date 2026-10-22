"""Nöronlardan oluşan katman."""
from noron import Noron

class Katman:
    def __init__(self, noron_sayisi, giris_sayisi, rng=None):
        if noron_sayisi < 1:
            raise ValueError("Katmanda en az bir nöron olmalı.")
        self.noronlar = [Noron(giris_sayisi, rng=rng) for _ in range(noron_sayisi)]

    def ileri(self, girdiler):
        return [noron.ileri(girdiler) for noron in self.noronlar]
