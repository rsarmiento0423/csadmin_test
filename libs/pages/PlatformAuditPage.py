""" PlatformAuditPage.py """
import inspect
from PlatformLoginPage import PlatformLoginPage


class PlatformAuditPage(PlatformLoginPage):
    """ Class: PlatformAuditPage """
    originator_user = '#mui-13'
    target_user = '#mui-14'
    target_organizations = '#byOrganization'
    actions = '#byAction'
    from_date = '#mui-19'
    to_date = '#mui-20'
    search_btn = 'div:nth-child(4) > div > button'
    table_header_row = 'table > thead > tr'
    table_data_rows = 'tbody > tr'

    def verify_audit_elements_exists(self):
        """ Method: verify_audit_elements_exists """
        try:
            test = inspect.stack()[0][3]
            assert self.element_present(self.audit_tab) is True, "Missing Audit tab!"
            assert self.element_not_present(self.originator_user) is True, "'Originator User' enabled!"
            assert self.element_not_present(self.target_user) is True, "'Target User' enabled!"
            assert self.element_present(self.target_organizations) is True, "Missing 'Target Organizations'!"
            assert self.element_present(self.actions) is True, "Missing Actions!"
            assert self.element_not_present(self.from_date) is True, "'From Date' enabled!"
            assert self.element_not_present(self.to_date) is True, "'To Date' enabled!"
            assert self.element_present(self.search_btn) is True, "Missing Search button!"
            assert self.element_present(self.table_header_row) is True, "Missing table header!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_search_btn(self):
        """ Method: click_search_btn """
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.search_btn)
            self.pause(3)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def verify_search_rows_returned(self):
        """ Method: verify_search_rows_returned"""
        try:
            test = inspect.stack()[0][3]
            total = len(self.return_object_list(self.table_data_rows))
            print(f"Total search results returned: {total}")
            assert total > 0, "No search results returned!"
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
