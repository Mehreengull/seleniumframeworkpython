import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestSearchByEmail:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_byEmail(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.add_cust = AddCustomer(self.driver)

        self.add_cust.click_onCustomerMenu()

        self.add_cust.click_onCustomer_list_menu()

        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setFirstName("Victoria")
        self.searchCustomer.setLastName("Terces")
        self.searchCustomer.clickSearch()
        self.searchCustomer.searchCustomerByName("Victoria Terces")
        self.driver.close()


