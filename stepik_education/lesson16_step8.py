from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    fname = browser.find_element(By.TAG_NAME, 'input')
    fname.send_keys("Ivan")
    lname = browser.find_element(By.NAME, 'last_name')
    lname.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла