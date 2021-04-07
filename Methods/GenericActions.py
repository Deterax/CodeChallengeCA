import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as LeCondition
from selenium.webdriver.support.wait import WebDriverWait


class generic_actions(object):

    # initializes the class
    def __init__(self, wd):
        self.driver = wd

    # Loads defined Page
    def load_page(self, url):
        self.driver.get(url)

    # compares if an element is preset on the website
    def is_element_present(self, how, what):
        try:
            # find element, if it can find it returns true, if not returns false
            time.sleep(2)
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print ("element not found")
            return False
        return True

    # Validate if the link of a given element is active and replies
    def link_works(self, what):
        try:
            # wait for loading to be completed
            WebDriverWait(self.driver, 3).until(LeCondition.presence_of_element_located((By.XPATH, what)))
            for a in self.driver.find_elements_by_xpath(what):
                print(a.get_attribute('href'))
                urlCheck = requests.head(a.get_attribute('href')).status_code
                if urlCheck == 200:
                    return True
                else:
                    return False
        except NoSuchElementException as e:
            return False

    # compares the text of an element to a base saved parameter
    def check_text(self, what, where):
        # searches footer text and verify if text matches what is currently being displayed
        bodyText = self.driver.find_elements_by_xpath(where)
        for a in bodyText:
            if what in a.text:
                return True
            else:
                return False

    # Writes an specific zipcode to the zipcode field
    def write_zipcode(self, what, where):
        element = self.driver.find_element_by_xpath(where)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys(what)
        time.sleep(1)

    # compares if an element is clickable
    def is_clickable(self, what):
        return self.driver.find_element_by_xpath(what).is_enabled()

    # compares if during navigation we had a change of tab to a new URL
    # this is compared to the base url defined above
    def is_dif_tab(self, baseURL):
        if self.driver.current_url == baseURL:
            return False
        else:
            return True
