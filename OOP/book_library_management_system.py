#Develop a book library management system using object-oriented programming (OOP) in Python.
# Implement classes for books, the library, customers, and the library management system.
# Consider the quantity of each book in the library.


class Book:

    def __init__(self, title, author, year, quantity=1):
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def display_info(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}'

    def __str__(self):
        return self.display_info()


class  EBook(Book):

    def __init__(self, title, author, year, format_type, quantity=1):
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity} Format: {self.format_type}'

    def __str__(self):
        return self.display_info()


class Library:

    def __init__(self):
        self.books = []
        self.book_count = 0

    def add_book(self, new_book):
        self.books.append(new_book)
        self.book_count += 1

    def display_books(self):
        for book in self.books:
            print(book.display_info())


class Customer:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} borrowed books:{self.borrowed_books}"

    def borrow_book(self, book):
        if book.quantity > 0:
            book.quantity -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.quantity += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class LibraryManagementSystem:

    def __init__(self):
        self.library  = Library()
        self.customers = []

    def register_customer(self, new_customer):
        self.customers.append(new_customer)
        print(f"Customer {new_customer.name} registered in the system.")

    def display_customer_books(self, customer):
        print(f"Books borrowed by {customer.name}:")
        for book in customer.borrowed_books:
            print(book.display_info())

    def display_all_books(self):
        print("Books in the Library:")
        self.library.display_books()


book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")
customer1 = Customer("Alice")
customer2 = Customer("Bob")
library_system = LibraryManagementSystem()
library_system.register_customer(customer1) #Customer Alice registered in the system.
library_system.register_customer(customer2) #Customer Bob registered in the system.
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)
customer1.borrow_book(book1) #Alice borrowed 'The Catcher in the Rye'.
customer1.borrow_book(ebook1) #Alice borrowed 'Python Crash Course'.
customer2.borrow_book(book2) #Bob borrowed 'To Kill a Mockingbird'.
customer1.return_book(book1) #Alice returned 'The Catcher in the Rye'.
customer2.return_book(book1) #Bob did not borrow 'The Catcher in the Rye'.
library_system.display_customer_books(customer1) #Books borrowed by Alice:
                                                #Title: Python Crash Course, Author: Eric Matthes, Year: 2015, Quantity: 0 Format: PDF
library_system.display_all_books() #Books in the Library:
                                    #Title: The Catcher in the Rye, Author: J.D. Salinger, Year: 1951, Quantity: 1
                                    #Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960, Quantity: 0
                                    #Title: Python Crash Course, Author: Eric Matthes, Year: 2015, Quantity: 0 Format: PDF
                                    #Title: Dive into Python 3, Author: Mark Pilgrim, Year: 2009, Quantity: 1 Format: EPUB
