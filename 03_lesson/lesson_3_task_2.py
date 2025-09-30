from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+77081286475"),
    Smartphone("Xiaomi", "14T", "+77081286318"),
    Smartphone("Samsung", "Galaxy a16", "+77016548742"),
    Smartphone("Nokia", "3000-3999", "+77011435486"),
    Smartphone("Honor", "Magic V", "+77083415785")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")
