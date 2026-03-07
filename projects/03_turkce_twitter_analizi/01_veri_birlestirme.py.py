import pandas as pd

print("--- 1. AŞAMA: PARÇALANMIŞ VERİLERİ OKUMA ---")
# Göreli yol (Relative Path) kullanarak dosyaları okuyoruz
df_urun_yok = pd.read_csv('projects/00_csv/notproduct.csv')
df_urun_var = pd.read_csv('projects/00_csv/product.csv')

print(f"Ürün geçmeyen tweet sayısı: {len(df_urun_yok)}")
print(f"Ürün geçen tweet sayısı: {len(df_urun_var)}")

print("\n--- 2. AŞAMA: TABLOLARI BİRLEŞTİRME (CONCAT) ---")
# İki tabloyu alt alta (axis=0) yapıştırıyoruz
df_toplam = pd.concat([df_urun_yok, df_urun_var], axis=0, ignore_index=True)

print("\n--- BİRLEŞTİRİLMİŞ YENİ VERİNİN RÖNTGENİ ---")
print(df_toplam.info())


print("\n==================================================")
print(" 3. AŞAMA: VERİYİ MAKİNE ÖĞRENMESİNE HAZIRLAMA")
print("==================================================")

# 1. Gürültüyü Sil: URL sütununa ihtiyacımız yok
df_toplam.drop('url', axis=1, inplace=True)
print("Gereksiz 'url' sütunu silindi.")

# 2. Etiketleri Sayısallaştır (Binary Encoding)
# Etiketlerin tam olarak ne yazdığını görmek için önce benzersiz değerlere bakalım
print("\nMevcut Etiketler:", df_toplam['label'].unique())

# 'nonproduct'  yazanları 0, 'product'  yazanları 1 yapıyoruz.
# 
sozluk = { 'nonproduct': 0,'product': 1,  }

df_toplam['label'] = df_toplam['label'].map(sozluk)

print("\n--- TEMİZLENMİŞ NİHAİ RÖNTGEN ---")
print(df_toplam.info())
print("\nİlk 5 Satır:\n", df_toplam.head())

# 3. Temiz ve Birleşik Veriyi Kaydet
# Bunu 00_csv klasörüne, makine öğrenmesi aşamasında kullanmak üzere kaydediyoruz.
kayit_yolu = 'projects/00_csv/twitter_birlestirilmis_temiz.csv'
df_toplam.to_csv(kayit_yolu, index=False)
print(f"\nOperasyon tamam! Temiz veri şuraya kaydedildi: {kayit_yolu}")