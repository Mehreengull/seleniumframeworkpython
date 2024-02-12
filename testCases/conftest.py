import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Safari()
    return driver


# this will get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# this will return browser value to set up method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(configure):
#     configure.metadata['Project Name'] = 'nop Commerce'
#     configure.metadata['Module Name'] = 'Customers'
#     configure.metadata['Tester'] = 'Pavan'
#
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
