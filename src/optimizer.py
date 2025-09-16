from data_loader import load_latest_prices

df_son_gun=load_latest_prices()
urun_fiyat={}

def find_market(butce,urunler):
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
       toplam += market_fiyat[en_ucuz_market]
       liste.append(f"{urun} : {en_ucuz_market} - {market_fiyat[en_ucuz_market]} TL ")


   sonuc = "bütçeniz yeterli" if toplam < butce else "bütçeniz yetersiz"
   return liste, sonuc


