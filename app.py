from flask import Flask, render_template, request

from utils.extract_basket import extract_shop_basket

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/receipt', methods=['POST'])
def shop_receipt():
    basket = extract_shop_basket(request.form.to_dict())
    return render_template('receipt.html', basket=basket)

