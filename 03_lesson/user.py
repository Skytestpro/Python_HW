class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def first_n(self):
        print('Name:', self.first_name)

    def last_n(self):
        print('Last name:', self.last_name)

    def first_last(self):
        print('Full name:', self.first_name, self.last_name)
