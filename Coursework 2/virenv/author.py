class Authors(object):
    def __init__(self, name, genre):
        self.authors = []

    def add_author(self, author_name, author_genre):
        self.authors.append(tuple(author_name, author_genre))

    def remove_author(self, author_name):
        self.authors.remove(tuple(author_name, author_genre))

    def add_loan():
        self.loans.append(author_name)

    def remove_loan():
        self.loans.remove(author_name)

    def list_of_authors(self):
        return self.authors