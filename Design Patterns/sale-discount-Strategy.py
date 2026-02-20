class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy


    def price_after_discount(self):
        if self.discount_strategy:
            return self.discount_strategy(self)
        return self.price

    def __str__(self):
        after_discount = self.price_after_discount()
        return f"Price: {self.price}, price after discount: {after_discount}"

def on_sale_discount(order):
    return order.price * 0.5


def twenty_percent_discount(order):
    return order.price * 0.8


print(Goods(20000)) #Price: 20000, price after discount: 20000
print(Goods(20000, discount_strategy=twenty_percent_discount)) #Price: 20000, price after discount: 16000.0
print(Goods(20000, discount_strategy = on_sale_discount)) #Price: 20000, price after discount: 10000.0

