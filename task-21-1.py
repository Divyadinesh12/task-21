"""
using python selenium display the cookie created before and after login
"""


from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Cookies:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        this method open the url and maximize the window
        :return:None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def wait(self, seconds):
        """
                this method hold on the screen at given second
                :param seconds
                :return None
        """
        sleep(seconds)

    def display_Cookies(self, messege):
        """
        this method display the created cookie
        :param messege:
        :return: cookies
        """
        cookies = self.driver.get_cookies()
        print(f"{messege}cookies:")
        print(cookies)

    def login(self, username, password):
        """
        this method check whether login process working correctly or not and display the cookies to console before loin and after login
        :param username:
        :param password:
        """
        self.display_Cookies("before loin")
        username_input_field = self.driver.find_element(by=By.ID, value="user-name")
        username_input_field.send_keys(username)
        passwoprd_input_field= self.driver.find_element(by=By.ID, value="password")
        passwoprd_input_field.send_keys(password)
        submit_button = self.driver.find_element(by=By.ID, value="login-button")
        submit_button.click()
        self.display_Cookies("after login")
        self.wait(5)

    def quit(self):
        """
        this method quit the driver
        :return:None
        """
        self.driver.quit()


url= "https://www.saucedemo.com/"
obj = Cookies(url)
obj.boot()
obj.login("standard_user","secret_sauce")
obj.quit()