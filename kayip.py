"""Kayıp fonksiyonları."""

def mse(tahmin, hedef):
    """Tahmin ve hedef listeleri arasındaki ortalama kare hata."""
    if len(tahmin) != len(hedef):
        raise ValueError("Tahmin ve hedef uzunlukları aynı olmalı.")
    if len(tahmin) == 0:
        raise ValueError("Boş listeler için MSE hesaplanamaz.")
    return sum((t - h) ** 2 for t, h in zip(tahmin, hedef)) / len(tahmin)
