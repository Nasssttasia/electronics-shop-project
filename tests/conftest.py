import pytest
from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


@pytest.fixture()
def item3():
    item3 = Item("Смартфон", 10000, 20)
    return item3

@pytest.fixture()
def phone3():
    phone3 = Phone("iPhone 14", 120_000, 5, 2)
    return phone3

@pytest.fixture()
def keyboard3():
    keyboard3 = Keyboard("iPhone 14", 120_000, 5)
    return keyboard3
