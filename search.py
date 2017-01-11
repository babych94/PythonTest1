from base import  BasePage
from base import InvalidPageExeption
from product import ProductPage

class SearchRegion(BasePage):
    _search_box_locator = 'q'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)

class SearchResults(BasePage):
    _product_list_locator = 'ul.products-grid > li'
    _product_name_locator = 'h2.product-name a'
    _product_image_link = 'a.product-image'
    _page_title_locator = 'div.page-title'


    _products_count = 0
    _products = {}

    def __init__(self, drver):
        super(SearchResults, self).__init__(self, drver)
        results = self.driver.find_element_by_css_selector(self._product_name_locator).text
        self._products[name] = product.find_element_by