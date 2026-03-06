import pandas as pd
import numpy as np

print("Kirli Twitter Verisi Oluşturuluyor...\n")

data = {
    'Tweet_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Kullanici': ['veri_kurdu', 'furkan_dev', 'anonim', 'furkan_dev', 'python_fan', 'anonim', 'veri_kurdu', 'ahmet123', 'furkan_dev', 'bot_hesap'],
    'Tweet_Metni': ['Pandas çok iyi!', 'Bugün hava harika.', np.nan, 'Veri analizi zor ama zevkli.', 'Python > All', 'Reklam tweeti...', 'Eksik veri can sıkar', np.nan, 'Groupby mantığını çözdüm', 'Tıkla para kazan!'],
    'Begeniler': [150, 45, 0, np.nan, 300, 2, np.nan, 15, 85, 0],
    'Retweetler': [15, 2, 0, np.nan, 50, 0, 10, 1, 12, 0],
    'Hesap_Yasi_Gun': [365, 120, 5, 120, 800, 2, 365, 45, 120, 1]
}

df_twitter = pd.DataFrame(data)
df_twitter.to_csv('kirli_tweetler.csv', index=False)
print("Veri 'kirli_tweetler.csv' adıyla kaydedildi. Makine durduruldu.")