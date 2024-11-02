from selenium.webdriver.common.by import By
from pageObject.CheckOutPage import CheckOutPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    form = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)  # Instantiate CheckOutPage
    
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def checkBox(self):
        return self.driver.find_element(*HomePage.check)

    def getForm(self):
        return self.driver.find_element(*HomePage.form)
    
    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)
    def alertMessage(self):
        return self.driver.find_element(*HomePage.alert)