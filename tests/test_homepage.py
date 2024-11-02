import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from TestData.homepagedata import HomePageData

class TestHomePage(BaseClass):

 
    def test_FormSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.checkBox().click()
        self.selectOption(homepage.getForm(),getData["gender"])
        
        homepage.submitForm().click()
        alertText = homepage.alertMessage().text
        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getData("Testcase2"))
    def getData(self, request):
        return request.param
