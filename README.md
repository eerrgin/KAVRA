# KAVRA
### Kendi Anlayan Veri ile Rasyonel Aklı

**KAVRA**, yapay sinir ağlarının temel mantığını saf Python ile öğretmek için hazırlanan küçük bir eğitim projesidir. İleri besleme, sigmoid aktivasyonu, ortalama kare hata ve geri yayılımı adım adım göstermeyi amaçlar.

> **Durum:** Öğrenme amaçlı prototip. Büyük ölçekli veya üretim ortamında kullanılmak üzere tasarlanmamıştır.

## Özellikler
- Harici Python paketi olmadan çalışır.
- Modüler sürüm ve tek dosyalık öğretici sürüm içerir.
- AND ve XOR mantık kapısı örnekleri içerir.
- Birim testleriyle temel davranış kontrol edilir.

## Gereksinimler
- Python 3.9 veya üzeri
- Git, yalnızca GitHub'a göndermek için

## Hızlı başlangıç

Proje klasöründe terminal açıp çalıştır:

```bash
python main.py
```

Tek dosyalık sürüm:

```bash
python kavra_v0.py
```

Testler:

```bash
python -m unittest discover -s tests -v
```

## XOR örneğini çalıştırma
`main.py` içindeki bu satırı:

```python
from ornekler.ve_kapisi import VERI
```

şu satırla değiştir:

```python
from ornekler.xor_kapisi import VERI
```

Sonra `python main.py` komutunu yeniden çalıştır. XOR gibi doğrusal olmayan bir problem için gizli katman gerekir. Öğrenme başarısı başlangıç ağırlıkları ve eğitim ayarlarından etkilenir; bu küçük eğitim uygulaması her rastgele başlangıçta başarı garantisi vermez.

## Dosya yapısı

```text
KAVRA/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── kavra_kur.py
├── kavra_v0.py
├── main.py
├── kavra/
│   ├── __init__.py
│   ├── aktivasyon.py
│   ├── kayip.py
│   ├── noron.py
│   ├── katman.py
│   ├── ag.py
│   └── egitim.py
├── ornekler/
│   ├── __init__.py
│   ├── ve_kapisi.py
│   └── xor_kapisi.py
└── tests/
    └── test_kavra.py
```

## Mimari
- `Noron`: ağırlıklı toplam ve sigmoid aktivasyonu hesaplar.
- `Katman`: nöronları bir araya getirir.
- `Ag`: katmanlar arasında ileri besleme ve geri yayılımı yürütür.
- `Egitmen`: eğitim ayarlarını ağın eğitim metoduna iletir.
- `mse`: tahmin ve hedef arasındaki ortalama kare hatayı hesaplar.

## Yol haritası
- [x] Saf Python ile ileri besleme ve geri yayılım
- [x] AND ve XOR veri kümeleri
- [x] Temel birim testleri
- [ ] ReLU ve tanh aktivasyonları
- [ ] Modeli JSON ile kaydetme/yükleme
- [ ] Eğitim geçmişini dosyaya aktarma ve grafikleme
- [ ] İsteğe bağlı NumPy hızlandırması

## Lisans
MIT lisansı. Ayrıntılar `LICENSE` dosyasındadır.
