#Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords.
#Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.

class Employee:
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        names = full_name.split()
        self.name = names[0]
        self.lastname = names[1]

        for key, value in kwargs.items():
            setattr(self, key, value)


john = Employee("John Doe")
print(john.name) #John

mary = Employee("Mary Major", salary=120000)
print(mary.lastname) #Major

richard = Employee("Richard Roe", salary=110000, height=178)
print(richard.height) #178

giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(giancarlo.nationality) #Italian
