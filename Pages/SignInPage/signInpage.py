from abc import abstractmethod
from base import BasePage

class SignInPage(BasePage):
    _sign_in_page_locator = './/*[@id=\'root\']/div/div/div/form/div[1]/img'