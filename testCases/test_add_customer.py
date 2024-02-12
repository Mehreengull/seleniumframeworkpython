import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string
import pytest


class TestAddCustomer:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
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

        self.add_cust.add_new_customer()
        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword("1234567")
        self.add_cust.setFirstName("Martha")
        self.add_cust.setLastName("Cano")
        self.add_cust.setGender("Female")
        self.add_cust.set_date_of_Birth("7/05/1985")
        self.add_cust.setCompanyName("Company name")
        self.add_cust.setCustomerRole("Guests")
        self.add_cust.setManagerOfVendor("Vendor 2")
        self.add_cust.setAdminContent("Admin Content")
        self.add_cust.click_on_save()
        self.message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.message)

        if "The new customer has been added successfully." in self.message:
            assert True
        else:
            assert False

        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
