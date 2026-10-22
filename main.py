"""KAVRA modüler sürümünün giriş noktası."""
from ag import Ag
from egitim import Egitmen
from ve_kapisi import VERI


def main():
    print("=== KAVRA | modüler sürüm ===")
    ag = Ag(giris_sayisi=2, katman_yapisi=[4, 1], tohum=7)
    egitmen = Egitmen(ag, oran=0.7)
    egitmen.egit(VERI, tur_sayisi=6000, rapor=1000)
    print("\nTahminler:")
    for girdiler, hedef in VERI:
        tahmin = ag.tahmin(girdiler)[0]
        sinif = int(tahmin >= 0.5)
        print(f"{girdiler} -> {tahmin:.4f} | sınıf={sinif} | hedef={int(hedef[0])}")


if __name__ == "__main__":
    main()
