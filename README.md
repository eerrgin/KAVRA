# KAVRA — Saf Python ile Yapay Sinir Ağı

KAVRA, sinir ağlarının ileri besleme, sigmoid aktivasyonu, geri yayılım ve ortalama kare hata (MSE) gibi temel parçalarını harici ML kütüphanesi olmadan göstermek üzere hazırlanmış eğitim projesidir.

## Gereksinim

Python 3.9+; harici paket gerekmez.

## Çalıştırma

Depo kök dizininde:

```bash
python main.py
python -m unittest test_kavra -v
```

## Modüller

- `ag.py`: ağ ve geri yayılım
- `katman.py`, `noron.py`: ağ yapısı
- `aktivasyon.py`, `kayip.py`: sigmoid ve MSE
- `egitim.py`: eğitim sarmalayıcısı
- `ve_kapisi.py`: AND kapısı eğitim verisi

## Sınırlar

Bu, küçük ve açıklanabilir bir eğitim uygulamasıdır; üretim ML çerçevesi veya genel amaçlı dil modeli değildir. AND kapısına ait test, yalnızca bu küçük örneğin beklenen davranışını doğrular.
