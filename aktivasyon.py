"""Aktivasyon fonksiyonları."""
import math

def sigmoid(x):
    """Sayısal taşmayı azaltan sigmoid fonksiyonu."""
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)

def sigmoid_turev_cikti(cikti):
    """Sigmoid türevi; sigmoid fonksiyonunun çıktısını alır."""
    return cikti * (1.0 - cikti)
