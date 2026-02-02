"""
Create function with name outer(name). This function should return inner function with name inner.
This inner function prints message Hello, <name>!
"""

def outer(name):
    def inner():
        print(f'Hello, {name}!')
    return inner

alice = outer("Alice")
alice() #Hello, Alice!

outer("Tom")() #Hello, Tom!