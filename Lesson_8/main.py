import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def categories():
    connection = sqlite3.connect('Goods.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Category FROM Goods_category")
        categories = list()
        for category in cursor:
            categories.append(*category)
    finally:
        connection.close()
    return render_template('index.html', categories=categories)


@app.route('/category/<category>')
def product_category(category=None):
    ID = None
    product_list = list()
    connection = sqlite3.connect('Goods.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Category_ID FROM Goods_category"
                       " WHERE Category=?", (category,))
        for category_id in cursor:
            ID = category_id[0]
        cursor.execute("SELECT Good_name FROM Store_goods"
                       " WHERE Category=? AND Is_available=?", (ID, 1))
        for product in cursor:
            product_list.append(*product)
    finally:
        connection.close()
    return render_template('available_products.html', products=product_list)


@app.route('/product/<product_name>')
def product(product_name=None):
    product_dict = dict()
    connection = sqlite3.connect('Goods.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Price, Amount FROM Store_goods"
                       " WHERE Good_name=?", (product_name,))
        for product_info in cursor:
            product_dict[product_name] = {'price': product_info[0], 'amount': product_info[1]}
    finally:
        connection.close()
        if product_name:
            product = product_dict.get(product_name, {'price': 0, 'amount': 0})
            product['name'] = product_name
            product['total'] = "{:.2f}".format(product['price'] * product['amount'])
            return render_template('product_info.html', products=product)


app.run(host='127.0.0.1', port='5000', debug=True)
