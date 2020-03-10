class Product:
    name = None
    price = None
    category = None
    imported = False
    tax = 0
    taxed_price = 0

    def __init__(self, name=name, price=price, category=category):
        self.name = name
        self.price = price
        self.category = category
        self.imported = True if 'imported' in self.name else False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_tax(self):
        return self.tax

    def set_tax_and_taxed_price(self, tax):
        self.tax = tax
        self.taxed_price = round(self.tax + self.price, 2)

    def is_imported(self):
        return self.imported

    def set_imported(self, imported):
        assert isinstance(imported, bool)
        self.imported = imported
