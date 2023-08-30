from Configurtion.logger import classname
from Page_Objects.regi_page import Regi_Page
from Test_Cases.basefile import Base_class
import configparser
config = configparser.ConfigParser()
config.read("utilities/input.properties")

class Test_regi(Base_class,classname):
    def test_login_page(self):
        log = self.getlogs()
        rg = Regi_Page(self.driver)


        rg.click_regi_button()
        log.info("user click on registration button")

        rg.input_first_name(config.get("User_Info", "First_name"))
        log.info("Enter First Name")

        rg.input_last_name(config.get("User_Info", "Last_name"))
        log.info("Enter Last Name")

        rg.input_street_name(config.get("User_Info", "Street_name"))
        log.info("Enter street Name")

        rg.input_city_name(config.get("User_Info", "City_name"))
        log.info("Enter City Name")

        rg.input_state_name(config.get("User_Info", "State_name"))
        log.info("Enter State Name")

        rg.input_zip_code(config.get("User_Info", "Zip_code"))
        log.info("Enter Zip code")

        rg.input_phone_number(config.get("User_Info", "Phone_number"))
        log.info("Enter phone Number")

        rg.input_ssn_number(config.get("User_Info", "Ssn_Number"))
        log.info("Enter SSN Number")

        rg.input_user_name(config.get("User_Info", "User_name"))
        log.info("Enter User Name")

        rg.input_password(config.get("User_Info", "Password"))
        log.info("Enter Password")

        rg.input_confirm_password(config.get("User_Info", "Confirm_password"))
        log.info("Enter confirm Password")

        rg.register_button()
        log.info("click on registration button")




        # self.error_msg = self.driver.find_element(By.XPATH, "//span[@id='customer.username.errors']")
        # if "This username already exists." in self.error_msg:
        #     self.user_name = "roshan123"
        #     self.rg.clear_button()
        #     self.driver.find_element(By.XPATH, "//input[@id='customer.username']").send_keys(self.user_name)
        #     self.driver.find_element(By.XPATH, "//input[@id='customer.password']").send_keys("Avinash123")
        #     self.driver.find_element(By.XPATH, "//input[@id='repeatedPassword']").send_keys("Avinash123")
        #     self.driver.find_element(By.XPATH, "//input[@value='Register']").click()
        # else:
        #     print("if its pass")


