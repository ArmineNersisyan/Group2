from webdriver_manager import driver
from lib import helpers
from lib import driver
#from pages.allcurses_page import allcourses_search
from testdata import test_data
from pages import practice_page, sign_in_page, sign_up_page, allcurses_page 
from webdriver_manager.utils import validate_response


def test_5():
    our_driver = driver.get_driver()
    # page = 
    helpers.go_to_page(test_data.practice_url)
    # helpers.wait_for_page(page)
    
    practice_page.click_sign_in_btn()
    sign_in_page.click_sign_up_btn()
    sign_up_page.registration()
    sign_up_page.click_logout_btn()
    sign_in_page.sign_in()
    sign_in_page.check_logged_in(our_driver)

    allcurses_page.allcourses_search()
    allcurses_page.get_result()

    helpers.driver.quit()

if __name__ == '__main__':
    test_5()
