from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from support.logging import logger


class HeaderPage(Page):


    CAFEDARIA_TITLE = (By.CSS_SELECTOR, 'div.rd-navbar-brand')
    NAV_SUBTITLES_LINKS = (By.CSS_SELECTOR, 'a.rd-nav-link')
    CART_ICON = (By.CSS_SELECTOR, 'a.icon.icon-sm.mdi.mdi-cart-outline')
    SEARCH_ICON =(By.CSS_SELECTOR, 'div.rd-navbar-search.toggle-original-elements')

    def verify_title_cafedaria_exists_on_nav_bar(self):
        self.find_element(*self.CAFEDARIA_TITLE)

    def verify_subtitles_are_in_nav_bar_and_are_clickable(self, expected_amount):
        expected_amount = int(expected_amount)
        sub_titles = self.find_elements(*self.NAV_SUBTITLES_LINKS)
        assert len(sub_titles) == expected_amount,\
            f'Expected {expected_amount} but got {len(sub_titles)}'

        for subtitle in sub_titles:
            assert subtitle.is_enabled(), f'Subtitle {subtitle.text} is not clickable'

    def verify_the_cart_and_search_icons_exist(self):
        self.find_element(*self.CART_ICON)
        self.find_element(*self.SEARCH_ICON)














