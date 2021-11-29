from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lib.driver import get_driver 
from lib.test_logger import logger
from selenium.webdriver.common.keys import Keys
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = get_driver()


def go_to_page(url, new_window=False):
    try:
        if new_window:
            driver.execute_script(f"window.open('{url}');")
        else:
            driver.get(url)
            driver.maximize_window()
            logger("The driver was successfully opened")

    except Exception as e:
        logger(e, True)


def find_and_click(loc, timeout=3):
    try:
        elem = find(loc, timeout)
        elem.click()
        logger("The element was successfully found anh clicked")
    except Exception as e:
        logger(e, True)
    

def find_and_send_keys(loc, inp_text, timeout=3):
    try:
        elem = find(loc, timeout)
        elem.send_keys(inp_text)
        logger("The data was successfully sent")
    except Exception as e:
        logger(e, True)


def find_and_send_keys_click (loc, inp_text, timeout=3):
    try:
        elem = find(loc, timeout)
        elem.send_keys(inp_text+Keys.ENTER)
        logger("The data was successfully sent")
    except Exception as e:
        logger(e, True)


def find(loc, timeout=3, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))
        logger("The element was successfully presented")  
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem         
    except Exception as e:
        logger(e, True)

def find_all(loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc),
                                                        message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        return False
    return elements

def open_file(file_name, text):
    try:
        with open (file_name, 'a+') as f:
            f.write(text+ '\n')
    except Exception as e:
        logger(e, True)

def wait_element_appear(loc, timeout=10):
    WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))

def wait_for_page(page="", not_page="", timeout=10):
    if page:
        WebDriverWait(driver, timeout).until(expected_conditions.url_contains(page))
    elif not_page:
        WebDriverWait(driver, timeout).until_not(expected_conditions.url_contains(not_page))

def random_str(symbols_count):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))
