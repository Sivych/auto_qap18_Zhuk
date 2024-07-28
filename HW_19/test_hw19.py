import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


URL = 'https://www.bbc.com/news'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_find_BBC_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-49542412-10 jTsKD"]')


def test_find_BBC_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '//div[@class="sc-49542412-2 hrGuyi"]')


def test_find_signin_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-ec3ac5c8-2 sc-ec3ac5c8-5 eRCykh jKWpcL"]')


def test_find_signin_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '//button[@class="sc-ec3ac5c8-2 sc-ec3ac5c8-5 eRCykh jKWpcL"]')


def test_find_home_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class ="sc-f116bf72-4 yKcKi"]')


def test_find_home_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '//a[@class="sc-f116bf72-4 yKcKi"]')


def test_find_sport_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-3 cHJCBW"]:nth-child(3)')


def test_find_sport_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//li[@class="sc-f116bf72-3 cHJCBW"])[2]')


def test_find_innovation_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-3 cHJCBW"]:nth-child(5)')


def test_find_innovation_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//li[@class="sc-f116bf72-3 cHJCBW"])[4]')


def test_find_travel_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-3 cHJCBW"]:nth-child(7)')


def test_find_travel_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//li[@class="sc-f116bf72-3 cHJCBW"])[6]')


def test_find_video_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-3 kkeorx"]')


def test_find_video_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//li[@class="sc-f116bf72-3 kkeorx"])')


def test_find_menu_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[aria-label="Open menu"]:first-child')


def test_find_menu_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '//*[@aria-label="Open menu"]')


def test_text_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[data-testid="card-headline"]:nth-child(1)')


def test_text_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//h2[@data-testid="card-headline"])[2]')


def test_picture_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[data-testid="card-media"]:nth-child(1)')


def test_picture_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//div[@class ="sc-814e9212-1 fcEyBx"])[5]')


def test_updated_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[data-testid="card-metadata-lastupdated"]')


def test_updated_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '//span[@data-testid="card-metadata-lastupdated"]')


def test_features_analysis_css(driver):
    driver.get(URL)

    assert driver.find_element(By.CSS_SELECTOR, '[data-testid="virginia-title"]:nth-child(1)')


def test_features_analysis_xpath(driver):
    driver.get(URL)

    assert driver.find_element(By.XPATH, '(//h2[@class="sc-54d40974-2 eKfxoB"])[2]')
