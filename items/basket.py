from items.product import Product


class Basket:
    total = None
    sales_tax = None
    products = []

    def __init__(self):
        self.products = []
        self.sales_tax = 0
        self.total = 0

    def add_product(self, product):
        assert isinstance(product, Product)
        self.total = round(self.total + product.taxed_price, 2)
        self.sales_tax = round(self.sales_tax + product.tax, 2)
        self.products.append(product)


