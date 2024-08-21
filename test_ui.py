from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(4)
    yield browser
    browser.quit()


# Перейти на сайт «Читай-город» и добавить куки
cookie = {"name": "cookie_policy", "value": "1"}


@allure.title("Согласие на добавление куки")
@allure.description("Тест проверяет добавление куки,чтобы плашка не мешала обзору")
@allure.severity("Major")
def test_opensite_and_addcookie(browser):
    browser.get("https://www.chitai-gorod.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    with allure.step("Добавление куки"):
        browser.add_cookie(cookie)
    sleep(5)


@allure.title("Поиск книги на русском языке")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.severity("blocker")
def test_add_book(browser):
    browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Добавлены ожидания и открытие окна"):
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска книги"):
        browser.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys("Алые паруса")
        browser.find_element(By.CSS_SELECTOR, ".header-search__button").click()
    assert "Показываем результаты по запросу" in browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
