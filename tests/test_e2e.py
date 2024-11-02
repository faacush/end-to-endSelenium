import pytest

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckOutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage

class TestOne(BaseClass):

    def test_2e2(self):
        log = self.getLogger()
        
        home_Page = HomePage(self.driver)

        # Navigate to the 'shop' section
        checkout_page = home_Page.shopItems()
        log.info("getting card titles")
        
        # Find all phone cards
        phones = checkout_page.getCardTitles()
        i = -1
        # Loop through the phone cards and click on 'Blackberry'
        for phone in phones:
            i = i + 1
            name = phone.find_element(By.XPATH, "//a[normalize-space()='Blackberry']")
            log.info(name)
            if name == "Blackberry":
                checkout_page.getCardFooter().click()

        # Proceed to checkout
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # Confirm the order
        confirm_page = checkout_page.getCardButton()
        log.info("entering country name")
        # Enter country name
        confirm_page.Delivery()

        # Wait for the India link to be present and then click it
        self.verifyLinkPresence("India")

        confirm_page.send_location()

        # Agree to the terms and submit the form

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_page.submit()

        # Verify the success message
        success_text = confirm_page.success_text()
        log.info("Text received from the app is"+success_text)
        assert "Success" in success_text
