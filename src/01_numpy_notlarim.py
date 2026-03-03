
import numpy as np 

# Numpy (Numerical Python) sayısal hesaplamalar için geliştirilmiş bir kütüphanedir.
# Pandas yeterliyse neden Numpy?
# Çünkü Numpy tek tip (homojen) veri taşır, bellekte ardışıktır ve çok daha hızlıdır.
# AI dünyasında (scikit-learn vb.) temel yapı taşıdır.

my_list = [1, 2, 5, [0, 1], [2, 3, 5]]
# Python listeleri esnektir, içine liste bile alırız ama matematiksel işlemde yavaştır.

# 1. TEMEL ARRAY OLUŞTURMA VE BOYUT (SHAPE)
tek_boyutlu_dizi = np.array([1, 2, 3, 4, 5])
iki_boyutlu_dizi = np.array([[1, 2, 3], [4, 5, 6]]) 
# NOT: Matrisler "simetrik" değil, "homojen" (düzenli/dikdörtgensel) olmalıdır. 
# Satırların eleman sayısı eşit olmalı, yoksa Numpy hata verir.

print("Tek boyutlu shape:", tek_boyutlu_dizi.shape)
print("İki boyutlu shape:", iki_boyutlu_dizi.shape) # (2, 3) -> 2 satır, 3 sütun

# 2. DİLİMLEME (SLICING) VE VIEW (GÖRÜNÜM) MANTIĞI
a = np.array([
    [3, 7, 3, 4],
    [5, 6, 7, 2],
    [2, 1, 1, 1]
])

b = a[:2, 1:3] # 0. ve 1. satırı al, 1. ve 2. sütunu al (3 dahil değil)
print("a'nın orijinal hali:\n", a)

# DÜZELTME: b'yi a'dan kopyalamadım. b, a'nın bir "penceresidir" (View).
a[0, 1] = 99
print("a[0,1] 99 yapıldıktan sonra b'nin ilk elemanı:", b[0, 0]) 
# Çıktı 99 olur. Çünkü aynı belleğe bakıyorlar. Kopyalamak isteseydim a.copy() derdim.

# 3. YENİDEN BOYUTLANDIRMA (RESHAPE) VE BİRLEŞTİRME (STACKING)
birinci_dizi = np.arange(10).reshape(2, -1) # -1 demek: "Sütun sayısını sen ayarla" (burada 5 olur)
ikinci_dizi = np.repeat(1, 10).reshape(2, -1)

# İki diziyi birleştirirken append KULLANILMAZ.
# Dikey birleştirme (satır satır üst üste koyma) için vstack kullanılır.
yigin = np.vstack((birinci_dizi, ikinci_dizi))
print("Yığınlanmış Dizi (vstack):\n", yigin)

# 4. MATEMATİKSEL İŞLEMLER VE AXIS
# np.mean() ortalama, np.median() medyan, np.std() standart sapma verir.
# axis=1 -> Sütunlar boyunca (her bir satırın kendi içinde) işlem yapar.
# axis=0 -> Satırlar boyunca (her bir sütunun kendi içinde) işlem yapar.

# 5. ALIŞTIRMA DÜZELTMESİ: KAYAN PENCERE (SLIDING WINDOW)

def time_resolved(dizi, pencere_genisligi, kayma):
    # Boş liste oluşturup, Numpy dizisinden kestiğimiz pencereleri içine atıyoruz.
    pencereler = []
    
    # range(başlangıç, bitiş, adım)
    for i in range(0, len(dizi) - pencere_genisligi + 1, kayma):
        alt_dizi = dizi[i : i + pencere_genisligi]
        pencereler.append(alt_dizi) # Python listesinde append yapmak sorun değildir.
        
    return np.array(pencereler) # En son tek seferde Numpy matrisine çeviriyoruz.

test_dizisi = np.array([1, 2, 6, 4, 5, 4, 2, 7, 8, 9])
sonuc = time_resolved(test_dizisi, 3, 4)
print("Time Resolved Sonucu:\n", sonuc)