
import numpy as np
import pandas as pd

print("==================================================")
print(" 1. TEMEL VERİ OPERASYONLARI VE VEKTÖRİZASYON")
print("==================================================")
# RandomState ile rastgeleliği sabitliyoruz (Profesyonel test ortamı)
rng = np.random.RandomState(42)

ser2 = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
print("Orijinal DataFrame:\n", ser2)

print("\n--- Vektörel İşlemler (Ufuncs) ---")
# Döngü kullanmadan tüm tabloya aynı anda matematiksel işlem uygulama
print("Tüm hücrelerin e üssü x'i:\n", np.exp(ser2))
print("\nTüm hücrelerin (sin(x * pi / 4)) değeri:\n", np.sin(ser2 * np.pi / 4))

print("\n--- İndeks Hizalama (Index Alignment) ve fill_value ---")
area = pd.Series({'Alaska': 1723337, 'Texas': 695662, 'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127}, name='population')

# Pandas indeksleri otomatik eşleştirir. Eşleşmeyenlere NaN basar.
print("Doğrudan Bölme (NaN üretir):\n", population / area)

# NaN yerine varsayılan bir değer (2000) atayarak güvenli işlem yapma
print("\nfill_value ile Güvenli Ekleme:\n", area.add(population, fill_value=2000))

print("\nİndeks Kesişimi (Ortak Olanlar):", area.index.intersection(population.index))
print("İndeks Bileşimi (Hepsi):", area.index.union(population.index))


print("\n==================================================")
print(" 2. KAYIP VERİ (MISSING DATA) YÖNETİMİ")
print("==================================================")
data = pd.Series([1, np.nan, 'hello', None, 5])
print("Orijinal Kirli Veri:\n", data)

print("\nBoşlukları Silme (dropna):\n", data.dropna())
print("\nBoşlukları Doldurma (fillna):\n", data.fillna(0))


print("\n==================================================")
print(" 3. TABLOLARI BİRLEŞTİRME (CONCAT VE MERGE)")
print("==================================================")
df1 = pd.DataFrame({'A': ['A1', 'A2'], 'B': ['B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4'], 'B': ['B3', 'B4']})

print("Concat (Alt Alta Ekleme):\n", pd.concat([df1, df2], axis=0, ignore_index=True))

kullanicilar = pd.DataFrame({'kullanici_adi': ['furkan', 'ahmet', 'ayse'], 'yas': [21, 25, 30]})
tweetler = pd.DataFrame({'kullanici_adi': ['furkan', 'furkan', 'ayse'], 'tweet': ['Selam', 'Pandas zor', 'Naber']})

print("\nMerge (Ortak Sütuna Göre Eşleştirme):\n", pd.merge(tweetler, kullanicilar, on='kullanici_adi'))


print("\n==================================================")
print(" 4. GRUPLAMA VE ÇÖKERTME (GROUPBY)")
print("==================================================")
df_group = pd.DataFrame({
    'kullanici': ['A', 'B', 'C', 'A', 'B', 'C'],
    'atilan_tweet': [1, 2, 3, 4, 5, 6],
    'alinan_begeni': [10, 20, 30, 40, 50, 60]
})

print("Kullanıcıya Göre Toplam Beğeni:\n", df_group.groupby('kullanici')['alinan_begeni'].sum())
print("\nÇoklu Özetleme (Min, Max, Mean):\n", df_group.groupby('kullanici').aggregate({'atilan_tweet': ['min', 'max', 'mean']}))