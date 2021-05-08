class Books(object):
    def __init__(self, book, title):
        self.books = []

    def add_book(self, author_name, book_title):
        self.books.append(tuple(author_name, book_title, False))

    def remove_book(self, author_name, book_title):
        self.books.remove(tuple(author_name, book_title))

    def loan_book(self, author_name, book_title):
        self.books[books.index(author_name, book_title, False)] = tuple(
            author_name, book_title, True)

    def return_book(self, author_name, book_title):
        self.books[books.index(author_name, book_title, True)] = tuple(
            author_name, book_title, False)

    def list_of_books(self):
        return self.books
