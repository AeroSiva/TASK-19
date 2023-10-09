'''Visit the URL htttps://www.aucedemo.co,/ and login with the following credentials:-

    Username: standard_user
    password: standard_user ----- As this password is not valid secret_sauce is taken as password

Try to fetch the following using Python selenium:-
    1) Title of the Webpage
    2) Current URL of the webpage
    3) Extract the entire content of the webpage and save it in a Text file whse name will be "Webpage_task_11.txt" '''



from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Basic_webpage_func:

    def __init__(self, web_url):
        self.url = web_url
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)

    # Visit the URL htttps://www.aucedemo.co,/ 
    def open_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
        except NoSuchElementException as selenium_error:
           print(f"Opening URL failed : {selenium_error}")

    def shutdown(self):
        self.driver.quit()


class Saucedemo(Basic_webpage_func):

    def __init__(self,username,password, web_url):
        super().__init__(web_url)
        self.username = username
        self.password = password


    # login using given credendials
    def login(self):
        try:
            self.driver.find_element(by=By.ID,value="user-name").send_keys(self.username)
            self.driver.find_element(by=By.ID,value="password").send_keys(self.password)
            self.driver.find_element(by=By.ID,value="login-button").click()
            sleep(4)
        except NoSuchElementException as selenium_error:
           print(f"Login Failed : {selenium_error}")


    # Fetching Title of the Webpage
    def fetch_title(self):
        try:
            current_title = self.driver.title
            return current_title
        except NoSuchElementException as selenium_error:
           print(f"Fetching URL Failed : {selenium_error}")

    
    # Fetching Current URL of the webpage
    def current_url(self):
        try:
            c_url = self.driver.current_url
            return c_url
        except NoSuchElementException as selenium_error:
           print(f"Fetching current URL Failed : {selenium_error}")


    # Extract the entire content of the webpage and save it in a Text file whse name will be "Webpage_task_11.txt
    def extract_content(self):
        try:
            content = self.driver.page_source
            file_name = "Webpage_task_11.txt"
            with open(file_name,"w") as file:
                file.write(content)
                print(f"Success: Entire content of the webpage is extracted and saved in {file_name} as Text file")
        except NoSuchElementException as selenium_error:
           print(f"Extracting and saving entire content Failed : {selenium_error}")


sauce = Saucedemo(web_url = "https://www.saucedemo.com/", username= "standard_user", password= "secret_sauce")

sauce.open_url()

sauce.login()

print(f"Title of Web-page is: {sauce.fetch_title()}")

print(f"URL of Web-page is: {sauce.current_url()}")

sauce.extract_content()

sauce.shutdown()