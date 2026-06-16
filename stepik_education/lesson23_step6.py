from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    btn = browser.find_element(By.CSS_SELECTOR, '.container > .trollface.btn')
    btn.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x_value = browser.find_element(By.ID, 'input_value').text
    x = calc(x_value)

    ans = browser.find_element(By.ID, 'answer')
    ans.send_keys(x)

    btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    btn.click()




finally:
    time.sleep(10)
    browser.quit()