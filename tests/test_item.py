from src.item import Item


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
