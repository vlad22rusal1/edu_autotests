from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # link = "https://suninjuly.github.io/selects1.html"
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text


    answer = browser.find_element(By.ID,'answer')
    answer.send_keys(calc(x))

    check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    check.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()
    button.click()


finally:
    time.sleep(5)
    browser.quit()