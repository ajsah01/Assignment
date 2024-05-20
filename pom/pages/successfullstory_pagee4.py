from selenium.webdriver.common.by import By


class Successfulstory:

    def __init__(self,driver):
        self.driver=driver
        self.Successfulstory_button = (By.XPATH, "//a[contains(text(),'successful stories'')]")



    def open_successfulstory_page(self, url):
        self.driver.get(url)

