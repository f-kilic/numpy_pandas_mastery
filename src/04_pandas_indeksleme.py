
import pandas as pd

# ---------------------------------------------------------
# 1. SERIES (1 BOYUTLU) ÜZERİNDE SORGULAMA VE FİLTRELEME
# ---------------------------------------------------------
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

print("--- Temel Sorgular ---")
# Bir indeksin varlığını sorgulama (Hızlı ve etkili)
print("'a' indeksi var mı?:", 'a' in data)

# keys() ve index Serilerde tamamen aynı şeyi verir.
print("Keys:", data.keys())
print("Index:", data.index)

print("\n--- Boolean Masking (Vektörel Filtreleme) ---")

# Amacımız 0.3'ten büyük, 0.8'den küçük olanları bulmak.
maske = (data > 0.3) & (data < 0.8)
print(data[maske])

# Matematiksel işlemleri tüm seriye aynı anda uygulayabiliriz (Vektörizasyon)
data['f'] = data['a'] * 2
print("\n'f' eklendikten sonra data:\n", data)


# ---------------------------------------------------------
# 2. DATAFRAME (2 BOYUTLU) ÜZERİNDE loc VE iloc MANTIĞI
# ---------------------------------------------------------

df = pd.DataFrame({
    'yas': [21, 25, 30],
    'skor': [85, 90, 75]
}, index=['kisi_A', 'kisi_B', 'kisi_C'])

print("\n--- DataFrame: loc vs iloc ---")
# .loc -> ETİKET (Label) bazlı indeksleme
# Format: df.loc['satır_etiketi', 'sütun_etiketi']
print("loc ile Kisi_A'nın skoru:", df.loc['kisi_A', 'skor'])

# .iloc -> TAM SAYI (Integer) bazlı indeksleme (NumPy gibi 0'dan başlar)
# Format: df.iloc[satır_indeksi, sütun_indeksi]
print("iloc ile 0. satır, 1. sütun (Kisi_A skoru):", df.iloc[0, 1])

# DataFrame'lerde satırları sütun, sütunları satır yapmak:
print("\n--- Transpoze (.T) İşlemi ---")
print(df.T)