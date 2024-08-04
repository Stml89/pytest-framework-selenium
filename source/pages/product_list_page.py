""" POM class for the Product page. """
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.pages.base import BasePage


class ProductListPage(BasePage):
    """ Product page class. """
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_item_count_selector = (By.CLASS_NAME, "shopping_cart_badge")
        self.inventory_item_name_selector = (By.CLASS_NAME, "inventory_item_name")
        self.inventory_item_price_selector = (By.CLASS_NAME, "inventory_item_price")
        self.inventory_item_selector = (By.CLASS_NAME, "inventory_item")
        self.sort_low_to_high_selector = (By.CSS_SELECTOR, "[value='lohi']")
        self.sort_menu_selector = (By.CLASS_NAME, "product_sort_container")
        self.add_to_card_button = (By.CLASS_NAME, "btn_inventory")

    def click_product_sort_menu(self):
        """ Click the product sort menu. """
        self.click_element(self.sort_menu_selector)

    def get_all_product_elements(self):
        """ Get the element of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_selector)
        return products

    def get_list_of_product_names(self):
        """ Get the name of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_name_selector)
        return [item.text for item in products]

    def get_number_cart_items(self):
        """ Get the number of items in the cart. """
        has_items_in_cart = len(self.driver.find_elements(*self.cart_item_count_selector)) > 0
        if has_items_in_cart:
            num_items_in_cart = self.driver.find_element(*self.cart_item_count_selector).text
            return int(num_items_in_cart)
        else:
            return 0

    def get_list_of_product_prices(self):
        """ Get the price of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_item_price_selector)
        return [float(item.text.replace("$", "")) for item in products]

    def sort_products_low_to_high(self):
        """ Sort products low to high. """
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_low_to_high_selector)
        )
        sort_option.click()

    def add_product_to_card(self, product_card):
        """ Add products to card. """
        button = product_card.find_element(*self.add_to_card_button)
        return button
