#Define a class Employee. In the class Employee implement the instance attributes as firstname,
# lastname and salary. Create the static method from_string() which parses a string containing
# these attributes and assigns them to the correct properties. Properties will be separated by a dash.

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return f"{self.firstname}{self.lastname}{self.salary}"

    @staticmethod
    def from_string(emp_str):
        firstname, lastname, salary = emp_str.split('-')
        return Employee(firstname, lastname, int(salary))

emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname) #Mary
print(emp1.salary) #60000

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.lastname) #Smith
print(emp2.salary) #55000


