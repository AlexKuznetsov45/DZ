from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13 Pro Max", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22 Ultra", "+79212345678"),
    Smartphone("Xiaomi", "Mi 11 Ultra", "+79341234569"),
    Smartphone("Huawei", "P50 Pro", "+79451234560"),
    Smartphone("OnePlus", "9 Pro", "+79561234561"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
