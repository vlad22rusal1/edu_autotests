from selenium.webdriver.common.by import By
import pytest
import time

try:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_open_stepik(browser):

        browser.get(link)
        buttonDis = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-add-to-basket")
        time.sleep(10)
        assert buttonDis.is_displayed(), \
            "Add to basket button is not displayed"
finally:
    time.sleep(5)

