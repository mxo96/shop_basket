from unittest import TestCase

from items.product import Product


class TestProduct(TestCase):

    def test_init_should_init_product_book(self):
        product = Product("Book", 12.49, "book")
        self.assertEqual(product.name, "Book")
        self.assertEqual(product.price, 12.49)
        self.assertEqual(product.category, "book")
        self.assertFalse(product.imported)
        self.assertEqual(0, product.tax)

    def test_init_should_init_product_imported_chocolates(self):
        product = Product("imported box of chocolates", 10.00, "food")
        self.assertEqual(product.name, "imported box of chocolates")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.category, "food")
        self.assertTrue(product.imported)
        self.assertEqual(0, product.tax)

    def test_init_should_init_product_imported_perfume(self):
        product = Product("imported bottle of perfume", 47.50, "other")
        self.assertEqual(product.name, "imported bottle of perfume")
        self.assertEqual(product.price, 47.50)
        self.assertEqual(product.category, "other")
        self.assertTrue(product.imported)
        self.assertEqual(0, product.tax)
