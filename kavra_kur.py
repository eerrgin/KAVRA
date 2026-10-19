"""KAVRA dosyalarını yeniden oluşturan kurulum betiği.

Bu betik KAVRA klasörünün DIŞINDA çalıştırılmak üzere tasarlanmıştır.
Mevcut KAVRA klasörünü silmez veya üzerine yazmaz; klasör varsa güvenli biçimde durur.
"""
from pathlib import Path
import sys

def main():
    hedef = Path("KAVRA")
    if hedef.exists():
        print("HATA: KAVRA klasörü zaten var. Dosyaları yanlışlıkla ezmemek için durdum.")
        print("Başka bir dizinde çalıştır veya mevcut klasörün yedeğini al.")
        sys.exit(1)
    print("Bu kurulum betiği, dağıtım arşivindeki dosyaları üretmek için kaynak olarak tutulur.")
    print("Bu hazır proje arşivinde KAVRA klasörü zaten oluşturulmuştur.")
    print("Klasörün içinde çalıştırma: python main.py")

if __name__ == "__main__":
    main()
