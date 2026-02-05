#Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.

class Pizza:

    pizza_flavour = {
                     'hawaiian': ['ham', 'pineapple'],
                     'meat_festival': ['beef', 'meatball', 'bacon'],
                     'garden_feast': ['spinach', 'olives', 'mushroom']
                    }
    order_count = 0

    def __init__(self, ingredients):
        Pizza.order_count += 1
        self.order_number = Pizza.order_count
        self.ingredients = ingredients

    @classmethod
    def hawaiian(cls):
        return cls(cls.pizza_flavour['hawaiian'])

    @classmethod
    def meat_festival(cls):
        return cls(cls.pizza_flavour['meat_festival'])

    @classmethod
    def garden_feast(cls):
        return cls(cls.pizza_flavour['garden_feast'])


p1 = Pizza(["bacon", "parmesan", "ham"])
print(p1.ingredients) #['bacon', 'parmesan', 'ham']
print(p1.order_number) # 1

p2 = Pizza.garden_feast()
print(p2.ingredients) #['spinach', 'olives', 'mushroom']
print(p2.order_number) # 2