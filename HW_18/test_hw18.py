import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""
Написать 5 автотестов по примеру ниже, 
на выбранного вами сайта 
либо на https://candymapper.com/ 
(https://candymapperr2.com/ исправленный сайт)

1. Открыть сайт http://thedemosite.co.uk/login.php
2. Ввести имя в поле username
3. Ввести пароль в поле password
4. Нажать на кнопку Test Login
5. Проверить, что Successful Login отображаются
"""

URL = 'https://candymapperr2.com/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_open(driver):
    driver.get(URL)

    close_element = driver.find_element(By.CSS_SELECTOR, '[id="popup-widget7437-close-icon"]')
    close_element.click()
    time.sleep(2)


def test_write_login_password(driver):
    driver.get(URL + 'm/login')

    close_element = driver.find_element(By.CSS_SELECTOR, '[id="popup-widget7833-close-icon"]')
    close_element.click()

    write_login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    write_login.send_keys('sivych26@mail.ru')
    write_password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    write_password.send_keys('AdminPass123')

    button_sign_in = driver.find_element(By.XPATH, '//button[@data-ux-btn="primary"]')
    button_sign_in.click()

    time.sleep(5)


def test_invalid_email(driver):
    driver.get(URL + 'm/login')

    close_element = driver.find_element(By.CSS_SELECTOR, '[id="popup-widget7833-close-icon"]')
    close_element.click()

    write_login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    write_login.send_keys('Kristina')
    write_password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    write_password.send_keys('AdminPass123')

    button_sign_in = driver.find_element(By.XPATH, '//button[@data-ux-btn="primary"]')
    button_sign_in.click()

    message = driver.find_element(By.XPATH, '//p[@data-aid="MEMBERSHIP_SSO_ERR_REND"]')
    assert message

    time.sleep(2)


def test_invalid_password(driver):
    driver.get(URL + 'm/login')

    close_element = driver.find_element(By.CSS_SELECTOR, '[id="popup-widget7833-close-icon"]')
    close_element.click()

    write_login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    write_login.send_keys('sivych26@mail.ru')
    write_password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    write_password.send_keys('aaa123')

    button_sign_in = driver.find_element(By.XPATH, '//button[@data-ux-btn="primary"]')
    button_sign_in.click()

    message = driver.find_element(By.XPATH, '//p[@data-aid="MEMBERSHIP_SSO_ERR_REND"]')
    assert message

    time.sleep(2)


