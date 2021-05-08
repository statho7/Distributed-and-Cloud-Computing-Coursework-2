class Users(object):
    def __init__(self):
        self.users = []
        self.current_loans = []
        self.history_of_loans = []

    def add_user(self, user_name):
        self.users.append(user_name)

    def remove_user(self, user_name):
        self.users.remove(user_name)

    def add_loan(self, user_name, book_title, year, month, day):
        self.current_loans.append(tuple(user_name, book_title, year, month, day))
        self.history_of_loans.append(tuple(user_name, book_title, year, month, day,'Loan'))

    def remove_loan(self, user_name, book_title, year, month, day):
        self.current_loans.remove(tuple(user_name, book_title, year, month, day))
        self.history_of_loans.append(tuple(user_name, book_title, year, month, day, 'Return'))

    def list_of_users(self):
        return self.users

    def list_of_current_loans(self):
        current_loans_of_user = [loan for loan in current_loans if loan[0] == user_name]
        return current_loans_of_user

    def history_of_loans(self, user_name):
        history_of_user = [loan for loan in history_of_loans if loan[0] == user_name]
        return history_of_user
