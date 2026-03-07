import pandas as pd

filtreli_veriler= pd.read_csv('projects/00_csv/twitter_birlestirilmis_temiz.csv')

# print(filtreli_veriler.info) 
 
# Eğer info yazarsam, Python sana o objenin (tablonun) kaba bir önizlemesini verir (ilk 5 ve son 5 satırlı çıktı).

# Eğer info() yazarsan, bu bir fonksiyondur (çalıştır emridir) ve  Non-Null Count ve Dtype yazan gerçek röntgeni verir.


filtreli_veriler= filtreli_veriler[ filtreli_veriler['label'] == 1 ]

# print(filtreli_veriler)


# Pandas'a "Metinleri kesme, ne kadar uzun olursa olsun tam göster" emrini veriyoruz.
pd.set_option('display.max_colwidth', None)

# Sadece filtrelenmiş verinin (1 olanların) ilk 5 satırını tam metin olarak yazdır.
print("\n--- ÜRÜN İÇEREN TWEETLER (TAM METİN) ---")
print(filtreli_veriler.head())



print("\n==================================================")
print(" 4. AŞAMA: METİN ÖN İŞLEME (NLP PREPROCESSING)")
print("==================================================")

# 1. Hamle: Her Şeyi Küçük Harfe Çevir.
# str.lower() komutu Pandas'ta tüm sütunu küçük harf yapar.
filtreli_veriler['tweet_text'] = filtreli_veriler['tweet_text'].str.lower()
print("Tüm metinler küçük harfe çevrildi.")

# 2. Hamle: Noktalama İşaretlerini Sil 
# str.replace() komutu ile [^\w\s] Regex (Düzenli İfade) kalıbını kullanıyoruz.
# Bu kalıp şunu der: "Harf (w) ve boşluk (s) DIŞINDAKİ (^) her şeyi boşlukla değiştir (sil)."
filtreli_veriler['tweet_text'] = filtreli_veriler['tweet_text'].str.replace(r'[^\w\s]', '', regex=True)
print("Tüm noktalama işaretleri ve semboller temizlendi.")

print("\n--- İŞLENMİŞ NİHAİ METİNLER (İLK 5 SATIR) ---")
print(filtreli_veriler.head())



print("\n==================================================")
print(" 5. AŞAMA: FREKANS ANALİZİ VE STOP WORDS FİLTRESİ")
print("==================================================")

# 1. Bütün cümleleri kelime kelime parçalayıp devasa tek bir listeye (Series) çeviriyoruz
tum_kelimeler = filtreli_veriler['tweet_text'].str.split(expand=True).stack()

# 2. Türkçe'deki en çok kullanılan çöp kelimeleri (Stop Words) tanımlıyoruz
# Not: Eğer listede marka isminin önüne geçen başka anlamsız kelime görürsen, buraya ekleyebilirsin.
cop_kelimeler = ['1','olsun','sadece','10','4','aynı','marka','değil','tl','böyle','ürün','olan','oldu','bisküvi','sen','bence','15','sorun','5','memnunum','model','neden','tv','kulaklık','çamaşır','bile','gün','onu','yeni','şu','ki','kullanıyorum','şey','hiç','bana','aynı','bir', 'her', 'menü' , 'önce' ,' kulaklık', 'servis','sadece','10', 'bir', 've', 'daha','bi','ya','aldım','telefon', '2','3','paket','olarak','mu', 'bu', 'da', 'de', 'çok', 'için', 'gibi', 'ile', 'o', 'en', 'ne', 'var', 'mi', 'mı', 'ama', 'kadar', 'diye', 'ben', 'sonra', 'iyi', 'yok']

# 3. Çöp kelimeleri listemizden söküp atıyoruz
temiz_kelimeler = tum_kelimeler[~tum_kelimeler.isin(cop_kelimeler)]

# 4. Kalan kelimeleri saydırıp, zirvedeki ilk 20 kelimeyi ekrana basıyoruz!
print("--- TWITTER'DA EN ÇOK KONUŞULAN KELİMELER/MARKALAR ---")
print(temiz_kelimeler.value_counts().head(20))


import matplotlib.pyplot as plt

print("\n==================================================")
print(" 6. AŞAMA: VERİYİ GÖRSELLEŞTİRME (DASHBOARD)")
print("==================================================")

# İlk 15 markayı alıyoruz (Grafik çok kalabalık olmasın diye)
en_cok_gecenler = temiz_kelimeler.value_counts().head(15)

# Grafiğin boyutunu ve tasarımını ayarlıyoruz
plt.figure(figsize=(12, 6))
en_cok_gecenler.plot(kind='bar', color='steelblue', edgecolor='black')

# Başlıklar ve etiketler
plt.title('Twitter Türkiye: En Çok Konuşulan Markalar ve Ürünler', fontsize=16, fontweight='bold')
plt.xlabel('Markalar / Kelimeler', fontsize=12)
plt.ylabel('Bahsedilme Sayısı (Frekans)', fontsize=12)
plt.xticks(rotation=45, ha='right') # İsimler yan dursun, birbirine girmesin
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği ekrana bas!
print("Grafik oluşturuluyor... Lütfen açılan pencereyi kontrol et.")
plt.tight_layout()
plt.show()