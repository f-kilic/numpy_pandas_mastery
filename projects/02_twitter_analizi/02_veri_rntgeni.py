
import pandas as pd

print("--- 1. AŞAMA: CSV'DEN VERİ OKUMA ---")
# Az önce diğer dosyanın ürettiği CSV'yi içeri alıyoruz
df = pd.read_csv('kirli_tweetler.csv')

print("\n--- ORİJİNAL KİRLİ VERİ RÖNTGENİ ---")
print(df.info())


print("\n--- 2. AŞAMA: TEMİZLİK AMELİYATI ---")
# Senin kendi bulduğun mühendislik mantığı: 
# Metinlerde medyan olmaz, boş string ("") atıyoruz.
df['Tweet_Metni'] = df['Tweet_Metni'].fillna("")

# Beğeniler ve Retweetler ise sayıdır. Onların boşluklarını kendi medyanlarıyla doldur.
medyan_begeni = df['Begeniler'].median()
df['Begeniler'] = df['Begeniler'].fillna(medyan_begeni)

medyan_retweet = df['Retweetler'].median()
df['Retweetler'] = df['Retweetler'].fillna(medyan_retweet)

print("\n--- TEMİZLİK SONRASI RÖNTGEN ---")
print(df.info())

print("\n==================================================")
print(" 3. AŞAMA: KULLANICI ETKİLEŞİM ANALİZİ")
print("==================================================")

# 1. Adım: Yeni bir kolon oluştur: Toplam Etkileşim
# Analiz yaparken bazen var olan kolonları toplayıp yeni bir anlam yaratırız.
df['Toplam_Etkilesim'] = df['Begeniler'] + df['Retweetler']

# 2. Adım: Kullanıcı bazlı gruplama
# Hangi kullanıcı ortalama ne kadar etkileşim alıyor?
kullanici_performans = df.groupby('Kullanici')['Toplam_Etkilesim'].mean().sort_values(ascending=False)

print("Kullanıcıların Ortalama Etkileşim Performansı:")
print(kullanici_performans)