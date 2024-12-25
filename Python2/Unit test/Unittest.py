import unittest
import sys
import os

sys.path.append(r"C:\Users\aryes\OneDrive\Desktop\skillcaptain\Python\Python2\Add to Cart")

from addToCart import Product, Cart

class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Laptop", 999.99, 10)
        self.product2 = Product("Mouse", 19.99, 50)
        self.cart = Cart("TestUser")

    def test_add_to_cart_valid_quantity(self):
        result = self.cart.add_to_cart(self.product1, 2)
        self.assertTrue(result)
        self.assertEqual(len(self.cart.products), 1)
        self.assertEqual(self.cart.products[0].quantity, 2)
        self.assertEqual(self.product1.quantity, 8)

    def test_add_to_cart_invalid_quantity(self):
        result = self.cart.add_to_cart(self.product1, 15)
        self.assertFalse(result)
        self.assertEqual(len(self.cart.products), 0)

    def test_remove_from_cart(self):
        self.cart.add_to_cart(self.product1, 1)
        result = self.cart.remove_from_cart("Laptop")
        self.assertTrue(result)
        self.assertEqual(len(self.cart.products), 0)

    def test_display_cart_empty(self):
        result = self.cart.display_cart()
        self.assertEqual(result, "TestUser's cart is empty.")

    def test_display_cart_with_products(self):
        self.cart.add_to_cart(self.product1, 1)
        self.cart.add_to_cart(self.product2, 2)
        result = self.cart.display_cart()
        self.assertIn("Laptop", result)
        self.assertIn("Mouse", result)

if __name__ == "__main__":
    unittest.main()
