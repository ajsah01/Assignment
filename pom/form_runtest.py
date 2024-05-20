import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pom.pages.contactform import Contactform


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

def test_Contactform(driver):
    submit_page = Contactform(driver)
    submit_page.open_page("https://mindrisers.com.np/contact-us")
    time.sleep(1)
    driver.maximize_window()
    submit_page.enter_Name("jay")
    time.sleep(1)
    submit_page.enter_Email("rk@gmail.com")
    time.sleep(2)
    submit_page.enter_Phone(9808737383)
    time.sleep(3)
    submit_page.enter_Subject("mathe")
    time.sleep(5)
    submit_page.enter_Queries("Ajnkajhicdgbwcecbuiwvevbivweui")
    time.sleep(2)

    # Contactform.click_submit()
    # time.sleep(5)

    print("congrats")
