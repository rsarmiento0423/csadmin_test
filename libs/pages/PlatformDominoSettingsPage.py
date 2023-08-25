""" PlatformDominoSettingsPage.py """
import inspect
from PlatformLoginPage import PlatformLoginPage


class PlatformDominoSettingsPage(PlatformLoginPage):
    """ Class: PlatformDominoSettingsPage """
    domino_settings_header = 'header > div > div.MuiTypography-root.MuiTypography-h6.css-1a3lqbo'
    missing_buildings_request_tab = '#simple-tab-0'
    upload_locations_tab = '#simple-tab-1'
    missing_buildings_requests_header = 'table > thead > tr'
    missing_buildings_requests_data = 'table > tbody > tr'
    search_upload_locations_btn = 'div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-2.css-o0rlmm > div > button'
    upload_locations_title = '[data-test-id="new-organization-modal-title"], [data-test-id="UploadLocations-Heading"]'
    upload_locations_header = 'table > thead > tr'
    upload_locations_data = 'table > tbody > tr'

    def click_upload_locations_tab(self):
        """ Method: click_upload_locations_tab """
        try:
            test = inspect.stack()[0][3]
            self.click_domino_settings()
            self.click_element(self.upload_locations_tab)
            assert self.element_present(self.upload_locations_title) is True, "Missing Upload Locations title!"
            assert self.element_present(self.upload_locations_header) is True, "Missing Upload Locations header!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_search_upload_locations(self):
        """ Method: click_search_upload_locations """
        try:
            test = inspect.stack()[0][3]
            self.click_domino_settings()
            self.click_element(self.search_upload_locations_btn)
            self.pause(3)
            assert self.element_present(self.upload_locations_data) is True, "Missing Upload Locations data!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_missing_buildings_requests_tab(self):
        """ Method: click_missing_buildings_requests_tab """
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.missing_buildings_request_tab)
            assert self.element_present(self.missing_buildings_requests_header) is True, "Missing Buildings Requests header!"
            assert self.element_present(self.missing_buildings_requests_data) is True, "Missing Buildings Requests data!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
