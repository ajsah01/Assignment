from selenium.webdriver.common.by import By

class Courses:

    def __init__(self, driver):
        self.driver = driver
        self.courses_button = (By.XPATH, "//a[normalize-space(),'our courses')]")

    def open_courses_page(self, url):
        self.driver.get(url)

    def click_courses(self,url):
        self.driver.get(url)


