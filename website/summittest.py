from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebsiteLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service, options=self.options)

    def login(self):
        self.browser.get("https://summit.armstrongltd.co.in/Default.aspx")
        print(self.browser.title)
        uname = self.browser.find_element(By.ID, "txtLoginName")
        uname.send_keys(self.username)
        pwd = self.browser.find_element(By.ID, "txtPassword")
        pwd.send_keys(self.password)
        submit = self.browser.find_element(By.ID, "btnLogin")
        submit.click()
        print('clicked')
        sleep(2)

        error_message = "Please"
        # Retrieve any errors found. 
        try:
            errors = self.browser.find_element(By.ID, "lblMessage")
            print(errors.text)

            # When errors are found, the login will fail. 
            if error_message in errors.text: 
                print("[!] Login failed")

        except:
            print("[+] Login successful")

        self.browser.get("https://summit.armstrongltd.co.in/Timesheet/EventEntryR.aspx") 
        sleep(10)
        print(self.browser.title)


    def __del__(self):
        self.browser.quit()


loginsummit = WebsiteLogin("30196", "Pravin@123")
loginsummit.login()
