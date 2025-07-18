from flask import Flask, render_template, request
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Simulate API data (replace with real API calls)
    sales_trend = requests.get('http://backend-url/api/sales-trend').json()
    top_products = requests.get('http://backend-url/api/top-products').json()
    forecast = requests.get('http://backend-url/api/forecast').json()
    summary_metrics = requests.get('http://backend-url/api/summary-metrics').json()

    return render_template('dashboard.html', sales_trend=sales_trend, top_products=top_products, forecast=forecast, summary_metrics=summary_metrics)

if __name__ == '__main__':
    app.run(debug=True)
