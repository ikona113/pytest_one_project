import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



@pytest.fixture()
def driver():
    driver = webdriver.Chrome() ### Открыть хром
    driver.maximize_window()  ### Браузер на весь экран
    driver.implicitly_wait(5) ### Ждать 5 секунд прогрузку
    yield driver
    driver.close()

def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html') ### Открыть страницу =

    galaxy_s6 = driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']") ### Найти элемент ссылка которого имеет текст = Samsung galaxy s6
    galaxy_s6.click() ### Кликнуть по элементу
    title = driver.find_element(By.CSS_SELECTOR, 'h2') ### Найти тег = h2
    assert title.text == 'Samsung galaxy s6'