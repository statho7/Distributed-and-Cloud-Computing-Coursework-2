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

    def add_author(self, author_name, author_genre):
        self.authors.append((author_name, author_genre))

    def return_authors(self):
        return self.authors

    def add_book_copy(self, author_name, book_title):
        self.books.append((author_name, book_title, False))
        # Books.add_book(author_name, book_title)
        self.books_not_on_loan.append((author_name, book_title))
        print('add_book_copy')
        print(self.books_not_on_loan)
        print(len(self.books_not_on_loan))

    def return_books_not_loan(self):
        print('return_books_not_loan')
        print(self.books_not_on_loan)
        print(len(self.books_not_on_loan))
        message = [book for book in self.books_not_on_loan] if len(
            self.books_not_on_loan) > 0 else 'All books are loaned'
        return message

    def loan_book(self, user_name, book_title, year, month, day):
        print('loan_book')
        print(self.books_not_on_loan)
        print(len(self.books_not_on_loan))
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) not in self.current_loans:
            self.books_on_loan.append(
                (author[0], book_title))
            self.books[self.books.index((author[0], book_title, False))] = (
                author[0], book_title, True)
            self.books_not_on_loan.remove((author[0], book_title))
            self.current_loans.append(
                (author[0], book_title))
            self.history_of_loans.append(
                (user_name, book_title, year, month, day, 'Loan'))
            return 1
        else:
            return 0

    def return_books_loan(self):
        message = [book for book in self.books_on_loan] if len(
            self.books_on_loan) > 0 else 'No books are loaned'
        print('return_books_loan')
        print(self.books_not_on_loan)
        print(len(self.books_not_on_loan))
        return message

    def return_book(self, user_name, book_title, year, month, day):
        # print(self.current_loans)
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) in self.current_loans:
            self.books_not_on_loan.append(
                (author[0], book_title))
            self.books[self.books.index((author[0], book_title, True))] = (
                author[0], book_title, False)
            self.books_on_loan.remove((author[0], book_title))
            self.current_loans.remove(
                (author[0], book_title))
            self.history_of_loans.append(
                (user_name, book_title, year, month, day, 'Returned'))
            print('return_book')
            print(self.books_not_on_loan)
            print(len(self.books_not_on_loan))
            return 1
        else:
            print('return_book')
            print(self.books_not_on_loan)
            print(len(self.books_not_on_loan))
            return 0

    def delete_book(self, book_title):
        author = [book[0] for book in self.books if book[1] == book_title]
        if (author[0], book_title) in self.books_not_on_loan:
            self.books_not_on_loan.remove((author[0], book_title))
            self.books.remove((author[0], book_title, False))

    def delete_user(self, user_name):
        current_loans = [
            loan for loan in self.current_loans if loan[0] == user_name]
        history_of_loans = [
            loan for loan in self.history_of_loans if loan[0] == user_name]

        if len(current_loans) == 0 and len(history_of_loans) == 0:
            self.users.remove(user_name)

    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        loans_of_user = []
        for loan in self.history_of_loans:
            if loan[0] == user_name and loan[5] == 'Loan' and (loan[2] > start_year or (loan[2] == start_year and (loan[3] > start_month or (loan[3] == start_month and loan[4] > start_day)))):
                for second_loan in self.history_of_loans:
                    if second_loan[0] == user_name and second_loan[1] == loan[1] and second_loan[5] == 'Returned' and (second_loan[2] < end_year or (second_loan[2] == end_year and (second_loan[3] < end_month or (second_loan[3] == end_month and second_loan[4] < end_day)))):
                        loans_of_user.append(loan)
                        loans_of_user.append(second_loan)
        return loans_of_user if len(loans_of_user) > 0 else 'No loans between these dates'


daemon = Daemon()
serve({library: "example.library"}, daemon=daemon, use_ns=True)
