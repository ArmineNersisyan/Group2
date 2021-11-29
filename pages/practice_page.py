from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import helpers
from lib.test_logger import logger

home_page_btn = (By.XPATH, "//a[contains(text(),'HOME')]")
#page_body = (By.CSS_SELECTOR,".body-style")
page_body = (By.TAG_NAME, 'body')
btn_sign_in = (By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']")
#btn_sign_in = (By.CSS_SELECTOR, "a[href^='/login']")


def click_sign_in_btn():
    try:
        # helpers.wait_element_appear(page_body)
        helpers.find_and_send_keys(page_body, (Keys.CONTROL + Keys.HOME))
        helpers.find_and_click(btn_sign_in)
        logger('Sign in was successfully performed')

    except Exception as e:
        logger(e, True)
