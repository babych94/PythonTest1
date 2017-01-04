from base import BasePage
from base import InvalidPageExeption

class HomePage(BasePage):

    _home_page_view_locator = ".//*[@id='root']/div/div[2]/div[2]/div/div/div[6]/div/div/div[3]/table/tbody/tr[1]/td[1]/a"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name \
                (self._home_page_slideshow_locator)
        except:
            raise InvalidPageExeption \
                ("Home Page not loaded")

