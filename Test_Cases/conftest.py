
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup(request):
    obj_service = Service("C:\\Users\\Vikky\\PycharmProjects\\ParaBank\\Driver\\chromedriver.exe")
    request.cls.driver = webdriver.Chrome(service=obj_service)
    request.cls.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    request.cls.driver.implicitly_wait(20)
    request.cls.driver.maximize_window()



# @pytest.fixture(scope="class")
# def setup(request):
#
#     obj_service = Service("C:\\Users\\Vikky\\PycharmProjects\\ParaBank\\Driver\\chromedriver.exe")
#     driver = webdriver.Chrome(service=obj_service)
#     driver.get("https://parabank.parasoft.com/parabank/index.htm")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()
#
