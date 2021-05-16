import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file library.py exists.
import os.path
if(os.path.isfile("library.py")==False):
	print("Error you need to call the Python file library.py!")

# Check that the class is called library. That is, the file library.py contains the expression "library(object):"
file_text = open('library.py', 'r').read()
if("library(object):" not in file_text):
	print("Error you need to call the Python class library!")


sys.excepthook = Pyro5.errors.excepthook
library = Proxy("PYRONAME:example.library")

library.add_author("James Joyce", "fiction")
library.add_book_copy("James Joyce", "Ulysses")
library.add_user("Maureen O Hara")
print(library.loan_book("Maureen O Hara", "Ulysses", 2019, 1, 3))
library.return_book("Maureen O Hara", "Ulysses", 2019, 2, 1)
library.delete_user("Maureen O Hara")
library.delete_book("Ulysses")
print(library.return_users())
print(library.return_authors())
print(library.return_books_not_loan())
print(library.return_books_loan())
print(library.user_loans_date("Maureen O Hara", 2010, 1, 1, 2029, 2, 1))