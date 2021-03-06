from Pyro5.api import expose, behavior, serve, Daemon
from book import Book
from author import Author
from user import User


@expose
@behavior(instance_mode="single")
class library(object):
    def __init__(self):
        self.authors = []
        self.books = []
        self.books_on_loan = []
        self.books_not_on_loan = []
        self.users = []
        self.current_loans = []
        self.history_of_loans = []

    def add_user(self, user_name):
        user = User(user_name)
        self.users.append(user.user_name)

    def return_users(self):
        return self.users

    def add_author(self, author_name, author_genre):
        author = Author(author_name, author_genre)
        self.authors.append(
            (author.author_name, author.author_genre))

    def return_authors(self):
        return self.authors

    def add_book_copy(self, author_name, book_title):
        book = Book(author_name, book_title)
        self.books.append(
            (book.author_name, book.book_title, False))
        self.books_not_on_loan.append(
            (book.author_name, book.book_title))

    def return_books_not_loan(self):
        message = [book for book in self.books_not_on_loan] if len(
            self.books_not_on_loan) > 0 else 'All books are loaned'
        return message

    def loan_book(self, user_name, book_title, year, month, day):
        author = [book[0] for book in self.books if book[1] == book_title]
        if len(author) == 0:
            return f'No book with title "{book_title}" in the database'
        book = Book(author[0], book_title)
        user = User(user_name)
        if (book.author_name, book.book_title) in self.books_not_on_loan:
            self.books_on_loan.append(
                (book.author_name, book.book_title))
            self.books[self.books.index((author[0], book_title, False))] = (
                author[0], book.book_title, True)
            self.books_not_on_loan.remove(
                (book.author_name, book.book_title))
            self.current_loans.append(
                (user.user_name, book.author_name, book.book_title))
            self.history_of_loans.append(
                (user.user_name, book.book_title, year, month, day, 'Loan'))
            return 1
        else:
            return 0

    def return_books_loan(self):
        message = [book for book in self.books_on_loan] if len(
            self.books_on_loan) > 0 else 'No books are loaned'
        return message

    def return_book(self, user_name, book_title, year, month, day):
        author = [book[0] for book in self.books if book[1] == book_title]
        if len(author) == 0:
            return f'No book with title "{book_title}" in the database'
        book = Book(author[0], book_title)
        user = User(user_name)
        if (book.author_name, book.book_title) in self.books_on_loan:
            self.books_not_on_loan.append(
                (book.author_name, book.book_title))
            self.books[self.books.index((author[0], book_title, True))] = (
                author[0], book.book_title, False)
            self.books_on_loan.remove(
                (book.author_name, book.book_title))
            self.current_loans.remove(
                (user.user_name, book.author_name, book.book_title))
            self.history_of_loans.append(
                (user.user_name, book.book_title, year, month, day, 'Returned'))
            return 1
        else:
            return 0

    def delete_book(self, book_title):
        author = [book[0] for book in self.books if book[1] == book_title]
        if len(author) == 0:
            return f'No book with title "{book_title}" in the database'
        book = Book(author[0], book_title)
        if (book.author_name, book.book_title) in self.books_not_on_loan:
            self.books_not_on_loan.remove(
                (book.author_name, book.book_title))
            self.books.remove(
                (author[0], book.book_title, False))

    def delete_user(self, user_name):
        if user_name not in self.users:
            return f'No user with name "{user_name}" in the database'
        current_loans = [
            loan for loan in self.current_loans if loan[0] == user_name]
        history_of_loans = [
            loan for loan in self.history_of_loans if loan[0] == user_name]

        if len(current_loans) == 0 and len(history_of_loans) == 0:
            self.users.remove(user_name)

    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        if user_name not in self.users:
            return f'No user with name "{user_name}" in the database'
        loans_of_user = []
        for loan in self.history_of_loans:
            if loan[0] == user_name and loan[5] == 'Loan' and (loan[2] > start_year or (loan[2] == start_year and (loan[3] > start_month or (loan[3] == start_month and loan[4] > start_day)))):
                for second_loan in self.history_of_loans:
                    if second_loan[0] == user_name and second_loan[1] == loan[1] and second_loan[5] == 'Returned' and (second_loan[2] < end_year or (second_loan[2] == end_year and (second_loan[3] < end_month or (second_loan[3] == end_month and second_loan[4] < end_day)))):
                        loans_of_user.append(loan)
                        loans_of_user.append(second_loan)
        return loans_of_user if len(loans_of_user) > 0 else f'No loans between these dates for user: "{user_name}"'


daemon = Daemon()
serve({library: "example.library"}, daemon=daemon, use_ns=True)
