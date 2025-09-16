from optimizer import find_market
while True:
    print("1-alışveriniz için en uygun marketler"
          "2- ürünlerin fiyat tahminleri")
    secim=int(input("uygun seçimi yapınız:"))
    if secim==1:
        butce=int(input("bütçenizi giriniz:"))
        urunler=input("sepetinize eklemek istediğiniz urunleri seçiniz:").split()
        liste,sonuc=find_market(butce,urunler)
        print(liste)
        print(sonuc)
    elif secim==2:
        print("çok yakında hizmete açılacaktır")
    else:
        break
