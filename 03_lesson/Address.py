class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartament = apartment

    def __str__(self):
        return (f'{int(self.index)}, {self.city}, {self.street}, '
                f'{self.house} - {self.apartament}')
