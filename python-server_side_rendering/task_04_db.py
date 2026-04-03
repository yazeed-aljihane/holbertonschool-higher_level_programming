from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        return None

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
    elif source == 'sql':
        data = read_sqlite_data()
        if data is None:
            return render_template('product_display.html', error_message="Database error")
    else:
        return render_template('product_display.html', error_message="Wrong source")
    
    if product_id:
        data = [p for p in data if str(p.get('id')) == str(product_id)]
        if not data:
            return render_template('product_display.html', error_message="Product not found")
            
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
