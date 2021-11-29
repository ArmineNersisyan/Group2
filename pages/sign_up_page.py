from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import helpers
from lib.test_logger import logger
from testdata import test_data

page_body = (By.TAG_NAME, 'body')
sign_in = (By.XPATH, "//a[@class='dynamic-link']//preceding::a[text()='Sign In']")
sign_up = (By.XPATH, "//a[text()=' Sign Up']")
#sign_reg_btn = (By.ID, "[data-uniqid='1577353831117']")
input_first_name = (By.XPATH, "//input[@placeholder='First Name']")
input_last_name = (By.XPATH, "//input[@placeholder='Last Name']")
input_email_address = (By.XPATH, "//input[@placeholder='Email Address']")
input_pswd = (By.XPATH, "//input[@placeholder='Password']")
confirm_pswd = (By.XPATH, "//input[@placeholder='Confirm Password']")
sign_up_btn = (By.XPATH, "//input[@data-action='submit_signup']")
img_btn = (By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
logout_btn = (By.XPATH, "//*[@id='navbar-inverse-collapse']/div[1]/div/div/ul/li[3]/a")
msg_txt = (By.XPATH, "//div[text()='//h1[text()='My Courses']']")



def registration():
    try:
        helpers.find_and_send_keys(page_body, (Keys.CONTROL + Keys.HOME))
        helpers.find_and_click(sign_in)
        helpers.find_and_click(sign_up)
        helpers.find_and_send_keys(input_first_name, test_data.firstname)
        helpers.find_and_send_keys(input_last_name, test_data.lastname)
        helpers.find_and_send_keys(input_email_address, helpers.random_str(5)+'@'+helpers.random_str(4)+'.'+'com')
        helpers.find_and_send_keys(input_pswd, test_data.pass_data)
        helpers.find_and_send_keys(confirm_pswd, test_data.pass_data)   
        helpers.find_and_click(sign_up_btn) 
        logger('Registration successfully performed')       
    except Exception as e:
        logger(e, True)


def click_logout_btn(): 
    try:
        helpers.find_and_click(img_btn)
        helpers.find_and_click(logout_btn)
        logger('Log out was successfully performed')
    except Exception as e:
        logger(e, True)


