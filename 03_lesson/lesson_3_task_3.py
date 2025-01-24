from Address import Address
from Mailing import Mailing

to_address = Address(995742, 'Москва', 'Ленина', 35, 15)
from_address = Address(654121, 'Екатеринбург', 'Техническая', 2, 54)

mailing1 = Mailing(from_address, to_address, 2500, 'CA123456789UA')

print(mailing1)
