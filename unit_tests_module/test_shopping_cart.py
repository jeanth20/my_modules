from unittest.mock import Mock
from item_database import ItemDatabase
from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(max_size=5)


def test_can_add_item_to_cart(cart):
    cart.add("bananas")
    assert cart.size() == 1

def test_when_item_added_then_cart_has_item(cart):
    cart.add("bananas")
    assert "bananas" in cart.get_items()
    
def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("bananas")
    with pytest.raises(OverflowError):
        cart.add("bananas")

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("bananas")

    price_map = {
        "apple": 1.0,
        "bananas": 2.0
    }
    assert cart.get_total_price(price_map) == 3.0

def test2_can_get_total_price(cart):
    cart.add("apple")
    cart.add("bananas")
    item_database = ItemDatabase()
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "bananas":
            return 2.0
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0