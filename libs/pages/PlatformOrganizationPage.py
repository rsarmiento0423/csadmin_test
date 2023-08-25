""" PlatformOrganizationPage.py """
import inspect
from PlatformLoginPage import PlatformLoginPage


class PlatformOrganizationPage(PlatformLoginPage):
    """Class: PlatformOrganizationPage"""

    organization_header = (
        "header > div > div.MuiTypography-root.MuiTypography-h6.css-1a3lqbo"
    )
    new_organization_header = '[data-test-id="new-organization-modal-title"], [data-test-id="UploadLocations-Heading"]'
    org_name = '[class="MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq"]'
    org_language = "#mui-component-select-language"
    admin_notes_btn = "div.css-4sd2fs > button"
    products_btn = "div:nth-child(4) > div > div > div > div > button"
    cancel_btn = "button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary.MuiButton-sizeMedium.MuiButton-outlinedSizeMedium.css-79xub"
    create_btn = '[data-test-id="new-organization-modal-create-button"], [data-test-id="CreateOrganization-Btn"]'
    name_required_error = "#root > div > div > div > div > label"
    first_organization = "table > tbody > tr:nth-child(1)"
    admin_notes = '[data-test-id="OrgAdminNotes-Input"]'
    profile_header = "table > thead > tr > th:nth-child(3)"
    update_button = '[data-test-id="OrgUpdate-Btn"]'

    def verify_organization_elements_exists(self):
        """Method: verify_organization_elements_exists"""
        try:
            test = inspect.stack()[0][3]
            header = self.get_text(self.organization_header)
            print(f"Got header: {header}")
            profile = self.get_text(self.profile_header)
            print(f"Got Profile header: {profile}")
            assert header == "Organizations", "Wrong header found!"
            assert profile == "Profile", "Profile column missing!"
            assert (
                self.element_present(self.organizations_tab) is True
            ), "Missing Organization tab!"
            assert (
                self.element_present(self.add_organization_btn) is True
            ), "Missing Organization button!"
            assert self.element_present(self.audit_tab) is True, "Missing Audit tab!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_add_organization(self):
        """Method: click_add_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.add_organization_btn)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def verify_new_org_elements_exists(self):
        """Method: verify_new_org_elements_exists"""
        try:
            test = inspect.stack()[0][3]
            header = self.get_text(self.new_organization_header)
            print(f"Got header: {header}")
            assert header == "New Organization", "Wrong header found!"
            assert (
                self.element_present(self.admin_notes_btn) is True
            ), "Missing Admin Notes button!"
            assert (
                self.element_present(self.products_btn) is True
            ), "Missing Products button!"
            assert (
                self.element_present(self.cancel_btn) is True
            ), "Missing Cancel button!"
            assert (
                self.element_present(self.create_btn) is True
            ), "Missing Create button!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_cancel_from_new_organization(self):
        """Method: click_cancel_from_new_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.cancel_btn)
            self.pause(1)
            assert (
                self.element_not_present(self.org_name) is True
            ), "Found New Organization page!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_create_from_new_organization(self):
        """Method: click_create_from_new_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.create_btn)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def verify_name_required(self):
        """Method: verify_name_required"""
        try:
            test = inspect.stack()[0][3]
            error = self.get_text(self.name_required_error)
            assert error == "Name is required", "Wrong error displayed!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def enter_organization_name(self):
        """Method: enter_organization_name"""
        try:
            test = inspect.stack()[0][3]
            self.enter_text(self.org_name, "test organization")
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_first_organization(self):
        """Method: click_first_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.first_organization, 1)
            assert (
                self.element_present(self.admin_notes) is True
            ), "Admin Notes not present!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def get_admin_notes(self):
        """Method: get_admin_notes"""
        try:
            test = inspect.stack()[0][3]
            notes = self.get_text(self.admin_notes)
            print(f"Got Admin Notes: {notes}")
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def update_admin_notes(self):
        """Method: update_admin_notes"""
        try:
            test = inspect.stack()[0][3]
            self.clear_field(self.admin_notes)
            self.enter_text(self.admin_notes, "Updating admin notes for QA test!")
            self.click_element(self.update_button, 3)
            self.get_admin_notes()
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
