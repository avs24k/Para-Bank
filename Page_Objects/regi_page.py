from selenium.webdriver.common.by import By


class Regi_Page:
    def __init__(self,driver):
        self.driver = driver
        self.regi_button = "Register"
        self.first_name = "customer.firstName"
        self.last_name = "//input[@id='customer.lastName']"
        self.street_name = "input[id='customer.address.street']"
        self.city_name = "//input[@id='customer.address.city']"
        self.state_name = "input[id='customer.address.state']"
        self.zip_code = "//input[@id='customer.address.zipCode']"
        self.phone_number = "customer.phoneNumber"
        self.ssn_number = "customer.ssn"
        self.user_name = "//input[@id='customer.username']"
        self.user_password = "//input[@id='customer.password']"
        self.confirm_password = "//input[@id='repeatedPassword']"
        self.click_button = "//input[@value='Register']"
        self.error_msg = "//span[@id='customer.username.errors']"
        self.clear_button = "//input[@id='customer.username']"

    def click_regi_button(self):
        self.driver.find_element(By.LINK_TEXT, self.regi_button).click()

    def input_first_name(self,first_name):
        self.driver.find_element(By.ID, self.first_name).send_keys(first_name)

    def input_last_name(self,last_name):
        self.driver.find_element(By.XPATH, self.last_name).send_keys(last_name)

    def input_street_name(self,Street):
        self.driver.find_element(By.CSS_SELECTOR, self.street_name).send_keys(Street)

    def input_city_name(self,City):
        self.driver.find_element(By.XPATH, self.city_name).send_keys(City)

    def input_state_name(self,State):
        self.driver.find_element(By.CSS_SELECTOR, self.state_name).send_keys(State)

    def input_zip_code(self,enter_zip):
        self.driver.find_element(By.XPATH, self.zip_code).send_keys(enter_zip)

    def input_phone_number(self,phone_number):
        self.driver.find_element(By.NAME, self.phone_number).send_keys(phone_number)

    def input_ssn_number(self,Enter_SSN):
        self.driver.find_element(By.ID, self.ssn_number).send_keys(Enter_SSN)

    def input_user_name(self,user_name):
        self.driver.find_element(By.XPATH, self.user_name).send_keys(user_name)

    def input_password(self,password):
        self.driver.find_element(By.XPATH, self.user_password).send_keys(password)

    def input_confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password).send_keys(confirm_password)

    def register_button(self):
        self.driver.find_element(By.XPATH, self.click_button).click()

    # def show_register_msg(self):
    #     self.error_msg = self.driver.find_element(By.XPATH, self.error_msg)

    def clear_button(self):
        self.driver.find_element(By.XPATH, self.clear_button).clear()
