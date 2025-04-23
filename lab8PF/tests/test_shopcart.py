import pytest
from lab8PF.src.shopcart import Product, ShoppingCart

@pytest.fixture()
def sample_product():
    return Product(id=1, name="Apple",price= 100)

@pytest.fixture()
def decimal_product():
    return Product(id=2, name="Milk",price=9.99)

@pytest.fixture()
def empty_cart():
    return ShoppingCart()

@pytest.fixture()
def filled_card(empty_cart,decimal_product):
    for _ in range(5):
        empty_cart.add_product(decimal_product)
    return empty_cart



def test_adding(empty_cart,sample_product):
    empty_cart.add_product(sample_product)
    assert sample_product.id in empty_cart.products.keys()
    assert empty_cart.get_product_count() == 1

def test_adding_decimal_product(empty_cart,decimal_product):
    empty_cart.add_product(decimal_product, quantity= 8)
    assert empty_cart.get_product_count() == 8
    assert empty_cart.get_total_price() == 79.92

@pytest.mark.parametrize("quanlity", [1, 3, 5,10])
def test_multiple_adding(empty_cart,sample_product,quanlity):
    empty_cart.add_product(sample_product,quanlity)
    assert empty_cart.get_product_count() == quanlity

def test_removing_invalid(filled_card,sample_product):
    with pytest.raises(ValueError):
        filled_card.remove_product(sample_product.id)

def test_removing(filled_card,decimal_product):
    filled_card.remove_product(decimal_product.id)
    assert filled_card.get_product_count() == 4

def test_clear(filled_card,decimal_product):
    while(filled_card.get_product_count() > 0):
        filled_card.remove_product(decimal_product.id,5)

    assert filled_card.get_product_count() == 0