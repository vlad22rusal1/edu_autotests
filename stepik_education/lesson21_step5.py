from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(10)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    ans = browser.find_element(By.ID, 'answer')
    ans.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    check.click()

    r_button = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    r_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    browser.implicitly_wait(10)



finally:
    time.sleep(5)
    browser.quit()