import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions


@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
