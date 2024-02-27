from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_id = "//input[@id='username']"
        self.login_password = "//input[@id='password']"
        self.login_button = "//button[@class='woocommerce-button button woocommerce-form-login__submit']"

    def send_user_id(self, loginid):
        self.driver.find_element(By.XPATH, self.login_id).send_keys(loginid)

    def send_login_password(self, password):
        self.driver.find_element(By.XPATH, self.login_password).send_keys(password)

    def cilck_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def take_a_screen_shot(self, tcount):
        self.driver.get_screenshot_as_file(f"screen_png{tcount}.png")