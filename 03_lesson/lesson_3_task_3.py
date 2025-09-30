from address import Address
from mailing import Mailing

address1 = Address("101500", "Москва", "Ленинградская", "60", "5")
address2 = Address("101600", "Санкт-Петербург", "Вольная", "63", "25")

mailing1 = Mailing(address1, address2, "1000", "номер 1")

print(mailing1)
