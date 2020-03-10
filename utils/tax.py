from math import ceil

NO_TAXED_CATEGORIES = ['book', 'food', 'medical']


def percentage_tax(category, imported):
    percentage = 0
    if imported:
        percentage += 5
    return percentage + 10 if category not in NO_TAXED_CATEGORIES else percentage


def tax_price(price, perc_tax):
    return ceil(price * perc_tax / 100 * 20) / 20
