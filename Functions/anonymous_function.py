#Create function create with one string argument. This function should return anonymous function
#that checks if the argument of function is equals to the argument of outer function.

def create(str):
    return lambda x: x == str


tom = create("pass_for_Tom")
print(tom("pass_for_Tom")) #True
print(tom("12345")) #False