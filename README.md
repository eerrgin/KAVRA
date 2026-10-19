KAVRA

Saf Python ile Yapay Sinir Ağı Projesi

KAVRA, yapay sinir ağlarının temel çalışma mantığını anlaşılır, modüler ve incelenebilir bir Python projesi üzerinden ele alan bir yazılım projesidir.

Projenin amacı; nöronlardan katmanlara, ileri beslemeden geri yayılıma kadar temel sinir ağı bileşenlerini bir araya getirerek yapay öğrenmenin nasıl çalıştığını incelemektir.

«Proje sahibi: Ergin Kaplan
Depo: "eerrgin/KAVRA" (https://github.com/eerrgin/KAVRA)
Programlama dili: Python
Proje durumu: Geliştirme aşamasında»

---

🧠 Proje Hakkında

KAVRA, yapay sinir ağlarının temel kavramlarını harici makine öğrenmesi kütüphanelerine bağımlı olmadan incelemeyi hedefler.

Proje, temel matematiksel işlemleri ve sinir ağı bileşenlerini Python kodları üzerinden takip etmeyi kolaylaştıracak şekilde düzenlenmiştir.

Temel bileşenler

- Nöronlar: Girdilerin ve ağırlıkların işlenmesi.
- Katmanlar: Nöronların bir araya getirilmesi.
- Aktivasyon fonksiyonu: Sigmoid aktivasyonunun kullanılması.
- İleri besleme (Forward Propagation): Girdilerden çıktı üretilmesi.
- Hata hesabı: Ortalama kare hata (MSE) yaklaşımı.
- Geri yayılım (Backpropagation): Hatanın ağırlık güncellemelerinde kullanılması.
- Testler: Temel işlevlerin doğrulanması için test altyapısı.

Not: Bileşenlerin mevcut uygulama durumu ve test sonuçları kod çalıştırılarak doğrulanmalıdır.

---

📁 Proje Yapısı

KAVRA/
├── README.md
├── LICENSE
├── main.py
├── kavra_kur.py
├── test_kavra.py
└── ...

Dosyaların ve klasörlerin tam listesi için deponun ana dizinini inceleyebilirsin.

---

⚙️ Gereksinimler

- Python 3.9 veya üzeri
- Git (depoyu klonlamak için)

Mevcut uygulamanın harici paket gerektirmediği hedeflenmektedir. Çalıştırmadan önce kaynak kodundaki bağımlılıkları kontrol et.

---

🚀 Kurulum ve Çalıştırma

1. Depoyu klonla

git clone https://github.com/eerrgin/KAVRA.git
cd KAVRA

2. Python sürümünü kontrol et

python --version

3. Projeyi başlat

python main.py

Bazı sistemlerde "python" yerine "python3" kullanman gerekebilir.

4. Testleri çalıştır

python -m unittest test_kavra.py

Test komutu, test dosyasının mevcut içe aktarma yapısıyla uyumlu olduğu doğrulandıktan sonra kullanılmalıdır.

---

🎯 Projenin Hedefleri

KAVRA'nın geliştirme hedefleri:

- Yapay sinir ağlarının temel mantığını anlaşılır kodlarla göstermek.
- Modüler ve bakımı kolay bir dosya yapısı oluşturmak.
- Eğitim ve test süreçlerini otomatikleştirmek.
- Örneklerle öğrenme sürecini görünür kılmak.
- Kod kalitesini ve test kapsamını geliştirmek.
- İlerleyen sürümlerde yeni ağ mimarileri ve özellikler eklemek.

---

🛠️ Geliştirme Planı

- [ ] Kurulum ve çalıştırma adımlarını doğrulamak
- [ ] Birim testlerini çalıştırmak ve eksikleri gidermek
- [ ] Girdi ve çıktı örnekleri eklemek
- [ ] Hata yönetimini geliştirmek
- [ ] GitHub Actions ile otomatik test süreci kurmak
- [ ] Sürüm ve değişiklik kayıtlarını düzenlemek

---

🤝 Katkıda Bulunma

KAVRA'yı geliştirmek için hata bildirimleri, iyileştirme önerileri ve kod katkıları değerlidir.

1. Depoyu forklayın.
2. Yeni bir dal oluşturun.
3. Değişikliklerinizi yapın.
4. Testleri çalıştırın.
5. Pull request gönderin.

---

📄 Lisans

Lisans koşulları için depodaki "LICENSE" dosyasını inceleyin. Yeniden kullanım ve dağıtım koşulları bu dosyada belirtilen lisansa tabidir.

---

👤 Proje Sahibi

Ergin Kaplan

GitHub: "@eerrgin" (https://github.com/eerrgin)

---

KAVRA, yapay sinir ağlarının temel mekanizmalarını Python üzerinden incelemek ve geliştirmek amacıyla yürütülen bir yazılım projesidir.
