import pytest

def calculate_price(price, discount):
    new_price = price - (price * discount / 100)
    return f"Yangi narx: {new_price:.0f} so‘m (Chegirma: {discount}%)"

def test_calculate_price():
    assert calculate_price(1000, 10) == "Yangi narx: 900 so‘m (Chegirma: 10%)"

def test_calculate_price_zero_discount():
    assert calculate_price(1000, 0) == "Yangi narx: 1000 so‘m (Chegirma: 0%)"

def test_calculate_price_hundred_discount():
    assert calculate_price(1000, 100) == "Yangi narx: 0 so‘m (Chegirma: 100%)"

def test_calculate_price_negative_price():
    with pytest.raises(ValueError):
        calculate_price(-1000, 10)

def test_calculate_price_negative_discount():
    with pytest.raises(ValueError):
        calculate_price(1000, -10)

def test_calculate_price_non_numeric_price():
    with pytest.raises(TypeError):
        calculate_price("1000", 10)

def test_calculate_price_non_numeric_discount():
    with pytest.raises(TypeError):
        calculate_price(1000, "10")
