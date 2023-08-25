""" CommonLibrary.py """
# pylint: disable=R0915
# pylint: disable=E0001

import json
import os.path
import time
from robot.api import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonLibrary:
    """Class: CommonLibrary"""

    def __init__(self, envfile, browser, url):
        """
        Create the variables associated with the class
        :type envfile: string
        :param envfile: the environment JSON file

        :type browser: string
        :param browser: can be chrome, firefox, or msedge

        :type url: string
        :param url: should be a valid url to Ready staging or production
        """

        self.url = url
        self.max_browser_wait = 30
        self.wait_for_obj = 30
        try:
            envfile_path = "./data/" + envfile
            if os.path.exists(envfile_path):
                with open(envfile_path) as json_file:
                    self.data = json.load(json_file)
            else:
                raise Exception(
                    "Aborting testing due to environment file: {} does not exist!".format(
                        envfile_path
                    )
                )

            if browser.lower() == "chrome":
                print("Running against Chrome browser...")
                options = webdriver.ChromeOptions()
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--start-maximized")
                options.add_argument("--headless")
                # The line below checks for the version of the browser.
                self.driver = webdriver.Chrome(
                    executable_path="/usr/local/bin/chromedriver", options=options
                )
                self.driver.get(self.url)
                self.driver.implicitly_wait(self.max_browser_wait)
                page_title = self.driver.title
                print("Login Page title: {}".format(page_title))
                assert page_title == "CS-Admin", "Expected 'CS-Admin' for page title!"

            if browser.lower() == "firefox":
                print("Running against Firefox browser...")
                options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Firefox(
                    executable_path="/usr/local/bin/geckodriver", options=options
                )
                self.driver.get(self.url)
                self.driver.implicitly_wait(self.max_browser_wait)
                pagetitle = self.driver.title
                print("Login Page title: {}".format(pagetitle))
                assert page_title == "CS-Admin", "Expected 'CS-Admin' for page title!"

            if browser.lower() not in ["chrome", "firefox"]:
                raise Exception(
                    "Browser: {} is currently not supported!".format(browser)
                )
        except RuntimeError as error:
            raise RuntimeError("Failure to access URL: {}".format(url)) from error

    @staticmethod
    def get_date_time():
        """Method: get_date_time"""
        timestamp = time.strftime("%m%d%Y%H%M%S")
        return timestamp

    def enter_text(self, myobject, myinput):
        """Method: enter_text
        :type myobject: string
        :param myobject: the proper CSS Selector

        :type myinput: string
        :param myinput: the string value to be entered
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, myobject))
            )
            element.send_keys(str(myinput))
        except Exception as error:
            raise Exception(f"Failed to enter text in element: {myobject}") from error

    def click_element(self, theobject, pause=0):
        """Method: click_element
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        :type pause: int
        :param pause: this is delay in seconds after clicking element
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            element.click()
            time.sleep(pause)
        except Exception as error:
            raise Exception(f"Failed to click element: {theobject} due to: {error}")

    def element_present(self, theobject):
        """Method: element_present
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            if not element.is_displayed():
                raise Exception(f"Expected element: {theobject} to be displayed!")
            return True
        except Exception as error:
            raise Exception(
                f"Failed to verify element is present: {theobject}"
            ) from error

    def element_not_present(self, theobject):
        """Method: element_not_present
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return True
        except Exception as error:
            raise Exception(f"Element not present as expected due to: {error}")

    def get_text(self, theobject):
        """Method: get_text
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.text
        except Exception as error:
            raise Exception(f"Failed get text: {theobject} due to: {error}")

    def get_inner_text(self, theobject):
        """Method: get_inner_text
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("innerHTML")
        except Exception as error:
            raise Exception(f"Failed get inner text: {theobject} due to: {error}")

    def get_class_attribute(self, theobject):
        """Method: get_class_attribute
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("class")
        except Exception as error:
            raise Exception(f"Failed get class: {theobject} due to: {error}")

    def get_input_value(self, theobject):
        """Method: get_input_value
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("value")
        except Exception as error:
            raise Exception(f"Failed get input value: {theobject} due to: {error}")

    def return_object_list(self, objects):
        """Method: get_object_list
        :type objects: string
        :param objects: the CSS Selector for the list of page objects
        """
        try:
            lst_objects = self.driver.find_elements(By.CSS_SELECTOR, objects)
            return lst_objects
        except Exception as error:
            raise Exception(f"Failed to return object list: {objects} due to: {error}")

    def generate_screenshot(self, error_file_name):
        """Method: generate_screenshot
        :type error_file_name: string
        :param error_file_name: this is the file name
        """
        screenshot = str(error_file_name) + "_" + self.get_date_time() + ".png"
        self.driver.save_screenshot(screenshot)
        print(f"Generated screenshot: {screenshot}")
        logger.info(
            "<img src='" + str(screenshot) + "' width='1400' height='900'/>", html=True
        )

    def clear_field(self, field):
        """Method: clear_field
        :type field: string
        :param field: the proper CSS Selector
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, field))
            )
            text = element.text
            print(f"Got text field data: {text}")
            print(f"Total string length: {len(text)}")
            if text != "":
                i = 0
                while i <= len(text):
                    element.send_keys(Keys.BACK_SPACE)
                    i += 1
        except Exception as error:
            raise Exception(f"Failed to clear field: {field} due to: {error}")

    @staticmethod
    def pause(delay=1):
        """Method: pause
        :type delay: int
        :param delay: for pausing test execution
        """
        time.sleep(delay)

    def send_arrow_down_enter_key(self, elem):
        """Method: send_arrow_down_enter_key
        :type elem: WebDriver Element
        :param elem: The locator for the element on the web
        :type keys: keyboard Keys.ARROW_DOWN + Keys.ENTER
        :param keys: Keys that user wants to send. ex Keys.ENTER
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, elem))
            )
            element.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        except Exception as error:
            raise Exception(
                f"Failed to send ARROW_DOWN and ENTER key on element: {elem} due to: {error}"
            )

    def send_end_key(self, elem, keys):
        """Method: send_end_key
        :type elem: WebDriver Element
        :param elem: The locator for the element on the web
        :type keys: keyboard.END.keys
        :param keys: Keys that user wants to send. ex Keys.ENTER
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, elem))
            )
            element.send_keys(Keys.PAGE_DOWN)
        except Exception as error:
            raise Exception(
                f"Failed to send keys {keys} in element: {elem} due to: {error}"
            )
