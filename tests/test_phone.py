from src.phone import Phone

phone3 = Phone("iPhone 14", 120_000, 5, 2)

def test_initial_phone(phone3):
    assert phone3.price == 120_000
    assert phone3.name == "iPhone 14"
    assert phone3.quantity == 5
    assert phone3.number_of_sim == 2

def test_repr(phone3):
    assert repr(phone3) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str(phone3):
    assert str(phone3) == 'iPhone 14'