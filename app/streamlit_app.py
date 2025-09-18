import streamlit as st
import pandas as pd
from src.data_loader import load_latest_prices,load_data
from src.optimizer import find_market,optimize_market


df_son_gun, son_tarih = load_latest_prices()
df_pivot = df_son_gun.pivot_table(index=["tarih", "ürün"], columns="market", values="fiyat")

st.title("Akıllı Market Optimizasyonu")

st.header("En ucuz marketi bul")
urunler_find = st.text_input("Ürünleri virgülle ayırarak girin:", "")

if st.button("Marketleri Bul"):
    if urunler_find.strip():
        urunler_list = [u.strip() for u in urunler_find.split(",")]
        liste = find_market(urunler_list)
        st.subheader("Sonuçlar")
        for satir in liste:
            st.write(satir)
    else:
        st.warning("Lütfen en az bir ürün girin.")

st.markdown("---")

st.header("Müşteri Listesi ile Optimizasyon")

st.write("Her ürün için miktarı girin ve bütçenizi belirtin.")

urun_sayisi = st.number_input("Kaç farklı ürün ekleyeceksiniz?", min_value=1, max_value=20, value=1, step=1)

urun_list = []
miktar_list = []

for i in range(urun_sayisi):
    col1, col2 = st.columns(2)
    with col1:
        urun = st.text_input(f"{i + 1}. Ürün adı", key=f"urun_{i}")
    with col2:
        miktar = st.number_input(f"{i + 1}. Miktar", min_value=1, value=1, key=f"miktar_{i}")
    urun_list.append(urun)
    miktar_list.append(miktar)

butce = st.number_input("Bütçeniz (TL):", min_value=0, value=100)

if st.button("Optimizasyonu Hesapla"):
    # DataFrame oluştur
    df_musteri = pd.DataFrame({"ürün": urun_list, "miktar": miktar_list})
    toplam_maliyet, secimler = optimize_market(df_musteri, butce)

    if secimler:
        st.subheader(f"En düşük maliyet: {toplam_maliyet} TL")
        for urun, market, maliyet in secimler:
            st.write(f"{urun} : {market} → {maliyet} TL")
    else:
        st.error("Bütçe yetersiz, hiçbir kombinasyon uygun değil.")




df = load_data()

st.title("Ürün Fiyat Grafiği")
urun = st.selectbox("Ürün seçin:", df["ürün"].unique())
market = st.selectbox("Market seçin:", df["market"].unique())

grafik_tipi = st.radio("Grafik tipi seçin:", ["Çizgi Grafiği", "Bar Grafiği", "Saçılım Grafiği"])

df_plot = df[(df["ürün"] == urun) & (df["market"] == market)].sort_values("tarih").tail(30)  # son 30 gün

if grafik_tipi == "Çizgi Grafiği":
    st.line_chart(df_plot.set_index("tarih")["fiyat"])

elif grafik_tipi == "Bar Grafiği":
    st.bar_chart(df_plot.set_index("tarih")["fiyat"])

elif grafik_tipi == "Saçılım Grafiği":
    st.scatter_chart(df_plot, x="tarih", y="fiyat")



