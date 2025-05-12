import pandas as pd

def prepare_time_data():
    df = pd.read_csv("data/cleaned_orders.csv")
    df['PURCHASE_TS'] = pd.to_datetime(df['PURCHASE_TS'], errors='coerce', infer_datetime_format=True)
    df['SHIP_TS'] = pd.to_datetime(df['SHIP_TS'], errors='coerce', infer_datetime_format=True)

    df['purchase_month'] = df['PURCHASE_TS'].dt.to_period('M')
    df['purchase_day'] = df['PURCHASE_TS'].dt.day_name()
    df['shipping_delay'] = (df['SHIP_TS'] - df['PURCHASE_TS']).dt.days

    return df

def get_monthly_revenue(df):
    monthly_revenue = df.groupby('purchase_month')['USD_PRICE'].sum()
    monthly_revenue.index = monthly_revenue.index.astype(str)  # 👈 convierte Period a string
    return monthly_revenue.to_dict()

def get_day_sales(df):
    return df.groupby('purchase_day')['USD_PRICE'].sum().sort_values(ascending=False).to_dict()

def get_average_shipping_delay(df):
    return round(df['shipping_delay'].mean(), 2)
