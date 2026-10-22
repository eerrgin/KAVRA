"""Küçük, tam bağlantılı ve sigmoid aktivasyonlu sinir ağı."""
import random
from katman import Katman
from aktivasyon import sigmoid_turev_cikti
from kayip import mse

class Ag:
    def __init__(self, giris_sayisi, katman_yapisi, tohum=None):
        if giris_sayisi < 1:
            raise ValueError("Girdi sayısı pozitif olmalı.")
        if not katman_yapisi or any(n < 1 for n in katman_yapisi):
            raise ValueError("En az bir katman ve her katmanda pozitif nöron sayısı olmalı.")
        self.rng = random.Random(tohum)
        self.katmanlar = []
        onceki = giris_sayisi
        for noron_sayisi in katman_yapisi:
            self.katmanlar.append(Katman(noron_sayisi, onceki, rng=self.rng))
            onceki = noron_sayisi

    def ileri(self, girdiler):
        cikti = list(girdiler)
        for katman in self.katmanlar:
            cikti = katman.ileri(cikti)
        return cikti

    def tahmin(self, girdiler):
        return self.ileri(girdiler)

    def egit_ornegi(self, girdiler, hedef, oran=0.3):
        if oran <= 0:
            raise ValueError("Öğrenme oranı pozitif olmalı.")
        if len(hedef) != len(self.katmanlar[-1].noronlar):
            raise ValueError("Hedef boyutu çıkış katmanıyla eşleşmeli.")
        aktivasyonlar = [list(girdiler)]
        for katman in self.katmanlar:
            aktivasyonlar.append(katman.ileri(aktivasyonlar[-1]))
        tum_deltalar = [None] * len(self.katmanlar)
        son = self.katmanlar[-1]
        tum_deltalar[-1] = [
            (noron.son_cikti - beklenen) * sigmoid_turev_cikti(noron.son_cikti)
            for noron, beklenen in zip(son.noronlar, hedef)
        ]
        for li in range(len(self.katmanlar) - 2, -1, -1):
            mevcut = self.katmanlar[li]
            sonraki = self.katmanlar[li + 1]
            deltalar = []
            for i, noron in enumerate(mevcut.noronlar):
                aktarilan = sum(
                    sonraki.noronlar[j].agirliklar[i] * tum_deltalar[li + 1][j]
                    for j in range(len(sonraki.noronlar))
                )
                deltalar.append(aktarilan * sigmoid_turev_cikti(noron.son_cikti))
            tum_deltalar[li] = deltalar
        for li, katman in enumerate(self.katmanlar):
            onceki_aktivasyonlar = aktivasyonlar[li]
            for noron, delta in zip(katman.noronlar, tum_deltalar[li]):
                for i, deger in enumerate(onceki_aktivasyonlar):
                    noron.agirliklar[i] -= oran * delta * deger
                noron.esik -= oran * delta
        return mse(aktivasyonlar[-1], hedef)

    def egit(self, veri, tur_sayisi=6000, oran=0.3, rapor=1000):
        if not veri:
            raise ValueError("Eğitim verisi boş olamaz.")
        if tur_sayisi < 1:
            raise ValueError("Tur sayısı en az 1 olmalı.")
        for tur in range(1, tur_sayisi + 1):
            sirali = list(veri)
            self.rng.shuffle(sirali)
            for girdiler, hedef in sirali:
                if len(hedef) != len(self.katmanlar[-1].noronlar):
                    raise ValueError("Hedef boyutu çıkış katmanıyla eşleşmeli.")
                self.egit_ornegi(girdiler, hedef, oran)
            if rapor and (tur == 1 or tur % rapor == 0 or tur == tur_sayisi):
                hata = sum(mse(self.ileri(x), y) for x, y in veri) / len(veri)
                print(f"Tur {tur:5d} | MSE: {hata:.6f}")
