import pandas as pd

print("Titanic Veri Seti Yükleniyor...\n")

# Pandas ile internetteki raw CSV dosyasını doğrudan okuyoruz!
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

print("--- Tablonun İlk 5 Satırı (head) ---")
print(df.head())

print("\n--- Veri Setinin Röntgeni (info) ---")
print(df.info())


print("\n==================================================")
print(" VERİ TEMİZLİĞİ: 1. AŞAMA (SÜTUN SİLME)")
print("==================================================")
df.drop('Cabin', axis=1, inplace=True)
print("Cabin sütunu başarıyla silindi!")


print("\n==================================================")
print(" VERİ TEMİZLİĞİ: 2. AŞAMA (EKSİK VERİ DOLDURMA)")
print("==================================================")
medyan_yas = df['Age'].median()
print(f"Gemideki medyan yaş: {medyan_yas}")

df['Age'] = df['Age'].fillna(medyan_yas)
kalan_bos_yas_sayisi = df['Age'].isnull().sum()
print(f"Doldurma işleminden sonra kalan boş yaş verisi: {kalan_bos_yas_sayisi}")


print("\n==================================================")
print(" VERİ TEMİZLİĞİ: 3. AŞAMA (KATEGORİK VERİ DOLDURMA)")
print("==================================================")
en_cok_binilen_liman = df['Embarked'].mode()[0]
print(f"En çok yolcunun bindiği liman (Mod): {en_cok_binilen_liman}")

df['Embarked'] = df['Embarked'].fillna(en_cok_binilen_liman)


print("\n==================================================")
print(" 4. AŞAMA: VERİYİ KONUŞTURMA (GROUPBY ANALİZİ)")
print("==================================================")

kurtulma_oranlari = df.groupby('Sex')['Survived'].mean() * 100
print("\n--- Cinsiyete Göre Hayatta Kalma Oranları (%) ---")
print(kurtulma_oranlari)

kurtulma_oranlari2 = df.groupby('Pclass')['Survived'].mean() * 100
print("\n--- Bilet Sınıfına (Pclass) Göre Hayatta Kalma Oranları (%) ---")
print(kurtulma_oranlari2)

kurtulma_oranlari3 = df.groupby(['Sex', 'Pclass'])['Survived'].mean() * 100
print("\n--- Cinsiyet ve Sınıfa Göre Çapraz Hayatta Kalma Oranları (%) ---")
print(kurtulma_oranlari3)


print("\n==================================================")
print(" 5. AŞAMA: TEMİZ VERİYİ KAYDETME")
print("==================================================")
df.to_csv('titanic_temizlenmis.csv', index=False)
print("Ameliyat bitti. Temiz veri 'titanic_temizlenmis.csv' adıyla klasöre kaydedildi!")