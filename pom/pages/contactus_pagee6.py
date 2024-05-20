from selenium.webdriver.common.by import By

class ContactUs:


    def __init__(self,driver):
        self.driver=driver
        self.contactus_button=(By.XPATH,"//a[contains(text(),'contact us')]")

    def open_contactus_page(self,url):
        self.driver.get(url)

    def click_contactus(self,url):
        self.driver.get(url)

    # def click_contactus(selfs):
    #     selfs.driver.find_element(* selfs.contactus_button).click

