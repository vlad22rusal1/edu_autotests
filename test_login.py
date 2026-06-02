from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

users = ['user1@mail.ru','user2@mail.ru','user3@mail.ru']
passws = ['qweqweqwe','adsda', 'axasdxas']

def generate_pairs():
    for


@pytest.mark.parametrize(
    'creds',
    [
        pytest.param(('user1@mail.ru', 'qweqweqwe'), id='user1@mail.ru, qweqweqwe'),
        pytest.param(('user2@mail.ru', 'adsda'), id='user2@mail.ru, adsda'),
        pytest.param(('user3@mail.ru', 'axasdxas'), id='user3@mail.ru, axasdxas')
    ]
)
def test_login(creds):
    login, password = creds
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://account.idea.ru/login')
    driver.find_element(By.ID, 'form.email').send_keys(login)
    driver.find_element(By.ID, 'form.password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '[x-data="filamentFormButton"]').click()
    error_text = driver.find_element(By.CLASS_NAME, 'fi-fo-field-wrp-error-message').text
    assert error_text == "Неверное имя пользователя или пароль."
    driver.close()