from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    phones = (By.XPATH, "//div/h4[@class='card-title']")
    phonesFooter = (By.XPATH, "div/button")
    phonesButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.phones)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.phonesFooter)

    def getCardButton(self):
        self.driver.find_element(*CheckOutPage.phonesButton).click()
        return ConfirmPage(self.driver)  # Instantiate ConfirmPage
