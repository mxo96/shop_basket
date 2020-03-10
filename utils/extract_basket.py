from items.basket import Basket
from items.product import Product
from utils.tax import tax_price, percentage_tax


def extract_shop_basket(products_from_form):
    products_selected = [product_values for form_input_name, product_values in products_from_form.items()]
    basket = Basket()
    for product_selected in products_selected:
        basket.add_product(create_product_with_tax(product_selected))
    return basket


def create_product_with_tax(pipe_separated_value):
    product = Product(name=pipe_separated_value.split('|')[0],
                      price=float(pipe_separated_value.split('|')[2]),
                      category=pipe_separated_value.split('|')[1])
    product.set_tax_and_taxed_price(
        tax_price(price=product.price,
                  perc_tax=percentage_tax(product.category,
                                          product.imported)))
    return product
