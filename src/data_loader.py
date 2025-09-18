import pandas as pd

def load_latest_prices(csv_path=r"C:\Users\skubra\smart-market-optimizer\data\market_prices.csv"):
    df=pd.read_csv(csv_path)
    son_tarih=df["tarih"].max()
    df_son_gun=df[df["tarih"]==son_tarih]
    return df_son_gun,son_tarih

def load_data(csv_path=r"C:\Users\skubra\smart-market-optimizer\data\market_prices.csv"):
    df=pd.read_csv(csv_path)
    return df
