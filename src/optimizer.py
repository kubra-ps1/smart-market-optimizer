from src.data_loader import load_latest_prices,load_data
import pandas as pd

df_son_gun,son_tarih=load_latest_prices()
df_pivot=df_son_gun.pivot_table(index=["tarih", "ürün"], columns="market", values="fiyat")
urun_fiyat={}

def find_market(urunler):
   liste=[]
   for index , row in df_son_gun.iterrows():
     urun=row["ürün"]
     market=row["market"]
     fiyat=row["fiyat"]
     if urun not in urun_fiyat:
        urun_fiyat[urun]={}
     urun_fiyat[urun][market]=fiyat
   toplam = 0
   for urun in urunler:
       market_fiyat = urun_fiyat[urun]
       en_ucuz_market = min(market_fiyat, key=market_fiyat.get)
       liste.append(f"{urun} : {en_ucuz_market} - {market_fiyat[en_ucuz_market]} TL ")
   return  liste


def optimize_market(df_musteri,butce):
    urunler = df_musteri['ürün'].tolist()
    miktarlar = df_musteri['miktar'].tolist()

    dp = [{} for _ in range(len(urunler)+1)]
    dp[0][butce] = (0, [])

    for i, urun in enumerate(urunler, 1):
        miktar = miktarlar[i-1]
        try:
            fiyatlar = df_pivot.loc[(son_tarih,urun)].dropna()
        except KeyError:
            continue

        for b_prev, (cost_prev, secim_prev) in dp[i-1].items():
            for market, fiyat in fiyatlar.items():
                maliyet = fiyat * miktar
                if b_prev >= maliyet:
                    b_kalan = b_prev - maliyet
                    toplam_maliyet = cost_prev + maliyet
                    if b_kalan not in dp[i] or toplam_maliyet < dp[i][b_kalan][0]:
                        dp[i][b_kalan] = (
                            toplam_maliyet,
                            secim_prev + [(urun, market, maliyet)]
                        )

    if dp[len(urunler)]:
        en_iyi = min(dp[len(urunler)].values(), key=lambda x: x[0])
        toplam_maliyet, secimler = en_iyi
        return toplam_maliyet, secimler
    else:
        return None, None











