from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('KEY')

PRODUCT = None
CATEGORY = None
TAG = None
BRAND = None
URL = 'http://makeup-api.herokuapp.com/api/v1/products.json'


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        global PRODUCT
        PRODUCT = request.form.get("search")
        return redirect(url_for('results', brand=PRODUCT))

    return render_template('home.html')


@app.route('/results')
def results():
    parameters = {
        "brand": PRODUCT
    }
    response = requests.get(URL, json=parameters)
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    product_list = []
    for item in data:
        product_list.append(dict(item))
    return render_template('results.html', data=product_list)


@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'POST':
        global PRODUCT
        global TAG
        PRODUCT = request.form.get("product_name")
        TAG = request.form.get('tag')
        return redirect(url_for('tags_results', tags=TAG, product=PRODUCT))

    return render_template('tag_search.html')


@app.route('/tags-result')
def tags_results():
    parameters = {
        "product_type": PRODUCT,
        "product_tags": TAG
    }
    response = requests.get(URL, json=parameters)
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    product_list = []
    for item in data:
        product_list.append(dict(item))
    return render_template('tag_search_results.html', data=product_list)


@app.route('/category', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        global PRODUCT
        global CATEGORY
        PRODUCT = request.form.get("product_name")
        CATEGORY = request.form.get("category")
        return redirect(url_for('category_results', product=PRODUCT, category=CATEGORY))

    return render_template('category.html')


@app.route('/category-results')
def category_results():
    parameters = {
        "product_type": PRODUCT,
        "product_category": CATEGORY
    }
    response = requests.get(URL, json=parameters)
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    product_list = []
    for item in data:
        product_list.append(dict(item))
    return render_template('category_results.html', data=product_list)


@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        global PRODUCT
        global BRAND
        PRODUCT = request.form.get("product_name")
        BRAND = request.form.get("brand")
        return redirect(url_for('product_search', product=PRODUCT, brand=BRAND))
    return render_template('products.html')


@app.route('/product-search')
def product_search():
    parameters = {
        "product_type": PRODUCT,
        "brand": BRAND
    }
    response = requests.get(URL, json=parameters)
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    product_list = []
    for item in data:
        product_list.append(dict(item))
    return render_template('product-search.html', data=product_list)


if __name__ == "__main__":
    app.run(debug=True)
