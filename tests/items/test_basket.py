from unittest import TestCase
from unittest.mock import patch

from items.basket import Basket
from items.product import Product


class TestBasket(TestCase):

    def test_init_should_init_basket(self):
        basket = Basket()
        self.assertEqual(0, basket.total)
        self.assertEqual(0, basket.sales_tax)
        self.assertEqual([], basket.products)

    @patch("items.product.Product", spec=Product)
    def test_add_product_should_set_total_sales_taxes_and_add_product(self, mock_product):
        mock_product.name = "test name"
        mock_product.price = 10.00
        mock_product.category = "test category"
        mock_product.imported = False
        mock_product.tax = 0.50
        mock_product.taxed_price = 10.50

        basket = Basket()
        basket.add_product(mock_product)

        self.assertEqual(10.50, basket.total)
        self.assertEqual(0.50, basket.sales_tax)
        self.assertEqual([mock_product], basket.products)

    def test_add_product_should_raise_assertion_error_given_no_product_istance(self):
        basket = Basket()
        self.assertRaises(AssertionError, basket.add_product, "")
