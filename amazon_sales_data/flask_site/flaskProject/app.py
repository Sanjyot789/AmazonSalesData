from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from flask_caching import Cache
from textblob import TextBlob

# Initialize Flask app and caching
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)

# Database connection
engine = create_engine("mysql+pymysql://root:password@localhost/Amazon_sales_data")

# Load data from MySQL
@cache.cached(timeout=60)
def load_data():
    query = "SELECT * FROM AmazonSales;"
    return pd.read_sql(query, engine)

# Homepage route
@app.route("/")
def index():
    data = load_data()
    categories = data['category'].unique()
    return render_template("index.html", categories=categories)

# Dashboard route
@app.route("/dashboard", methods=["GET"])
def dashboard():
    data = load_data()

    # Filters
    selected_category = request.args.get("category", None)
    min_rating = float(request.args.get("min_rating", 0))
    page = int(request.args.get("page", 1))
    per_page = 10

    # Filter data
    if selected_category:
        data = data[data['category'] == selected_category]
    data = data[data['rating'] >= min_rating]

    # Paginate data
    total_pages = (len(data) + per_page - 1) // per_page
    data_paginated = data.iloc[(page - 1) * per_page: page * per_page]

    # KPIs
    total_products = len(data)
    avg_rating = round(data['rating'].mean(), 2) if total_products > 0 else 0
    max_discount = round(data['discount_percentage'].max(), 2) if total_products > 0 else 0

    # Visualizations
    top_products = data.nlargest(10, 'rating')
    bar_chart = px.bar(
        top_products,
        x='product_name', y='rating',
        title='Top Rated Products'
    ).to_json()

    scatter_plot = px.scatter(
        data, x='discount_percentage', y='rating',
        title='Discount Percentage vs Rating',
        labels={'discount_percentage': 'Discount (%)', 'rating': 'Rating'}
    ).to_json()

    # Sentiment Analysis
    data['sentiment'] = data['review_content'].apply(
        lambda x: 'Positive' if TextBlob(str(x)).sentiment.polarity > 0
        else 'Negative' if TextBlob(str(x)).sentiment.polarity < 0 else 'Neutral'
    )
    sentiment_counts = data['sentiment'].value_counts().to_dict()

    return render_template(
        "dashboard.html",
        bar_chart=bar_chart,
        scatter_plot=scatter_plot,
        total_products=total_products,
        avg_rating=avg_rating,
        max_discount=max_discount,
        page=page,
        total_pages=total_pages,
        sentiment_counts=sentiment_counts,
        data_paginated=data_paginated.to_dict(orient="records")
    )

# Run the app
if __name__ == "__main__":
    app.run(debug=True)