from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_data(filepath):
    products = []
    try:
        with open(filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except Exception:
        pass
    return products

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
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except Exception:
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        data = read_json_data('products.json')
    elif source == 'csv':
        data = read_csv_data('products.csv')
    else:
        return render_template('product_display.html', error_message="Wrong source")
    
    if product_id:
        data = [p for p in data if str(p.get('id')) == str(product_id)]
        if not data:
            return render_template('product_display.html', error_message="Product not found")
            
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
