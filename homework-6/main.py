from src.item import Item
from path import ITEMS_PATH, ITEM_PATH

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(ITEM_PATH)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ITEMS_PATH)
    # InstantiateCSVError: Файл item.csv поврежден
