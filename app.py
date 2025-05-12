from flask import Flask, render_template
from data.basic_analysis import (
    load_data,
    get_top_products,
    get_top_revenue_products,
    get_sales_by_platform,
    get_marketing_channel_counts,
    get_revenue_by_channel,
)
from data.time_analysis import (
    prepare_time_data,
    get_monthly_revenue,
    get_day_sales,
    get_average_shipping_delay,
)

app = Flask(__name__)

@app.route("/")
def home():
    df = load_data()
    df_time = prepare_time_data()
    total_orders = len(df)
    total_revenue = round(df['USD_PRICE'].sum(), 2)
    top_game = df['PRODUCT_NAME'].value_counts().idxmax()
    avg_delay = get_average_shipping_delay(df_time)

    return render_template("index.html",
        top_products=get_top_products(df),
        top_revenue_products=get_top_revenue_products(df),
        platform_sales=get_sales_by_platform(df),
        marketing_counts=get_marketing_channel_counts(df),
        revenue_by_channel=get_revenue_by_channel(df),
        monthly_revenue=get_monthly_revenue(df_time),
        day_sales=get_day_sales(df_time),
        avg_shipping_delay=avg_delay,
        total_orders=total_orders,
        total_revenue=total_revenue,
        top_game=top_game
    )

if __name__ == "__main__":
    app.run(debug=True)
