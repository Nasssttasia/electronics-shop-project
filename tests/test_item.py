import pytest

from src.item import Item


def test_calculate_total_price(item3):
    assert item3.calculate_total_price() == 200000


def test_apply_discount(item3):
    Item.pay_rate = 0.8
    assert item3.price == 10000
