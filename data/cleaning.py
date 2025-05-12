import pandas as pd

df = pd.read_excel("gamezone-orders-data.xlsx", sheet_name="orders")

# 1. Convert PURCHASE_TS to datetime
df['PURCHASE_TS'] = pd.to_datetime(df['PURCHASE_TS'], errors='coerce')

# 2. Check for missing values
print("\n🔍 Missing values after conversion:")
print(df.isnull().sum())

# 3. Drop rows with missing PRICE (since only 5 rows out of 21k)
df = df.dropna(subset=['USD_PRICE'])

# 4. Fill or tag missing marketing/account creation data
df['MARKETING_CHANNEL'] = df['MARKETING_CHANNEL'].fillna('unknown')
df['ACCOUNT_CREATION_METHOD'] = df['ACCOUNT_CREATION_METHOD'].fillna('unknown')

# 5.fill COUNTRY_CODE or drop — for now we keep it and tag
df['COUNTRY_CODE'] = df['COUNTRY_CODE'].fillna('unknown')
df = df.dropna(subset=['USD_PRICE', 'PURCHASE_TS'])


# 6. Confirm ORDER_ID is unique (should be 1-to-1)
print("\n✅ ORDER_ID unique?", df['ORDER_ID'].is_unique)

# 7. strip whitespace & lowercase for category columns
category_cols = ['PURCHASE_PLATFORM', 'MARKETING_CHANNEL', 'ACCOUNT_CREATION_METHOD', 'COUNTRY_CODE']
for col in category_cols:
    df[col] = df[col].str.strip().str.lower()


print("✅ Limpieza completa. Shape final:", df.shape)


df.to_csv("cleaned_orders.csv", index=False)

print("✅ Cleaned data saved as 'cleaned_gamezone_orders.csv'")
