from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from support.logging import logger


class MainPage(Page):


    FOOTER_SEC = (By.CSS_SELECTOR, 'footer.page-footer')
    FOOTER_TITLE = (By.CSS_SELECTOR, 'div.col-md-6.col-xl-3 img.brand-logo-light')
    FOOTER_MAP = (By.CSS_SELECTOR, 'div.gm-style-moc')


    def open_the_main_page(self):
        self.open_url()
        sleep(2)


    def scroll_down_to_footer(self):
        actions = ActionChains(self.driver)
        footer = self.find_element(*self.FOOTER_SEC)
        actions.move_to_element(footer)
        actions.perform()


    def verify_the_title_cafedaria_in_footer_exists(self):
        self.find_element(*self.FOOTER_TITLE)


    def verify_the_footer_contains_a_map(self):
        self.find_element(*self.FOOTER_MAP)




