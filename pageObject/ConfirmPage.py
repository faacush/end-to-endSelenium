from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID, "country")
    location = (By.LINK_TEXT, "India")
    final_step = (By.CSS_SELECTOR, "input[type='submit']")
    confirmation = (By.CLASS_NAME, "alert-success")

    def Delivery(self):
        self.driver.find_element(*ConfirmPage.countryName).send_keys("ind")
    
    def send_location(self):
        self.driver.find_element(*ConfirmPage.location).click()

    def submit(self):
        self.driver.find_element(*ConfirmPage.final_step).click()

    def success_text(self):
        return self.driver.find_element(*ConfirmPage.confirmation).text
