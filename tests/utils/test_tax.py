from unittest import TestCase
from unittest.mock import patch

from utils.tax import percentage_tax, tax_price


@patch("utils.tax.NO_TAXED_CATEGORIES", ['no taxed category'])
class TestTax(TestCase):

    def test_percentage_tax_should_return_5_given_imported_food(self):
        result = percentage_tax("no taxed category", True)
        self.assertEqual(5, result)

    def test_percentage_tax_should_return_0_given_not_imported_book(self):
        result = percentage_tax("no taxed category", False)
        self.assertEqual(0, result)

    def test_percentage_tax_should_return_10_given_not_imported_music(self):
        result = percentage_tax("music", False)
        self.assertEqual(10, result)

    def test_percentage_tax_should_return_15_given_imported_other(self):
        result = percentage_tax("other", True)
        self.assertEqual(15, result)

    def test_tax_price_should_return_0_50_given_10_price_and_5_tax_perc(self):
        result = tax_price(10, 5)
        self.assertEqual(0.50, result)

    def test_tax_price_should_return_0_given_12_49_price_and_0_tax_perc(self):
        result = tax_price(12.49, 0)
        self.assertEqual(0, result)

    def test_tax_price_should_return_4_2_given_27_99_price_and_15_tax_perc(self):
        result = tax_price(27.99, 15)
        self.assertEqual(4.2, result)

    def test_tax_price_should_return_1_5_given_14_99_price_and_10_tax_perc(self):
        result = tax_price(14.99, 10)
        self.assertEqual(1.5, result)

    def test_tax_price_should_return_0_6_given_11_25_price_and_5_tax_perc(self):
        result = tax_price(11.25, 5)
        self.assertEqual(0.6, result)

    def test_tax_price_should_return_7_15_given_47_50_price_and_15_tax_perc(self):
        result = tax_price(47.50, 15)
        self.assertEqual(7.15, result)
