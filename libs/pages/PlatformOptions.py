""" PlatformOptions.py """
import inspect
from PlatformLoginPage import PlatformLoginPage


class PlatformOptions(PlatformLoginPage):
    """Class: PlatformOptions"""

    qa_test_org = '[data-test-id="Organization-/a-smoke-csadmin-org"]'
    users_tab = '[data-test-id="organization-details-tab-users"]'
    move_test_org = '[data-test-id="Organization-/a-move-org"]'
    smoke_tester1_user_options_btn = "table > tbody > tr > td:nth-child(7) > button"
    menu_option_list = 'ul > li[role="menuitem"]'
    disable_enable_option = "ul > li:nth-child(1)"
    remove_set_org_admin_option = "ul > li:nth-child(2)"
    resend_invite_option = "ul > li:nth-child(3)"
    change_organization_option = "ul > li:nth-child(4)"
    change_organization_modal_title = "#modal-modal-title"
    organizations_input = '[data-test-id="Organizations-Input"], [role="combobox"]'
    change_organization_btn = 'div[class="css-av3g5w"] > button:nth-child(2)'
    cancel_organization_btn = 'div[class="css-av3g5w"] > button:nth-child(1)'
    clear_org = "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-1wnsr1i > div.MuiGrid-root.MuiGrid-container.css-zlmj8 > div > div > div > div > div > div > button > svg"
    main_menu = "div > header > div > div:nth-child(1) > button"
    organization_menu = "ul:nth-child(1) > li:nth-child(1) > div > div.MuiListItemText-root.css-1tsvksn > span"

    def select_qa_test_organization(self):
        """Method: select_qa_test_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.qa_test_org)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def select_move_test_organization(self):
        """Method: select_move_test_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.move_test_org, 3)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_users_tab(self):
        """Method: click_users_tab"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.users_tab)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def choose_user_option(self):
        """Method: choose_user_option"""
        try:
            test = inspect.stack()[0][3]
            assert self.element_present(
                self.smoke_tester1_user_options_btn
            ), "Missing User!"
            self.click_element(self.smoke_tester1_user_options_btn, 3)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def verify_options(self):
        """Method: verify_options"""
        try:
            test = inspect.stack()[0][3]
            assert self.element_present(self.menu_option_list), "Missing Options list!"
            # Get list of menu options
            lst_actual_menu_items = []
            menuitems = self.return_object_list(self.menu_option_list)
            for menu in menuitems:
                print(menu.text)
                lst_actual_menu_items.append(menu.text)
            assert len(lst_actual_menu_items) == 4, "Wrong number of options displayed!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def select_disable_enable_option(self):
        """Method: select_disable_enable_option"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.disable_enable_option, 3)
            assert self.element_present(
                self.smoke_tester1_user_options_btn
            ), "Missing User!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def select_remove_set_org_admin_option(self):
        """Method: select_remove_set_org_admin_option"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.remove_set_org_admin_option, 3)
            assert self.element_present(
                self.smoke_tester1_user_options_btn
            ), "Missing User!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def select_resend_invite_option(self):
        """Method: select_resend_invite_option"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.resend_invite_option, 3)
            assert self.element_present(
                self.smoke_tester1_user_options_btn
            ), "Missing User!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def select_change_organization_option(self, org):
        """Method: select_change_organization_option"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.change_organization_option)
            self.click_element(self.organizations_input)
            self.click_element(self.clear_org)
            self.enter_text(self.organizations_input, org)
            self.send_arrow_down_enter_key(self.organizations_input)
            new_org = self.get_input_value(self.organizations_input)
            print(f"New organization: {new_org}")
            assert new_org == org, f"Expected organization: {org}"
            self.click_element(self.change_organization_btn, 5)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def cancel_change_organization_option(self):
        """Method: cancel_change_organization_option"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.change_organization_option)
            old_org = self.get_input_value(self.organizations_input)
            print(f"Previous organization: {old_org}")
            assert self.element_present(
                self.cancel_organization_btn
            ), "Missing Cancel button for change organization!"
            self.click_element(self.cancel_organization_btn)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def navigate_to_organization(self):
        """Method: navigate_to_organization"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.main_menu)
            self.click_element(self.organization_menu)
            self.pause(3)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")
