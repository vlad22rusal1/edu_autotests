from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.button_simple import SimpleButtonPage

def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.button_click()
    assert "Submitted" == simple_page.result_text()