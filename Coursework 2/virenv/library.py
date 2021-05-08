from Pyro5.api import expose, behavior, serve, Daemon
# from book import Books
# from author import Authors
# from user import Users


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
        self.users.append(user_name)

    def return_users(self):
        return self.users
        # message = [user for user in Users.list_of_users()] if len(
        #     Users.list_of_users()) > 0 else 'No users'
        # return message

    def add_author(self, author_name, author_genre):
        self.authors.append((author_name, author_genre))
        print(self.authors)

    def return_authors(self):
        return self.authors
        # message = [author for author in Authors.list_of_authors()] if len(
        #     Authors.list_of_authors()) > 0 else 'No authors'
        # return message

    def add_book_copy(self, author_name, book_title):
        self.books.append((author_name, book_title, False))
        # Books.add_book(author_name, book_title)
        self.books_not_on_loan.append((author_name, book_title))

    def return_books_not_loan(self):
        message = [book for book in self.books_not_on_loan] if len(
            self.books_not_on_loan) > 0 else 'All books are loaned'
        return message

    def loan_book(self, user_name, book_title, year, month, day):
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) in self.books_not_on_loan:
            self.books_on_loan.append(
                (user_name, book_title, year, month, day))
            self.books[self.books.index((author[0], book_title, False))] = (
                author[0], book_title, True)
            self.books_not_on_loan.remove((author[0], book_title))
            self.current_loans.append((user_name, book_title, year, month, day))
            self.history_of_loans.append((user_name, book_title, year, month, day,'Loan'))
            return 1
        else:
            return 0

    def return_books_loan(self):
        message = [book for book in self.books_on_loan] if len(
            self.books_on_loan) > 0 else 'No books are loaned'
        return message

    def return_book(self, user_name, book_title, year, month, day):
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) in self.books_on_loan:
            self.books_not_on_loan.append(
                (user_name, book_title, year, month, day))
            self.books[self.books.index((author[0], book_title, True))] = (
            author[0], book_title, False)
            self.books_on_loan.remove(Book(author[0], book_title))
            return 1
        else:
            return 0

    def delete_book(self, book_title):
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) in self.books_not_on_loan:
            self.books_not_on_loan.remove((author[0], book_title))
            self.books.remove((author[0], book_title))

    def delete_user(self, user_name):
        current_loans = [loan for loan in self.current_loans if loan[0] == user_name]
        history_of_loans = [loan for loan in self.history_of_loans if loan[0] == user_name]

        if len(current_loans) == 0 and len(history_of_loans) == 0:
            self.users.remove(user_name)

    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        pass


daemon = Daemon()
serve({library: "example.library"}, daemon=daemon, use_ns=True)
