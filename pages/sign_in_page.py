import time
from selenium.webdriver.common.by import By
from lib import helpers
from lib.test_logger import logger
from testdata import test_data
# from sign_up_page import click_logout_btn

txt_email = (By.ID, "email")
txt_pass = (By.ID, "password")
btn_login = (By.XPATH, "//input[@value='Login']")
msg_invalid = (By.XPATH, "//input[@id='email']//following::span[contains(text(),'invalid')]")
msg_valid = "https://courses.letskodeit.com/"
sign_in_btn = (By.XPATH, "//a[@class='dynamic-link']//preceding::a[text()='Sign In']")
sign_up_btn = (By.XPATH, "//a[contains(text(),'Sign Up')]")
# navigation = (By.XPATH, "//div[@id='navbar-inverse-collapse']")
# search = (By.XPATH, "//input[@id='search']")
# click_btn =(By.XPATH, "//i[@class='fa fa-search']")
# sel_courses = (By.XPATH, "//div[@id='course-list']/div[3]")
# sel1= //div[@id='course-list']/div//following::h4[contains(text(),'With Python 3.x')]
# //div[@id='course-list']/div//following::h4[contains(text(),'Advanced')]
# //div[@id='course-list']/div//following::h4[contains(text(),'With Java')]


def sign_in(): 
    try:   
        helpers.find_and_click(sign_in_btn)
        helpers.find_and_send_keys(txt_email, test_data.email_data)
        helpers.find_and_send_keys(txt_pass, test_data.pass_data)
        time.sleep(5)
        helpers.find_and_click(btn_login)
        logger('Sign in was successfully performed')
    except Exception as e:
        logger(e, True)

    
def click_sign_up_btn(): 
    try:
        helpers.find_and_click(sign_up_btn)
        logger('Sign up was successfully performed')
    except Exception as e:
        logger(e, True)

def check_logged_in(driver_current):
    try:
        if driver_current.current_url == msg_valid:
            validation_msg = 'we are logged in'
        else:
            validation_msg = helpers.find(msg_invalid, 3, get_text=True)
        logger(f'Validation Message is - {validation_msg}')
    except Exception as e:
        logger(e, True)