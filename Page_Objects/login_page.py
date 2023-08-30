from selenium.webdriver.common.by import By


class LogIn_page:
    def __init__(self,driver):
        self.driver = driver
        self.click_user_name_button = "//input[@name='username']"
        self.user_name = "//input[@name='username']"
        self.user_password = 'password'
        self.click_login_button = "//input[@value='Log In']"

    def user_name_button(self):
        self.driver.find_element(By.XPATH, self.click_user_name_button).click()

    def input_name(self, Enter_Name):
        self.driver.find_element(By.XPATH, self.user_name).send_keys(Enter_Name)

    def input_password(self,Enter_Password):
        self.driver.find_element(By.NAME, self.user_password).send_keys(Enter_Password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.click_login_button).click()





