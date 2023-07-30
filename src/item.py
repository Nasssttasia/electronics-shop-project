import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """возвращает name"""
        return self.__name

    @name.setter
    def name(self, user_input):
        if len(user_input) < 10:
            self.name = user_input
        else:
            self.name = user_input[0:9]

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, "r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                name, price, quantity = i['name'], float(i['price']), int(i['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
