from src.item import Item
from src.phone import Phone


def test_calculate_total_price(item3):
    assert item3.calculate_total_price() == 200000


def test_apply_discount(item3):
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.calculate_total_price() == 160000


def test_initial_item(item3):
    assert item3.price == 10000
    assert item3.name == "Смартфон"
    assert item3.quantity == 20

def test_string_to_number(item3):
    assert Item.string_to_number('5') == 5

def test_repr(item3):
    assert repr(item3) == "Item('Смартфон', 10000, 20)"

def test_str(item3):
    assert str(item3) == 'Смартфон'

def test_add(item3):
    phone3 = Phone("iPhone 14", 120_000, 5, 2)
    assert item3.quantity + phone3.quantity == 25
