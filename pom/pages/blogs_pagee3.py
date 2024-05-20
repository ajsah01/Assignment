from selenium.webdriver.common.by import By

class Blogs:

    def __init__(self, driver):
        self.driver = driver
        self.blogs_button = (By.XPATH, "//a[normalize-space(),'blogs')]")

    def open_blogs_page(self, url):
        self.driver.get(url)

    # def click_blogs(self):
    #     self.driver.find_element(*self.blogs_button).click()
