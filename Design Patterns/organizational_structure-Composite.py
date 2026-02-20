from abc import ABC, abstractmethod


class Organization(ABC):
    @abstractmethod
    def showDetails(self):
        pass

class LeafElement(Organization):
    def __init__(self, *args):
        if args:
            self.position = args[0]
        else:
            self.position = None

    def showDetails(self, indent=0):
        print("\t" * indent + f"{self.position}")


class CompositeElement(Organization):
    def __init__(self, *args):
        if args:
            self.position = args[0]
        else:
            self.position = None
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self, indent=0):
        print("\t" * indent + f"{self.position}")
        for child in self.children:
            child.showDetails(indent + 1)

head_office = CompositeElement("General Manager")


sales_dept = CompositeElement("Sales Manager")
dev_dept = CompositeElement("CTO")


sales_dept.add(LeafElement("Sales Rep A"))
sales_dept.add(LeafElement("Sales Rep B"))

dev_dept.add(LeafElement("Software Engineer"))


head_office.add(sales_dept)
head_office.add(dev_dept)

head_office.showDetails()