from selenium import webdriver
import pytest


@pytest.fixture()
def setup_ife_store(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://ifestore.com/my-account/")
    yield
    request.cls.driver.close()
