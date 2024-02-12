from selenium.webdriver.common.by import By


class SearchCustomer:
    searchEmail_id = "SearchEmail"
    searchFirstName_id = "SearchFirstName"
    searchLastName_id = "SearchLastName"
    search_button_id = "search-customers"
    full_table_xpath = "(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[1]"
    result_table_id = "customers-grid"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.emailid = None
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.searchEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.searchFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.searchLastName_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        self.flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.ID, self.result_table_id)
            self.emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if self.emailid == email:
                self.flag = True
                break
        return self.flag

    def searchCustomerByName(self, Name):
        self.flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.ID, self.result_table_id)
            self.name = table.find_element(By.XPATH,
                                              "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if self.name == Name:
                self.flag = True
                break
        return self.flag