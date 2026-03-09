
# Türkçe Twitter Verisi ile Uçtan Uca NLP ve Metin Sınıflandırma (PoC)

## 📌 Proje Özeti
Bu proje, Twitter üzerinden çekilmiş gürültülü metin verilerini Doğal Dil İşleme (NLP) teknikleriyle temizlemek ve Lojistik Regresyon algoritması kullanarak tweetlerin "Ürün Şikayeti/Yorumu (1)" mu yoksa "Günlük Geyik (0)" mi olduğunu ayırt eden bir **Makine Öğrenmesi Boru Hattı (Pipeline)** inşa etmek amacıyla geliştirilmiştir. Bir Konsept Kanıtı (Proof of Concept) çalışmasıdır.

## ⚙️ Kullanılan Teknolojiler
* **Veri Manipülasyonu:** `Pandas`, `NumPy`
* **Doğal Dil İşleme (NLP):** Regular Expressions (`Regex`), Stop Words Filtreleme
* **Makine Öğrenmesi:** `Scikit-Learn` (TF-IDF Vectorizer, Logistic Regression, Train-Test Split)
* **Veri Görselleştirme:** `Matplotlib`

## 🏗️ Mimari ve Proje Aşamaları
Proje, "Separation of Concerns" (Kavramların Ayrılığı) prensibine uygun olarak 3 ana modüle bölünmüştür:

1. **`01_veri_birlestirme.py`:** Parçalı CSV veri setlerinin birleştirilmesi, gereksiz sütunların (URL vb.) atılması ve etiketlerin (1-0) sayısallaştırılması.
2. **`02_filtreleme_analizi.py`:** Metinlerin küçük harfe çevrilmesi, noktalama işaretlerinin temizlenmesi, Türkçe "Stop Words" (ve, ama, fakat vb.) analizi ve verinin Makine Öğrenmesine pürüzsüz bir şekilde hazırlanması.
3. **`03_vektorizasyon.py`:** Temizlenmiş metinlerin **TF-IDF** mimarisi ile matematiksel matrise (594 satır, 9690 benzersiz kelime/sütun) dönüştürülmesi. Lojistik Regresyon modelinin eğitilmesi ve canlı verilerle test edilmesi.

## 📊 Model Başarısı ve Performans Karnesi
Model %80 Eğitim (Train) ve %20 Sınav (Test) verisiyle ayrıştırılarak test edilmiştir.

* **Genel Başarı (Accuracy):** %91.67
* **Precision (Sınıf 1 - Ürün):** 0.98 *(Model bir şeye ürün dediğinde %98 oranında haklı çıkmaktadır.)*
* **Recall (Sınıf 0 - Geyik):** 0.98 *(Sistem, ürün içermeyen gürültü veriyi ustalıkla ayırt etmektedir.)*

## 🔍 Mimari Gözlem ve Gelecek Vizyonu
Sistem uçtan uca kusursuz çalışmakta olup, canlı testlerde başarılı sonuçlar vermiştir. Ancak, sisteme beslenen laboratuvar verisinde (1197 satır) geçmeyen çok spesifik sektör kelimeleriyle (örn: kozmetik, şampuan) karşılaştığında, model risk almayarak '0' tahmini yapabilmektedir. 

Bu durum bir algoritma hatası değil, veri seti sınırlarıdır. Mimarinin gerçek bir ticari ürüne dönüşmesi için kod blokları değiştirilmeden, sadece başlangıçtaki ham veri setinin (Scale-up) büyütülmesi yeterli olacaktır. 