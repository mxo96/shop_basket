from unittest import TestCase
from unittest.mock import patch, Mock

from items.product import Product
from utils.extract_basket import create_product_with_tax, extract_shop_basket


class TestExtractBasket(TestCase):

    def test_create_product_should_return_product_object_with_tax_and_taxed_price(self):
        test_pipe_separated_value = "book|book|12.49"
        result = create_product_with_tax(test_pipe_separated_value)
        self.assertEqual("book", result.name)
        self.assertEqual(12.49, result.price)
        self.assertEqual("book", result.category)
        self.assertEqual(0, result.tax)
        self.assertEqual(12.49, result.taxed_price)

    @patch("utils.extract_basket.create_product_with_tax")
    def test_extract_shop_basket_should_return_basket_object(self, mock_create_product):
        mock_product = Mock(spec=Product, taxed_price=12.49, tax=0)
        mock_create_product.return_value = mock_product

        test_products_from_form = {"product": "book|book|12.49"}
        result = extract_shop_basket(test_products_from_form)
        self.assertEqual(12.49, result.total)
        self.assertEqual(0, result.sales_tax)
        self.assertEqual([mock_product], result.products)
