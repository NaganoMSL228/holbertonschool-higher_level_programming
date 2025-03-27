from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def create_database():
    """Create and populate the SQLite database if it doesn't exist"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Check if data exists
    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products_data = []
    error_message = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_data = json.load(f)
        except Exception as e:
            error_message = f"Error reading JSON file: {str(e)}"

    elif source == 'csv':
        try:
            products_data = []
            with open('products.csv', 'r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    # Convert ID and price to appropriate types
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_data.append(row)
        except Exception as e:
            error_message = f"Error reading CSV file: {str(e)}"

    elif source == 'sql':
        try:
            # Ensure database exists and is populated
            create_database()

            # Connect to the database
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row  # This enables column access by name
            cursor = conn.cursor()

            # Fetch data
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()

            # Convert to dictionary format
            for row in rows:
                products_data.append({
                    'id': row['id'],
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })

            conn.close()
        except Exception as e:
            error_message = f"Error accessing SQLite database: {str(e)}"

    else:
        error_message = "Wrong source"

    # Filter by ID if provided
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered_data = [p for p in products_data if p['id'] == product_id]
            if filtered_data:
                products_data = filtered_data
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid product ID"

    return render_template('product_display.html', products=products_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
