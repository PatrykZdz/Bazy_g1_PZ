import pytest
from lab8PF.src.discount import calculate_discounted_price
class TestDiscount:

    def test_correct_discount(self):
        assert calculate_discounted_price(100,30) == 70

    def test_rounding(self):
        assert calculate_discounted_price(100,33.3333) == 66.67

    def test_invalid_discount(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(455, "A")

    def test_negative_price(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(-4,23)

