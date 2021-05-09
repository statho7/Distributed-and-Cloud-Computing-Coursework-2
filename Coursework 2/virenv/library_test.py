import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file library.py exists.
import os.path

if(os.path.isfile("library.py") == False):
    print("Error you need to call the Python file library.py!")

# Check that the class is called library. That is, the file library.py contains the expression "library(object):"
file_text = open('library.py', 'r').read()
if("library(object):" not in file_text):
    print("Error you need to call the Python class library!")


sys.excepthook = Pyro5.errors.excepthook
library = Proxy("PYRONAME:example.library")

print('\nadd_author\n')
library.add_author("Omiros", "history")

print('\nadd_book_copy\n')
library.add_book_copy("Omiros", "Iliada")

print('\nadd_user\n')
library.add_user("Andreas")

print('\nadd_author\n')
library.add_author("Omiros", "history")

print('\nadd_book_copy\n')
library.add_book_copy("Omiros", "Odisia")

print('\nloan_book\n')
print(library.loan_book("Andreas", "Odisia", 2019, 1, 3))

print('\nadd_author\n')
library.add_author("Elitis", "poetry")

print('\nadd_book_copy\n')
library.add_book_copy("Elitis", "Aeriko")

print('\nprint(library.return_books_not_loan())\n')
print(library.return_books_not_loan())

print('\nadd_user\n')
library.add_user("Nikos")

print('\nloan_book\n')
print(library.loan_book("Nikos", "Aeriko", 2019, 1, 3))

print('\nadd_user\n')
library.add_user("Dimitris")

print('\nadd_book_copy\n')
library.add_book_copy("Elitis", "Aeriko")

print('\nprint(library.return_books_not_loan())\n')
print(library.return_books_not_loan())

print('\nloan_book\n')
print(library.loan_book("Andreas", "Aeriko", 2019, 2, 3))

print('\nprint(library.return_books_loan())\n')
print(library.return_books_loan())

print('\nprint(library.return_books_not_loan())\n')
print(library.return_books_not_loan())

print('\nreturn_book\n')
library.return_book("Andreas", "Aeriko", 2021, 2, 1)

print('\nadd_book_copy\n')
library.add_book_copy("Omiros", "Odisia")

print('\nprint(library.return_books_not_loan())\n')
print(library.return_books_not_loan())

print('\ndelete_user\n')
library.delete_user("Dimitris")

print('\nreturn_book\n')
library.return_book("Andreas", "Odisia", 2022, 2, 1)

print('\ndelete_book\n')
library.delete_book("Odisia")

print('\nuser_loans_date\n')
print(library.user_loans_date("Andreas", 2010, 1, 1, 2029, 2, 1))

print('\nreturn_book\n')
print(library.return_book("Nikos", "Aeriko", 2022, 1, 3))

print('\nuser_loans_date\n')
print(library.user_loans_date("Dimitris", 2010, 1, 1, 2029, 2, 1))

print('\nuser_loans_date\n')
print(library.user_loans_date("Nikos", 2010, 1, 1, 2029, 2, 1))




















# library.add_author("James Joyce", "fiction")

# library.add_book_copy("James Joyce", "Ulysses")

# print('\nprint(library.return_books_not_loan())\n')

# print(library.return_books_not_loan())

# library.add_user("Maureen O Hara")

# print('\nprint(library.loan_book("Maureen O Hara", "Ulysses", 2019, 1, 3))\n')

# print(library.loan_book("Maureen O Hara", "Ulysses", 2019, 1, 3))

# print('\nprint(library.return_books_loan())\n')

# print(library.return_books_loan())

# library.return_book("Maureen O Hara", "Ulysses", 2019, 2, 1)

# library.delete_user("Maureen O Hara")

# library.delete_book("Ulysses")

# print('\nprint(library.return_users())\n')

# print(library.return_users())

# print('\nprint(library.return_authors())\n')

# print(library.return_authors())

# print('\nprint(library.return_books_not_loan())\n')

# print(library.return_books_not_loan())

# print('\nprint(library.return_books_loan())\n')

# print(library.return_books_loan())

# print('\nprint(library.user_loans_date("Maureen O Hara", 2010, 1, 1, 2029, 2, 1))\n')

# print(library.user_loans_date("Maureen O Hara", 2010, 1, 1, 2029, 2, 1))
