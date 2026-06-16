from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(10)
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")
    # x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    ans = browser.find_element(By.ID, 'answer')
    ans.send_keys(y)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    r_button = browser.find_element(By.ID, 'robotsRule')
    r_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    browser.implicitly_wait(10)



finally:
    time.sleep(5)
    browser.quit()