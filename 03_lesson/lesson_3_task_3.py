from mailing import Mailing
from address import Address

sender_address = Address(
    index="123456", city="Пенза", street="Проспект Победы", house="101", apartment="45"
)
receiver_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="99",
    apartment="12",
)

mailing = Mailing(
    to_address=receiver_address,
    from_address=sender_address,
    cost=500,
    track="ABCD-1234",
)
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
