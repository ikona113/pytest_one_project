from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options) ### Открыть хром
    driver.maximize_window()  ### Браузер на весь экран
    driver.implicitly_wait(5) ### Ждать 5 секунд прогрузку
    yield driver
    driver.close()
