"""Test the product list page of saucedemo.com"""
import logging
import pytest
import test_data.constants as const
import test_data.login_creds as lc
from source.pages.login_page import LoginPage
from source.pages.product_list_page import ProductListPage


@pytest.mark.parametrize(
    "username, password",
    [
        (lc.TEST_USER, lc.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.regression
def test_get_products(driver, username, password):
    """Test getting all product names from the PLP."""
    logging.info("Verifying that products shows on a product list page")
    lp = LoginPage(driver)
    lp.perform_complete_login(username, password)
    p_page = ProductListPage(driver)
    product_names = p_page.get_list_of_product_names()
    for name in product_names:
        logging.info(f"PLP has product with name: {name}")
    assert len(product_names) > 0, "No products found on the PLP."
    logging.info("Successfully verified that products are shown")


@pytest.mark.parametrize(
    "username, password",
    [
        (lc.TEST_USER, lc.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.product_sort
@pytest.mark.regression
def test_sort_low_to_high(driver, username, password):
    """Test sorting the PLP's products by price in ascending order."""
    logging.info("Verifying that user can sort products by price from low to high")
    lp = LoginPage(driver)
    lp.perform_complete_login(username, password)
    p_page = ProductListPage(driver)
    logging.info("Clicking on `Price(low to high)` button")
    p_page.sort_products_low_to_high()
    product_prices = p_page.get_list_of_product_prices()
    for i in range(len(product_prices)-1):
        assert product_prices[i] <= product_prices[i+1], \
            "Products {0} and {1} are not ordered correctly.".format(product_prices[i], product_prices[i+1])
    logging.info("Successfully verified that user can sort products by price from low to high")


@pytest.mark.parametrize(
    "username, password",
    [
        (lc.TEST_USER, lc.STANDARD_PASSWORD),
    ],
)
@pytest.mark.product_page
@pytest.mark.add_cart
@pytest.mark.regression
def test_add_to_cart(driver, username, password):
    """Test adding items to the cart."""
    logging.info("Verifying that user can add items to cart from PLP")
    lp = LoginPage(driver)
    lp.perform_complete_login(username, password)
    p_page = ProductListPage(driver)
    product_elements = p_page.get_all_product_elements()
    num_items_in_cart = 0
    assert p_page.get_number_cart_items() == num_items_in_cart, "An unexpected item has been found in the cart."

    # Add products, check mini cart total.
    logging.info("Adding item to to cart from PLP")
    for product in product_elements:
        add_cart_button = p_page.add_product_to_card(product)
        add_cart_button.click()
        num_items_in_cart += 1
        assert num_items_in_cart == p_page.get_number_cart_items(), "An unexpected item has been found in the cart."
        remove_cart_button = p_page.add_product_to_card(product)
        assert remove_cart_button.text == const.REMOVE
    logging.info(f"{num_items_in_cart} items were added to cart")

    # Remove products, check mini cart total.
    logging.info("Removing item to to cart from PLP")
    for product in product_elements:
        remove_cart_button = p_page.add_product_to_card(product)
        remove_cart_button.click()
        num_items_in_cart -= 1
        assert num_items_in_cart == p_page.get_number_cart_items(), "An unexpected item has been found in the cart."
        add_cart_button = p_page.add_product_to_card(product)
        assert add_cart_button.text == const.ADD_TO_CART
    logging.info(f"{num_items_in_cart} items in to cart after removal")

    logging.info("Successfully verified that user was able to add items to cart from PLP")
