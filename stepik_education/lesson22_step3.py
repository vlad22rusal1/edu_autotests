from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x1,y1):
  return x1 + y1

try:
    # link = "https://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(10)
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text

    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text

    z_ans = calc(int(x),int(y))


    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, f'[value="{z_ans}"]').click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{z_ans}")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    browser.implicitly_wait(10)



finally:
    time.sleep(5)
    browser.quit()