import smtplib
from flask import Flask, render_template, url_for, flash, redirect, request
from firebase import firebase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

firebase = firebase.FirebaseApplication('https://python-f5763.firebaseio.com/')

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


@app.route("/sendInfo", methods = ['POST', 'GET'])
def sendInfo():
    result = request.form['mail']
    arr = firebase.get('/Habook',"test")
    arr.append(result)
    firebase.put('/Habook',"test",arr)
    return render_template('contect.html')

if __name__ == '__main__':
    app.run(debug=True)
