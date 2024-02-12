import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    main_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_xpath = "//a[normalize-space()='Add new']"
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    first_name_id = "FirstName"
    last_name_id = "LastName"
    gender_male_id = "Gender_Male"
    gender_female_id = "Gender_Female"
    dob_xpath = "//input[@id='DateOfBirth']"
    company_id = "Company"
    roles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    administrator_xpath = "//li[normalize-space()='Administrators']"
    guest_xpath = "//li[normalize-space()='Guests']"
    vendors_xpath = "//li[contains(text(),'Vendors')]"
    registered_xpath = "//li[@id='a0da2a02-1ac4-45b2-a726-73807065e091']"
    manager_of_vendor_id = "VendorId"
    admin_comment = "//textarea[@id='AdminComment']"
    save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.list_of_roles = None
        self.driver = driver

    def click_onCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.main_menu_xpath).click()

    def click_onCustomer_list_menu(self):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_xpath)))
        element.click()

    def add_new_customer(self):
        self.driver.find_element(By.XPATH, self.add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def setFirstName(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.gender_male_id).click()

    def set_date_of_Birth(self, dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)

    def setCompanyName(self, company_name):
        self.driver.find_element(By.ID, self.company_id).send_keys(company_name)

    def setCustomerRole(self, role):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.roles_xpath)))
        element.click()
        if role == "Registered":
            # save the role into a list variable
            self.list_of_roles = self.driver.find_element(By.XPATH, self.registered_xpath)
        elif role == "Administrators":
            self.list_of_roles = self.driver.find_element(By.XPATH, self.administrator_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_of_roles = self.driver.find_element(By.XPATH, self.guest_xpath)
        elif role == 'Registered':
            self.list_of_roles = self.driver.find_element_by_xpath(self.registered_xpath)
        elif role == 'Vendors':
            self.list_of_roles = self.driver.find_element_by_xpath(self.vendors_xpath)
        else:
            self.list_of_roles = self.driver.find_element_by_xpath(self.guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.list_of_roles)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.manager_of_vendor_id))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.admin_comment).send_keys(content)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.save_xpath).click()
