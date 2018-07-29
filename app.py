from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/product")
def product():
    return render_template('product.html')


@app.route("/product1")
def product1():
    return render_template('product1.html')


@app.route("/product2")
def product2():
    return render_template('product2.html')


@app.route("/product3")
def product3():
    return render_template('product3.html')


@app.route("/virtual_currency_guide")
def virtual_currency_guide():
    return render_template('virtual_currency_guide.html')


@app.route("/contect")
def contect():
    return render_template('contect.html')


if __name__ == '__main__':
    app.run(debug=True)