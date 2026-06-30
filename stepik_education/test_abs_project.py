# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class > input')
        fname.send_keys("Vlad")

        sname = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class > input')
        sname.send_keys("Voy")

        mail = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class > input')
        mail.send_keys("Voy@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.implicitly_wait(10)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")

        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class > input')
        fname.send_keys("Vlad")

        sname = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class > input')
        sname.send_keys("Voy")

        mail = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class > input')
        mail.send_keys("Voy@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.implicitly_wait(10)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be absolute value of a number")

        browser.quit()



if __name__ == "__main__":
    unittest.main()


