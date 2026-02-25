import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def get_discount(self):
        if self.count in range(5, 7):
            return 0.05
        elif self.count in range(7,10):
            return 0.1
        elif self.count in range(10, 20):
            return 0.2
        elif self.count == 20:
            return 0.3
        elif self.count > 20:
            return 0.5
        return 0


class Cart:
    def __init__(self, products):
        self.products_list = products

    def get_total_price(self):
        total = 0
        for product in self.products_list:
            discount = product.get_discount()
            product_total = (product.price * product.count) * (1 - discount)
            total += product_total
        return total


class CartTest(unittest.TestCase):
    def test_product_discount_zero(self):
        p = Product('test', 100, 4)
        self.assertEqual(p.get_discount(), 0)

    def test_product_discount_max(self):
        p = Product('test', 100, 25)
        self.assertEqual(p.get_discount(), 0.5)

    def test_product_discount_border(self):
        p = Product('test', 100, 20)
        self.assertEqual(p.get_discount(), 0.3)

    def test_cart_total(self):
        products = [Product('p1', 100, 10), Product('p2', 200, 2)]
        cart = Cart(products)
        self.assertEqual(cart.get_total_price(), 1200)



products = (Product('p1',10,4), Product('p2',100,5),
            Product('p3',200,6))
cart = Cart(products)
print(cart.get_total_price()) #1655.0


if __name__ == '__main__':
    unittest.main()