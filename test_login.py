from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

users = ['user1@mail.ru','user2@mail.ru','user3@mail.ru']
passws = ['qweqweqwe','adsda', 'axasdxas']

def generate_pairs():
    pairs = []
    for user in users:
       for passw in passws:
           pairs.append(pytest.param((user,passw),id=f'{user},{passw}'))
    return pairs


# @pytest.mark.parametrize(
#     'creds',
#     [
#         pytest.param(('user1@mail.ru', 'qweqweqwe'), id='user1@mail.ru, qweqweqwe'),
#         pytest.param(('user2@mail.ru', 'adsda'), id='user2@mail.ru, adsda'),
#         pytest.param(('user3@mail.ru', 'axasdxas'), id='user3@mail.ru, axasdxas')
#     ]
# )

@pytest.mark.skip
@pytest.mark.parametrize('creds', generate_pairs())
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

@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'jury':
        driver.get('https://idea.ru/jury')
    elif param == 'works':
        driver.get('https://idea.ru/works')
    return driver

@pytest.mark.parametrize('page',['jury'], indirect=True)
def test_jury(page):
    title = page.find_element(By.CSS_SELECTOR, '[class="Heading-module-scss-module__RCmfiq__Root Heading-module-scss-module__RCmfiq__As_h2 PageHeroHeading-module-scss-module__qqey5q__Title"]')
    assert title.text == "ЖЮРИ"

@pytest.mark.parametrize('page',['works'], indirect=True)
def test_works(page):
    title = page.find_element(By.CSS_SELECTOR, '[class="Heading-module-scss-module__RCmfiq__Root Heading-module-scss-module__RCmfiq__As_h2 PageHeroHeading-module-scss-module__qqey5q__Title"]')
    assert title.text == "РАБОТЫ"