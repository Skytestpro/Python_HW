from smartphone import Smartphone

catalog = [Smartphone('Xiaomi', '14T Pro', '7 999 999 99 99'),
           Smartphone('Honor', 'X7c', '7 999 999 99 00'),
           Smartphone('Samsung', 'S24 5G', '7 999 999 00 00'),
           Smartphone('Apple', 'iPhone 15 Pro', '7 999 900 00 00'),
           Smartphone('Infinix', 'GT 20 Pro', '7 999 000 00 00')]

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
