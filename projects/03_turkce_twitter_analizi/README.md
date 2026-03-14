# Türkçe Twitter Verisi ile Uçtan Uca NLP ve Metin Sınıflandırma (PoC)

## 📌 Proje Özeti
Bu proje, Twitter üzerinden elde edilen gürültülü metin verilerini Doğal Dil İşleme (NLP) teknikleri ile temizleyerek, tweetlerin "Ürün Şikayeti/Yorumu (1)" veya "Günlük Geyik (0)" olup olmadığını sınıflandıran bir Makine Öğrenmesi boru hattı (pipeline) oluşturmayı amaçlamaktadır. Proje bir Proof of Concept (PoC) çalışmasıdır. 

**V2 Güncellemesi ile:** Türkçe'nin sondan eklemeli yapısından kaynaklanan "Boyutluluk Laneti" (Curse of Dimensionality) ve aşırı öğrenme (overfitting) sorunları, morfolojik analiz (Stemming) ile çözülmüş ve model gerçek dünya verilerine karşı optimize edilmiştir.

## ⚙️ Kullanılan Teknolojiler
* **Veri İşleme:** Pandas, NumPy
* **Doğal Dil İşleme (NLP):** Regular Expressions (Regex), Stop Words Filtreleme, **SnowballStemmer (Kelime Kökü Bulma)**
* **Makine Öğrenmesi:** Scikit-Learn, TF-IDF Vectorizer, Logistic Regression, Train-Test Split
* **Veri Görselleştirme:** Matplotlib

## 🏗️ Proje Mimarisi
Proje, kodun okunabilirliğini artırmak amacıyla Separation of Concerns prensibine uygun şekilde modüler olarak yapılandırılmıştır.

### 1️⃣ Veri Birleştirme (`01_veri_birlestirme.py`)
* Parçalı CSV veri setlerinin birleştirilmesi ve etiketlerin sayısallaştırılması.

### 2️⃣ Metin Temizleme, Analiz ve Kök Bulma (`02_filtreleme_analizi.py`)
* Metinlerin küçük harfe dönüştürülmesi ve noktalama işaretlerinin Regex ile temizlenmesi.
* Türkçe stop words filtreleme.
* **[V2] Stemming (Kök Bulma):** `SnowballStemmer` kullanılarak kelimelerin eklerinden arındırılması ve morfolojik köklerine indirgenmesi.

### 3️⃣ Vektörizasyon ve Model Eğitimi (`03_vektorizasyon.py`)
* Temizlenmiş ve köklerine ayrılmış metinlerin TF-IDF yöntemi ile sayısal özelliklere dönüştürülmesi.
* Lojistik Regresyon modeli ile sınıflandırma.
* Canlı test verilerinde "Eğitim-Çıkarım Asimetrisini" önlemek için test girdilerine de Stemming uygulanması.
* **TF-IDF Çıktısı (V2):** 957 eğitim tweeti, **6744** benzersiz kelime özelliği (V1'deki 9690'dan düşürüldü).

## 📊 Model Performansı
Veri seti %80 eğitim ve %20 test olacak şekilde ayrılmıştır.
* **Accuracy:** %90.00
* **Precision (Sınıf 1 – Ürün):** 0.96
* **Recall (Sınıf 0 – Geyik):** 0.97

## ⚠️ Mimari Not ve Sürüm Geçmişi (V1 -> V2)
* **[V1 Sorunu - Boyutluluk Laneti]:** İlk sürümde metinler sadece Regex ile temizlendiği için, Türkçe'nin sondan eklemeli dil yapısı (örn: klavye, klavyenin) modelin 9690 kolonluk devasa bir matris oluşturmasına (overfitting) ve canlı yayın testlerinde çuvallamasına neden oldu.
* **[V2 Çözümü - Morfolojik Analiz]:** Sisteme `SnowballStemmer` entegre edildi. Kelimeler köklerine indirgenerek özellik (feature) sayısı 6744'e düşürüldü. Canlı test verileri de modele girmeden önce aynı kök bulucu işlemden geçirildi. Model artık ekleri değil, anlamsal kökleri sınıflandırarak yüksek doğrulukla çalışmaktadır.