from selenium.webdriver.common.by import By

class Contactform:

    def __init__(self,driver):
        self.driver=driver
        self.Name_textbox=(By.XPATH,"//input[@placeholder='Name']")
        self.Email_textbox = (By.XPATH,"//input[@placeholder='Email']")
        self.Phone_textbox = (By.XPATH,"//input[@placeholder='Phone']")
        self.Subject_textbox = (By.XPATH,"//input[@placeholder='Subject']")
        self.Queries_textbox =(By.XPATH,"//textarea[@placeholder='Queries']")
        # self.click_Recaptcha=(By.XPATH,"//div[@class='recaptcha-checkbox-border']")
        #
        # self.submit_button= (By.XPATH,"//button[normalize-space()='Submit']")

    def open_page(self,url):
        self.driver.get(url)

    def enter_Name(self,Name):
        self.driver.find_element(*self.Name_textbox).send_keys(Name)

    def enter_Email(self,Email):
        self.driver.find_element(*self.Email_textbox).send_keys(Email)

    def enter_Phone(self,Phone):
        self.driver.find_element(*self.Phone_textbox).send_keys(Phone)

    def enter_Subject(self,Subject):
        self.driver.find_element(*self.Subject_textbox).send_keys(Subject)


    def enter_Queries(self, Queries):
        self.driver.find_element(*self.Queries_textbox).send_keys(Queries)

