"""Ağı eğitmek için basit sarmalayıcı sınıf."""
class Egitmen:
    def __init__(self, ag, oran=0.3):
        if oran <= 0:
            raise ValueError("Öğrenme oranı pozitif olmalı.")
        self.ag = ag
        self.oran = oran

    def egit(self, veri, tur_sayisi=6000, rapor=1000):
        self.ag.egit(veri, tur_sayisi=tur_sayisi, oran=self.oran, rapor=rapor)
