import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date 
from selenium.webdriver.support.select import Select


class SummitDataEntry:

    def __init__(self,  data_dict):
        self.data_dict = data_dict
        self.username = self.data_dict["username"]
        self.password = self.data_dict["password"]
        self.data_dict = data_dict

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def login(self):
        self.browser.get("https://summit.armstrongltd.co.in/Default.aspx")

        uname = self.browser.find_element(By.ID, "txtLoginName")
        uname.send_keys(self.username)
        pwd = self.browser.find_element(By.ID, "txtPassword")
        pwd.send_keys(self.password)
        submit = self.browser.find_element(By.ID, "btnLogin")
        submit.click()
        sleep(2)

        # Verify that the login was successful.
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

    def submit_data(self):
        self.browser.get("https://summit.armstrongltd.co.in/Timesheet/EventEntryR.aspx")
        sleep(2)
        # Get date in DD/MM/YYYY format
        date_today = date.today().strftime("%d/%m/%Y")
        date_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlDate"))
        date_field.select_by_visible_text("22/02/2023")

        task_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlType"))
        task_field.select_by_visible_text("Task")

        start_time_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlStartHours"))
        start_time_field.select_by_visible_text("09:00")

        end_time_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlEndHours"))
        end_time_field.select_by_visible_text("18:00")

        task_name_field = self.browser.find_element(By.ID, "ContentPlaceHolder1_txtTaskName")
        task_name_field.send_keys(self.data_dict["task_name"])

        task_notes_field = self.browser.find_element(By.ID, "ContentPlaceHolder1_txtTaskNotes")
        task_notes_field.send_keys(self.data_dict["task_notes"])

        link_field = self.browser.find_element(By.ID, "ContentPlaceHolder1_rdbCategory_2")
        link_field.click()

        city_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlCity"))
        city_field.select_by_visible_text(self.data_dict["city"])

        medium_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlMedium"))
        medium_field.select_by_visible_text("Solo")

        project_field = Select(self.browser.find_element(By.ID, "ContentPlaceHolder1_ddlProjCode"))
        project_field.select_by_value(self.data_dict["project_code"])

        submit_button = self.browser.find_element(By.ID, "btnSaveNewTask")
        submit_button.click()

        print("Waiting")
        sleep(10)
        self.browser.quit()
    
    def submitForApproval(self):
        # Get today's date in the format expected by the review page
        today = "22/02/2023"#date.today().strftime("%d/%m/%Y")

        # Construct the URL for the review page
        url = f"https://summit.armstrongltd.co.in/Timesheet/ReviewMyDayR.aspx?year={datetime.today().year}&jmonth={datetime.today().month-1}&month={datetime.today().strftime('%m')}&date={today.split('/')[0]}"
        self.browser.get(url)
        sleep(2)
        submit_button = self.browser.find_element(By.ID, "ContentPlaceHolder1_btnSubmitTimesheet")
        submit_button.click()
        # Wait for the dialog to appear
        alert = self.browser.switch_to.alert

        # Accept the dialog
        alert.accept()
        sleep(2)
        self.browser.quit()



# data = {
#     "username": "30196",
#     "password": "Pravin@123",
#     "task_name": "Task Name",
#     "task_notes": "Task details to be given here. A1336 details. It should be at least 50 char. SO I don't know how much is this.",
#     "city": "Nashik",
#     "project_code": "A1336"
# }

# auto = SummitDataEntry(data)

# auto.login()
# auto.submit_data()