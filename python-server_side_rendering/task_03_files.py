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
