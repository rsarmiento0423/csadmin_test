""" PlatformLoginPage.py """
import inspect
from CommonLibrary import CommonLibrary
from selenium.webdriver.common.by import By


class PlatformLoginPage(CommonLibrary):
    """Class: PlatformLoginPage"""

    login_frame = "login-iframe"
    username_txt = "#username"
    password_txt = "#password"
    login_button = "#kc-login"
    remember_me_checkbox = "#rememberMe"
    forget_password_link = "#kc-forgot-pword-link"
    menu_icon = '[data-testid="MenuIcon"]'
    organizations_tab = "#simple-tab-0"
    audit_tab = "#simple-tab-1"
    domino_settings = (
        "li:nth-child(2) > div > div.MuiListItemText-root.css-1tsvksn > span"
    )
    logout_button = "ul:nth-child(3) > li > div"
    invalid_credentials = (
        'div[class="alert alert-error"] span[class="c-snackbar--error"]'
    )
    reset_password_header = 'h2[class="kc-page-title"]'
    login_access_denied = "#simple-tabpanel-0 > div > p > div"
    add_organization_btn = '[data-test-id="new-organization-modal-open-button"], [data-test-id="CreateOrganization-Btn"]'
    profile_table_header = "table > thead > tr > th:nth-child(3)"
    name_table_header = "table > thead > tr > th:nth-child(2)"
    id_table_header = "table > thead > tr > th:nth-child(1)"

    def log_in(self, username, password):
        """Method: log_in"""
        try:
            test = inspect.stack()[0][3]
            username = str(self.data[username])
            password = str(self.data[password])

            browsername = self.driver.capabilities["browserName"]
            browserversion = self.driver.capabilities["browserVersion"]
            print(f"Browser: {browsername}")
            print(f"Version: {browserversion}")
            print("Logging into Platform as: {}".format(username))
            self.driver.switch_to.frame(PlatformLoginPage.login_frame)
            self.clear_field(PlatformLoginPage.username_txt)
            self.enter_text(PlatformLoginPage.username_txt, username)
            self.enter_text(PlatformLoginPage.password_txt, password)
            self.click_element(PlatformLoginPage.remember_me_checkbox)
            self.click_element(PlatformLoginPage.login_button)
            handles = self.driver.window_handles
            size = len(handles)
            for num in range(size):
                self.driver.switch_to.window(handles[num])
            assert self.element_present(
                PlatformLoginPage.add_organization_btn
            ), "Unable to log into Platform!"
            table_profile_header = self.get_text(self.profile_table_header)
            table_name_header = self.get_text(self.name_table_header)
            table_id_header = self.get_text(self.id_table_header)
            assert table_profile_header == "Profile", "Missing 'Profile' table header!"
            assert table_name_header == "Name", "Missing 'Name' table header!"
            assert table_id_header == "Id", "Missing 'Id' table header!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Fail to log into Platform due to: {error}!")

    def login_negative(self, username, password):
        """login_negative"""
        try:
            test = inspect.stack()[0][3]
            print("Logging into Platform as: {}".format(username))
            self.driver.switch_to.frame(PlatformLoginPage.login_frame)
            if username != "blank":
                self.enter_text(PlatformLoginPage.username_txt, username)
            if password != "blank":
                self.enter_text(PlatformLoginPage.password_txt, password)
            self.click_element(PlatformLoginPage.remember_me_checkbox)
            self.click_element(PlatformLoginPage.login_button)
            error_message = self.get_text(PlatformLoginPage.invalid_credentials)
            print("Got error: {}".format(error_message))
            assert (
                error_message == "Invalid credentials"
            ), "Wrong error message displayed!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(
                f"Fail to login negative Platform test due to: {error}!"
            )

    def login_with_no_permission(self, username, password):
        """Method: login_with_no_permission"""
        try:
            test = inspect.stack()[0][3]
            username = str(self.data[username])
            password = str(self.data[password])

            print("Logging into Ready as: {}".format(username))
            self.driver.switch_to.frame(PlatformLoginPage.login_frame)
            self.clear_field(PlatformLoginPage.username_txt)
            self.enter_text(PlatformLoginPage.username_txt, username)
            self.enter_text(PlatformLoginPage.password_txt, password)
            self.click_element(PlatformLoginPage.remember_me_checkbox)
            self.click_element(PlatformLoginPage.login_button, 5)
            access_denied_error = self.driver.find_element(
                By.CSS_SELECTOR, PlatformLoginPage.login_access_denied
            ).text
            print("Got login access denied error: {}".format(access_denied_error))
            assert (
                access_denied_error == "Error: 403 Forbidden (admin role required)"
            ), "Wrong error message displayed!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(
                f"Fail to get login access denied permission error due to: {error}!"
            )

    def log_out(self):
        """Method: log_out"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(PlatformLoginPage.menu_icon)
            self.click_element(PlatformLoginPage.logout_button)
            print(f"PASS: {test}")
            print("Logged out from CSAdmin!")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Fail to log out from Platform due to: {error}!")

    def click_forgot_password(self):
        """Method: click_forgot_password"""
        try:
            test = inspect.stack()[0][3]
            self.driver.switch_to.frame(PlatformLoginPage.login_frame)
            self.click_element(PlatformLoginPage.forget_password_link)
            actual_header = self.get_text(PlatformLoginPage.reset_password_header)
            print("Got header: {}".format(actual_header))
            assert actual_header == "Reset password", "Expected: 'Reset password'"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(
                f"Fail to click 'Forgot password' link due to: {error}!"
            )

    def navigate_to_url(self, url):
        """Method: navigate_to_url"""
        try:
            test = inspect.stack()[0][3]
            print(f"Navigating to URL: {url}...")
            if "staging" in url:
                print("Setting to EN locale!")
                locale = "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en"
                self.driver.get(locale)
            self.driver.get(url)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Fail to navigate to the URL: {url} due to: {error}!")

    def click_menu(self):
        """Method: click_menu"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.menu_icon)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_domino_settings(self):
        """Method: click_domino_settings"""
        try:
            test = inspect.stack()[0][3]
            self.click_menu()
            self.click_element(self.domino_settings)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_organizations_tab(self):
        """Method: click_organizations_tab"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.click_organizations_tab())
            print(f"PASS: {test}")
            self.pause(3)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_audit_tab(self):
        """Method: click_audit_tab"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.audit_tab)
            print(f"PASS: {test}")
            self.pause(3)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
