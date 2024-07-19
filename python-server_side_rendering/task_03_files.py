#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)

    return render_template('items.html', data=data.get('items', []))

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in  ['json', 'csv']:
        return render_template('product_display.html', errorMessage="Wrong source")

    file = f"products.{source}"
    def rjf(file):
        with open(file, "r") as file:
            return json.load(file)

    def rcf(file):
        with open(file, 'r') as file:
            csv_reader = csv.DictReader(file)
            return [
                    {key: float(value) if key == 'price' else int(value) if key == 'id' else value for key, value in row.items()}
                    for row in csv_reader
                    ]
    read_function = rcf if source == "csv" else rjf

    try:
        products = read_function(file)
    except FileNotFoundError:
        return render_template('product_display.html', errorMessage=f"File {file} notfound")

    if product_id:
        product_id = int(product_id)
        products = [i for i in products if i['id'] == product_id]
        if not products:
            return render_template('product_display.html', errorMessage="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
