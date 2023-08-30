from Page_Objects.login_page import LogIn_page
from Test_Cases.basefile import Base_class


class Test_login(Base_class):
    def test01(self):
        lg = LogIn_page(self.driver)
        lg.user_name_button()
        lg.input_name("Avinash")
        lg.input_password("Avinash123")
        lg.login_button()
