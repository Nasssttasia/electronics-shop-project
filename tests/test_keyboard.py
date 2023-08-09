

def test_initial_keyboard(keyboard3):
    assert keyboard3.price == 120_000
    assert keyboard3.name == "iPhone 14"
    assert keyboard3.quantity == 5
    assert keyboard3.language == 'EN'

def test_language(keyboard3):
    keyboard3.change_lang()
    assert str(keyboard3.language) == "RU"
