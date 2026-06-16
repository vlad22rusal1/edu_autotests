from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fname = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class > input')
    fname.send_keys("Vlad")

    sname = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class > input')
    sname.send_keys("Voy")

    mail = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class > input')
    mail.send_keys("Voy@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    browser.implicitly_wait(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()