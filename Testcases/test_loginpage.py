from selenium import webdriver
import pytest
from Pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_ife_store")
class Test_login_page001:

    def test_loginid_001(self):
        lg = LoginPage(driver = self.driver)
        lg.send_user_id("akshaytakale4@gmail.com")
        # self.driver.get_screenshot_as_file("png1.png")
        lg.send_login_password("Akii@2227")
        lg.cilck_on_login_button()

    @pytest.mark.parametrize("login_id, Password",
                             [("akshay1", "akshay123"), ("akshay2", "akshay123"), ("akshay3", "akshay123")])
    def test_loginid_002(self, login_id, Password):
        lg = LoginPage(self.driver)
        # super.self.driver = self.driver
        lg.send_user_id(login_id)
        # self.driver.get_screenshot_as_file(Password)
        lg.send_login_password("Akii@2227")
        lg.cilck_on_login_button()

    @pytest.mark.parametrize("loginid, c_password, conditions",[("akshaytakale4@gmail.com", "Akii@9822","1"), ("akshaytakale4@gmail.com", "Akii@98224","2")])
    def test_correct_loginid_001(self, loginid, c_password, conditions):
        lg = LoginPage(driver=self.driver)
        lg.send_user_id(loginid)
        lg.send_login_password(c_password)
        lg.cilck_on_login_button()
        lg.take_a_screen_shot(conditions)

@pytest.mark.usefixtures("setup_ife_store")
class Test_login_page_multiple_ids:


    @pytest.mark.parametrize("login_id, Password",[("akshay1","akshay123"),("akshay2","akshay123"),("akshay3","akshay123")])
    def test_loginid_002(self, login_id, Password):
        lg = LoginPage(self.driver)
        # super.self.driver = self.driver
        lg.send_user_id(login_id)
        # self.driver.get_screenshot_as_file(Password)
        lg.send_login_password("Akii@2227")
        lg.cilck_on_login_button()
