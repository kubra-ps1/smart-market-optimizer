from optimizer import  optimize_market
import  pandas as pd

urunler=input("almak istediğiniz urunleri giriniz:").split()
miktarlar=list(map(int,input("ürünlerin miktarlarını giriniz:").split()))
butce=int(input("bütçenizi giriniz:"))

musteri_dic={"ürün":urunler,"miktar":miktarlar}

df_musteri=pd.DataFrame(musteri_dic)

print(df_musteri)

toplam_maliyet,secimler=optimize_market(df_musteri,butce)

if secimler:
    print(f"en düşük maliyet : {toplam_maliyet} TL")
    for urun,market,maliyet in secimler:
        print(f"{urun} : {market} , maliyet = {maliyet}")
else:
    print("bütçe yetersiz,hiçbir kombinasyon uygun değil.")

