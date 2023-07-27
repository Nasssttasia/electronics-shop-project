import pytest
from src.item import Item

@pytest.fixture()
def item3():
    item3 = Item("Смартфон", 10000, 20)
    return item3
