import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    fname = browser.find_element(By.NAME, 'firstname')
    fname.send_keys("Vlad")

    lname = browser.find_element(By.NAME, 'lastname')
    lname.send_keys("Voy")

    email = browser.find_element(By.NAME, 'email')
    email.send_keys("mail@mail.ru")

    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()