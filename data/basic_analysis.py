import pandas as pd

def load_data():
    return pd.read_csv("data/cleaned_orders.csv")

def get_top_products(df):
    return df['PRODUCT_NAME'].value_counts().head(10).to_dict()

def get_top_revenue_products(df):
    return df.groupby('PRODUCT_NAME')['USD_PRICE'].sum().sort_values(ascending=False).head(10).to_dict()

def get_sales_by_platform(df):
    return df['PURCHASE_PLATFORM'].value_counts().to_dict()

def get_marketing_channel_counts(df):
    return df['MARKETING_CHANNEL'].value_counts().to_dict()

def get_revenue_by_channel(df):
    return df.groupby('MARKETING_CHANNEL')['USD_PRICE'].sum().sort_values(ascending=False).to_dict()



