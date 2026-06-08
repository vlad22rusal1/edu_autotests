from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.button_like import LikeButtonPage

def test_button1_exist2(browser):
    like_page = LikeButtonPage(browser)
    like_page.open()
    assert like_page.button_is_displayed()

def test_button1_clicked2(browser):
    like_page = LikeButtonPage(browser)
    like_page.open()
    like_page.button_click()
    assert "Submitted" == like_page.result_text()