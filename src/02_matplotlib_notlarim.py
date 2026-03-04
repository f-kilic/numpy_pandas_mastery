# Matplotlib
# Veri görselleştirme, veri analizinin en önemli bölümlerinden biridir.
# Bize büyük veri kümelerine basit ve güçlü bir görsel erişim sağlar.
# Python'da görselleştirme için kullanılan temel kütüphane matplotlib'dir.
# Datayı betimlemek, farklı parametreleri kıyaslamak ve okuyucu gözünde anlatı
# kurabilmek, sezgi oluşturabilmek veri görselleştirmeden faydalanırız.
# Python ve R  diğer yapılandırılmış programlara kıyasla daha verimlidir.
# Analiz ve görseli aynı anda işleyebilmeyi mümkün kılar.

# Çizim (grafik türü seçmek)
# plt.plot(x,y) --> çizgi (trend/zaman serisi)
# plt.bar(x,h) --> bar/sütun (kategori karşılaştırma)
# plt.hist(data, bins=...) --> histogram (dağılım)
# plt.scatter(x,y) --> scatter (ilişki)

# Anlatı / Okunabilirlik
# plt.title("...") --> başlık
# plt.xlabel("...") / plt.ylabel("...") --> eksen isimleri ( birim ekle )
# plt.legend() --> seri açıklaması ( önce label )"..." verilmeli
# plt.grid(True) --> ızgara ( opsiyonel )

# Düzen
# plt.tight_layout() --> taşmaları düzelt, boşlukları ayarla

# Çıktı
# plt.savefig("fig.png",dpi=300) --> dosyaya keydet (rapor-tez için)
# plt.show() --> ekranda göster ( genelde en sonda )

# Tipik Akış
# Draw --> Label --> Layout --> Save --> Show 

import numpy as np
import matplotlib.pyplot as plt

#region girisornegı
x = [1, 2, 3, 4] 
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]
y3 = [17, 27, 37, 50]  

# DÜZELTME: Profesyonel kullanım için State-based (plt.plot) yerine 
# Object-Oriented (fig, ax) yapısına geçiyoruz.
fig1, ax1 = plt.subplots()

ax1.plot(x, y1, 'r--1', label='y1') #(r)red kırmızı olsun, çizgiler(--) şeklinde olsun ve 1 ters üçgen
ax1.plot(x, y2, 'k-1', label='y2')
ax1.plot(x, y3, 'go', label='y3')

ax1.set_xlabel('X label') # Object-Oriented yapıda fonksiyonların başına 'set_' gelir.
ax1.set_ylabel('Y label')
ax1.grid(True)
ax1.set_title('Bu bir baslıktır')
ax1.legend()
# plt.show()'u tüm figürleri tek seferde görmek için en sona taşıdım.
#endregion

#region ornek 2
t = np.arange(0, 5, 0.2) # 0 dan 5 e kadar 0,2 artan numpy arrayi

fig2, ax2 = plt.subplots()
ax2.plot(t, t, 'r', label='line one', linewidth=5)
ax2.plot(t, t**2, 'b--^', label='line two', linewidth=2)
ax2.plot(t, t**3, 'g-o', label='marker', markersize=4)

ax2.legend()
ax2.grid(True, alpha=0.5, color='k') # alpha saydamlik ayarlar
#endregion

#region histogram ornegi
# Histogram elimde tek değişken olduğunda ve bu tek değişkenin
# data içerisinde nasıl dağıldığını görmek için kullanılır.

pop_yas = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 45, 68, 78, 98, 57, 85, 88, 89]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

fig3, ax3 = plt.subplots()
ax3.hist(pop_yas, bins, histtype='bar', rwidth=0.8)

ax3.set_xlabel('yas gruplari')
ax3.set_ylabel('insan sayisi')
ax3.set_title('Histogram')
#endregion

#region ornek soru
#- 0 ile 1000 arasında rastgele değerler oluşturun ve bu değerleri grafik üzerinde gösterin.
#Grafikte, 500’den küçük değerler için mavi, 500’den büyük değerler için kırmızı renk kullanın.

data = np.random.randint(0, 1000, 50)
x = np.arange(50)

#  for döngüsü ve np.append KESİNLİKLE KULLANILMAZ (Bellek israfı).
#  Bunun yerine Pandas'ta da sürekli kullanacağımız "Boolean Masking" kullanılır.

maske_kirmizi = data > 500
maske_mavi = data <= 500

# Filtrelenmiş datalar (NumPy bunu C hızında anında arka planda ayırır)
data_kirmizi = data[maske_kirmizi]
indeks_kirmizi = x[maske_kirmizi]

data_mavi = data[maske_mavi]
indeks_mavi = x[maske_mavi]

fig4, ax4 = plt.subplots()
ax4.plot(x, data, "k--", alpha=0.3) # Tüm veriyi silik siyah bir çizgiyle gösterdim

# Nokta basmak için .plot değil .scatter kullanılır.
ax4.scatter(indeks_mavi, data_mavi, color="blue", marker="*", label="<= 500")
ax4.scatter(indeks_kirmizi, data_kirmizi, color="red", marker="^", label="> 500")

ax4.legend()
ax4.set_title('Filtrelenmiş Rastgele Veriler')

plt.show() # Ürettiğimiz fig1, fig2, fig3 ve fig4'ü aynı anda ekrana basar.
#endregion