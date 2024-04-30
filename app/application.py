from pages.main_page import MainPage
from pages.header_page import HeaderPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header_page = HeaderPage(driver)


