"""
using python selenium automation after login into the dashboard of the zen portal do the logout also and verify that the cookies are being generated during the login process
"""


from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class ZenClass:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        this method get and open the url and maximize the window
        :return:None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def display_Cookies(self, messege):
        """
                this method display the created cookie
                :param messege:
                :return: cookies
        """
        cookies = self.driver.get_cookies()
        print(f"{messege}cookies:")
        print(cookies)

    def login(self,username,password):
        """
        this method check whether login process working correctly or not
        :param username:
        :param password:
        :return:str
        """
        self.display_Cookies("before login")
        username_Input_Field = self.driver.find_element(by=By.NAME, value="email")
        username_Input_Field.send_keys(username)
        passWord_Input_Field = self.driver.find_element(by=By.NAME, value="password")
        passWord_Input_Field.send_keys(password)
        submit_button=self.driver.find_element(by=By.TAG_NAME, value="button")
        submit_button.click()
        print("successfully login")
        self.display_Cookies("after login")
        self.wait(5)

    def logout(self):
        """
        this method chck whether log out process working correctly or not
        :return:str
        """
        x_path1 = "/html/body/div[1]/nav/div/div/div/span/img"
        profile = self.driver.find_element(by=By.XPATH, value=x_path1)
        profile.click()
        self.wait(5)
        x_path = "/html/body/div[1]/nav/div/div/div/div/button[2]"
        logoutbutton = self.driver.find_element(by=By.XPATH, value=x_path)
        logoutbutton.click()
        print("successfully logout")

    def wait(self,seconds):
        """
        this method hold on the screen at the given seconds
        :param seconds:
        :return: None
        """
        sleep(seconds)

    def quit(self):
        """
        this method close the driver
        :return:
        """
        self.driver.quit()


url = "https://www.zenclass.in/class"
obj = ZenClass(url)
obj.boot()
obj.login("divyaramaraj06@gmail.com","Nayanika@123")
obj.logout()
obj.quit()