from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('http://desktop-ng-test.fastlaneams.com/')
assert 'FastLane' in browser.title

email = browser.find_element_by_name('email')
email.clear()
email.send_keys('qa.test133@gmail.com' + Keys.RETURN)

password = browser.find_element_by_name('password')
password.clear()
password.send_keys('123456' + Keys.RETURN)

signIn = browser.find_element_by_xpath("//button[@type='submit']")
signIn.click()

#browser.implicitly_wait(10)

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//table/tbody/tr/td/a"))
    )
finally:

    view_buttons = browser.find_elements_by_xpath(".//table/tbody/tr/td/a")
    print('Number of VIEW buttons is', view_buttons.__len__())
    view_buttons[0].click()

#browser.quit()