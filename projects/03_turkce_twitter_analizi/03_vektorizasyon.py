
import sklearn
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from snowballstemmer import TurkishStemmer
stemmer = TurkishStemmer()

print("--- 1. VERİ ŞANTİYEYE GETİRİLİYOR ---")
# 1. DOĞRU DOSYA YOLU: Dosyanın gerçekte bulunduğu klasörü gösteriyoruz
df = pd.read_csv("projects/00_csv/twitter_nlp_tam_temiz.csv") 

# 2. DOĞRU SÜTUN ADI: sütunun gerçek adını yazıyoruz ('tweet_text')
df = df.dropna(subset=['tweet_text']) 

print("--- 2. TF-IDF MAKİNESİ KURULUYOR ---")
vectorizer = TfidfVectorizer()

# 3. DOĞRU SÜTUN ADI: Metinleri al ve matematiksel matrise dönüştür
X_matrisi = vectorizer.fit_transform(df['tweet_text'])

print("--- 3. İŞLEM BAŞARILI ---")
print("Şantiyenin Boyutu (Satır, Sütun):", X_matrisi.shape)




from sklearn.model_selection import train_test_split

print("\n--- 4. HEDEF (Y) BELİRLENİYOR VE VERİ BÖLÜNÜYOR ---")

# 1. Hedefimizi (Cevap Anahtarını) belirliyoruz. Biz neyi tahmin etmeye çalışıyoruz? 'label' sütununu!
y_cevaplar = df['label']

# 2. Bıçağı indiriyoruz! %80 Çalışma (Train), %20 Sınav (Test)
X_train, X_test, y_train, y_test = train_test_split(
    X_matrisi,          # Sorular (Matrisimiz)
    y_cevaplar,         # Cevap Anahtarı (1'ler ve 0'lar)
    test_size=0.20,     # %20'sini sınava ayır, kasaya kilitle
    random_state=42     # Veriyi rastgele karıştır ama her çalıştırdığımızda aynı şekilde karıştır ki test edebilelim
)

# 3. Bölünmüş verinin boyutlarını kontrol et
print(f"Eğitim İçin Ayrılan Tweet Sayısı: {X_train.shape[0]}")
print(f"Sınav (Test) İçin Saklanan Tweet Sayısı: {X_test.shape[0]}")


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("\n==================================================")
print(" 5. AŞAMA: YAPAY ZEKA (MODEL) EĞİTİLİYOR")
print("==================================================")

# 1. Modeli şantiyeye çağır (Zeki ama henüz eğitimsiz)
model = LogisticRegression(random_state=42)

# 2. Modeli Eğit! (Çalışma sorularını ve cevap anahtarını veriyoruz)
# Makine şu an 957 tweet'in içindeki 9690 kelimenin matematiğini çözüyor...
model.fit(X_train, y_train)
print("Model eğitimi tamamlandı! Makine artık kelimelerin gücünü biliyor.")


print("\n==================================================")
print(" 6. AŞAMA: FİNAL SINAVI (TEST AŞAMASI)")
print("==================================================")

# 3. Kasadaki 240 soruyu (X_test) makinenin önüne koy ve tahmin etmesini iste!
tahminler = model.predict(X_test)

# 4. Sınav Sonucunu (Karne) Açıkla!
# Makinenin verdiği cevaplar (tahminler) ile cebimizdeki gerçek cevapları (y_test) karşılaştır.
basari_orani = accuracy_score(y_test, tahminler)

print(f"\n--- MODELİN SINAV BAŞARISI: % {basari_orani * 100:.2f} ---")

# 5. Detaylı Karne (Hangi konuda iyi, nerede çuvalladı?)
print("\n--- DETAYLI KARNE (CLASSIFICATION REPORT) ---")
print(classification_report(y_test, tahminler))


print("\n==================================================")
print(" 6. AŞAMA: GERÇEK DÜNYA TESTİ (CANLI YAYIN)")
print("==================================================")

def yapay_zeka_tahmin_et(yeni_tweet):
    temiz_tweet = str(yeni_tweet).lower()
    temiz_tweet = re.sub(r'[^\w\s]', '', temiz_tweet)
    temiz_tweet = ' '.join([stemmer.stemWord(kelime) for kelime in temiz_tweet.split()])
    # Temizlenmiş tweeti boşluklardan parçala, her kelimenin kökünü bul ve tekrar birleştir.
  

   

    
    # DİKKAT: Yeni cümlede sadece transform kullanıyoruz!
    vektor = vectorizer.transform([temiz_tweet])
    tahmin = model.predict(vektor)
    
    if tahmin[0] == 1:
        return f"🔴 [ÜRÜN/ŞİKAYET VAR - 1] -> {yeni_tweet}"
    else:
        return f"🟢 [GEYİK/ÜRÜN YOK - 0]  -> {yeni_tweet}"

# Test Cümleleri
test_cumleleri = [
    "Yeni aldığım klavyenin tuşları çok sert, yazarken parmaklarım ağrıyor. İade edeceğim.", 
    "Yarın hava çok güzel olacakmış, sahile inip biraz yürüyüş yapalım mı?", 
    "Kargom 3 gündür şubede bekliyor, böyle rezalet bir müşteri hizmetleri görmedim!", 
    "Dün akşamki maç efsaneydi, o golü nasıl kaçırdı hala inanamıyorum.",
    "Şampuan saçlarımı kepek yaptı, hiç memnun kalmadım.",
    "İzlediğimiz sinema filminin adını hatırlayamıyorum.",
    "Hayat bazen gerçekten tuhaf hissettiriyor."
]

print("\n--- TEST SONUÇLARI ---")
for cumle in test_cumleleri:
    print(yapay_zeka_tahmin_et(cumle))
    print("-" * 60)


# ==============================================================================
# 📌 MİMARİ NOT VE SÜRÜM GEÇMİŞİ (V1 -> V2 Geçişi)
# ==============================================================================
# [V1 Sorunu - Boyutluluk Laneti]: İlk sürümde Türkçe metinler sadece Regex ile 
# temizlendiği için, sondan eklemeli dil yapısı (örn: klavye, klavyenin, klavyeler) 
# modelin 9690 kolonluk (feature) devasa bir matris oluşturmasına (overfitting) 
# ve canlı yayın testlerinde "Eğitim-Çıkarım Asimetrisi" yaşamasına neden oldu.
#
# [V2 Çözümü - Morfolojik Analiz]: Sisteme 'SnowballStemmer' entegre edildi. 
# Kelimeler köklerine indirgenerek (Stemming) feature sayısı 6744'e düşürüldü. 
# Gelen canlı test verileri de modele girmeden önce aynı kök bulucu işlemden 
# geçirildi. Model artık ekleri değil, anlamsal kökleri sınıflandırarak 
# yüksek doğrulukla çalışmaktadır.
# ==============================================================================