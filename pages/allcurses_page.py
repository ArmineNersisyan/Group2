from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from lib import helpers
from lib.test_logger import logger
from testdata import test_data
from lib.helpers import open_file

# navigation = (By.XPATH, "//div[@id='navbar-inverse-collapse']")

click_allcourses =(By.XPATH, "//a[contains(text(),'ALL COURSES')]")
search = (By.XPATH, "//input[@id='search']")
# sel1 = (By.XPATH, "//div[@id='course-list']/div[1]")#arajin tab
# sel2 = (By.XPATH, "//div[@id='course-list']/div[2]")#erkrord tab
# sel3 = (By.XPATH, "//div[@id='course-list']/div[2]")#errord tab
titles_selector = (By.XPATH, "//h4[@class='dynamic-heading']")
# titl1=(By.XPATH, "//div[@id='course-list']/div//following::h4[contains(text(),'With Python 3.x')]")
# titl2=(By.XPATH, "//div[@id='course-list']/div//following::h4[contains(text(),'Advanced')]")
# titl3=(By.XPATH, "//div[@id='course-list']/div//following::h4[contains(text(),'With Java')]")
currency_selector = (By.XPATH, "//span[contains(@class,'zen-course-price')]")
# prices1= (By.XPATH, "//span[@class='currency'].text")
# prices2= (By)

file_name = 'result.txt'

def allcourses_search():
    try:
        helpers.find_and_click(click_allcourses)
        elem = helpers.find_and_send_keys_click(search, test_data.search_data)
        logger("result count" + len(elem))
    except Exception as e:
        logger(e, True)

def get_result():
    list_of_elements = helpers.find_all(titles_selector)
    price_list = helpers.find_all(currency_selector)
    open_file(file_name, str(len(list_of_elements)))
    for i in list_of_elements:
        open_file(file_name, i.text)
    for j in price_list:
        open_file(file_name, j.text)
  