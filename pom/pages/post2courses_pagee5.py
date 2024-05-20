from selenium.webdriver.common.by import By

class Post2Courses:

    def __init__(self,driver):
        self.driver=driver
        self.post2courses_button= (By.XPATH,"//a[contains(text(),'post +2 courses')]")


    def open_post2courses_page(self,url):
        self.driver.get(url)


