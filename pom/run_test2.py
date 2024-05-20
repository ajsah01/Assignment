import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pom.pages.placementpartner_pagee2 import Placementpartner
from pom.pages.contactus_pagee6 import ContactUs
from pom.pages.blogs_pagee3 import Blogs
from pom.pages.ourcourse_pagee1 import Courses
from pom.pages.successfullstory_pagee4 import Successfulstory
from pom.pages.post2courses_pagee5 import Post2Courses


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_placementpartner_page(driver):
    placementpartner_page =Placementpartner(driver)
    placementpartner_page.open_placementpartner_page("https://mindrisers.com.np/placement-partner")
    time.sleep(3)
    driver.maximize_window()
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 900
    scroll_iteration = int(page_height /scroll_speed)

    for _ in range(scroll_iteration):

        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        time.sleep(4)

def test_course_page(driver):
    course_page=Courses(driver)
    course_page.open_courses_page("https://mindrisers.com.np/courses")
    time.sleep(5)
    driver.maximize_window()
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed =1000
    scroll_iteration = int(page_height / scroll_speed)

    for _ in range(scroll_iteration):


        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        time.sleep(5)

def test_blogs_page(driver):
    blogs_page=Blogs(driver)
    blogs_page.open_blogs_page("https://mindrisers.com.np/courses")
    time.sleep(5)
    driver.maximize_window()
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=900
    scroll_iterarion = int(page_height / scroll_speed)

    for _ in range(scroll_iterarion):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        time.sleep(2)

def test_post2courses_page(driver):
    post2courses_page=Post2Courses(driver)
    post2courses_page.open_post2courses_page("https://mindrisers.com.np/after+2-courses")
    time.sleep(5)
    driver.maximize_window()
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=850
    scroll_iteration=int(page_height / scroll_speed)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed})")
        time.sleep(3)


def test_successfullstory_page(driver):
    page_successfullstory=Successfulstory(driver)
    page_successfullstory.open_successfulstory_page("https://mindrisers.com.np/success-gallery")
    time.sleep(4)
    driver.maximize_window()
    page_height= driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 800
    scroll_iteration =int(page_height / scroll_speed)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed})")
        time.sleep(4)

def test_contactus_page(driver):
    page_contactus=ContactUs(driver)
    page_contactus.open_contactus_page("https://mindrisers.com.np/contact-us")
    time.sleep(4)
    driver.maximize_window()
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=700
    scroll_iteration=int(page_height / scroll_speed)
    time.sleep(3)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        time.sleep(3)


    print("congratr̥")

