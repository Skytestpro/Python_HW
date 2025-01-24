from smartphone import Smartphone

catalog = [Smartphone('Xiaomi', '14T Pro', '+79999999999'),
           Smartphone('Honor', 'X7c', '+79999999900'),
           Smartphone('Samsung', 'S24 5G', '+79999990000'),
           Smartphone('Apple', 'iPhone 15 Pro', '+79999000000'),
           Smartphone('Infinix', 'GT 20 Pro', '+79990000000')]

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
