import time

import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "./TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("TEST WITH DATA")
        self.logger.info("***Test case to verify login with data***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = XLUtilis.getRowCount(self.path, 'Sheet1')
        lst_status = []  # empty list variable
        for r in range(2, self.rows+1):
            self.username = XLUtilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilis.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            # Conditions to verify that there is no conflict in actual result and expected result in sheet
            if actual_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("Test case Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("Test case Failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif actual_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("failed")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info('Passed')
                    lst_status.append("Pass")
            print(lst_status)

            if "Fail" not in lst_status:
                self.logger.info(" Login ddt passed")
                self.driver.close()
                assert True
            else:
                self.logger.info(" Login ddt failed")
                self.driver.close()
                assert False
