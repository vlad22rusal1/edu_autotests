from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


try:
    link = "https://stepik.org/lesson/236895/step/1"
    def math_answer_get():
        answer = math.log(int(time.time()))
        return answer


    @pytest.mark.parametrize('idishnik', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_open_stepik(browser,idishnik):
        link = f"https://stepik.org/lesson/{idishnik}/step/1"
        browser.get(link)
        browser.find_element(By.CLASS_NAME, "navbar__auth.navbar__auth_login").click()
        browser.find_element(By.ID, 'id_login_email').send_keys("")
        browser.find_element(By.ID, 'id_login_password').send_keys("")
        browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
        time.sleep(10)
        browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea").send_keys(math_answer_get())
        browser.find_element(By.CLASS_NAME, "attempt-wrapper-buttons__button").click()
        time.sleep(10)
        text_f = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")

        text_found = text_f.text
        if (text_found == "Correct!"):
            assert True
        else:
            print(text_found)
finally:
    time.sleep(5)

