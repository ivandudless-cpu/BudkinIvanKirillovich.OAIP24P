import json

# Таблица 1: Школьники
table_1 = [
    {"id": 1, "name": "Azumi", "surname": "Morimoto", "class": 2, "age": 14, "subject": "Biology"},
    {"id": 2, "name": "Emiko", "surname": "Yamomoto", "class": 1, "age": 14, "subject": "Art"},
    {"id": 3, "name": "Minako", "surname": "Kavaguti", "class": 1, "age": 13, "subject": "Mathematics"}
]

# Таблица 2: Танки
table_2 = [
    {"id": 1, "TankName": "T-150", "TankClass": "Heavy Tank", "TankLevel": "VI"},
    {"id": 2, "TankName": "VK 16.01 Leopard", "TankClass": "Light Tank", "TankLevel": "V"},
    {"id": 3, "TankName": "Matilda", "TankClass": "Medium Tank", "TankLevel": "IV"}
]

# Таблица 3: Автомобили
table_3 = [
    {"id": 1, "CarSign": "Nissan", "CarModel": "Skyline GT-R R34", "StockClass": "C"},
    {"id": 2, "CarSign": "Honda", "CarModel": "Civic Si (CX)", "StockClass": "E"},
    {"id": 3, "CarSign": "Dodge", "CarModel": "Charger R/T (69)", "StockClass": "D"}
]


with open("students.json", "w", encoding="utf-8") as f:
    json.dump(table_1, f, ensure_ascii=False, indent=2)

with open("tanks.json", "w", encoding="utf-8") as f:
    json.dump(table_2, f, ensure_ascii=False, indent=2)

with open("cars.json", "w", encoding="utf-8") as f:
    json.dump(table_3, f, ensure_ascii=False, indent=2)