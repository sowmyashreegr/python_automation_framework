from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from database_connections import organizations
from pages.base_page import BasePage
# from pages.organization.organization_page import OrganizationPage
# from pages.sys_admin.sys_admin_change_password_page import SysAdminChangePasswordPage
# from pages.sys_admin.sys_admin_my_account_page import SysAdminMyAccountPage
# from utils import database_helpers


class LoginPage(BasePage):
    # region Locators
    USERNAME_FIELD = By.ID, "user_name"
    PASSWORD_FIELD = By.ID, "password"
    LOGIN_BUTTON_ELEMENT = By.ID, "logon_submit"
    NEED_HELP_EL = By.XPATH, '//*[@id="need_help_link"]'

    LOGIN_FAILED_ALERT = By.XPATH, "//span[@class='mt-2 message text-danger auth-alert-msg']"

    # Forgot Password section
    FORGOT_PASSWORD_FIELD = By.XPATH, "//*[@id='main_login']/div/div[3]/a"
    FORGOT_PASSWORD_USERNAME_FIELD = By.ID, "pass_username"
    EMAIL_FIELD = By.ID, "email_address"
    NEW_PASSWORD_FIELD = By.ID, "new_password"
    OLD_PASSWORD_FIELD = By.ID, "old_password"
    CONFIRM_PASSWORD_FIELD = By.ID, "confirm_password"
    SAVE_BUTTON = By.XPATH, "//button[text()='Save']"
    CHANGE_PASSWORD_BTN = By.ID, "change_passwordBtn"
    MOBILE_CHANGE_PASSWORD_BUTTON = By.ID, "saveBtn"

    UPDATE_CONTACT_INFO_SAVE_FIELD = By.XPATH, "//button[text()='Save']"
    CURRENT_PASSWORD_FIELD = By.ID, "cpassword"
    RETYPE_NEW_PASSWORD_FIELD = By.ID, "n2password"
    NEW_CHANGED_PASSWORD_FIELD = By.ID, "n1password"

    MFA_MESSAGE_FIELD = By.ID, "mfa_access_code"
    MFA_LOGIN_BUTTON = By.XPATH, "//input[@type='submit' and @value='Login']"

    PAGE_TITLE = By.XPATH, "//title"
    FORGOT_PASSWORD_LINK = By.ID, "forgot_password_link"
    ALERT_MESSAGE_EL = By.XPATH, "//div[@class='col alert-content']"

    # Need Help Workflows
    FORGOT_UN_RADIO_BUTTON = By.ID, "admin_username_option"
    FORGOT_PW_RADIO_BUTTON = By.ID, "admin_password_option"
    CONTINUE_BUTTON = By.ID, "admin_form_submit"
    EMAIL_TEXT_BOX = By.ID, "admin_email"
    USERNAME_TEXT_BOX = By.ID, "admin_username"

    NEW_PW_TEXT_BOX = By.ID, "n1password"
    VERIFY_PW_TEXT_BOX = By.ID, "n2password"
    CHANGE_PW_BUTTON = By.ID, "change_passwordBtn"
    USERNAME_LABEL = By.XPATH, "//span[contains(@class, 'user-name')]"

    FORGOT_USERNAME_RADIO_BUTTON = By.ID, "forgot_uname"
    FORGOT_PASSWORD_RADIO_BUTTON = By.XPATH, "//input[@id='forgot_password']"
    LAST_NAME_TEXT_BOX = By.ID, "last_name"
    DOB_TEXT_BOX = By.ID, "dob"
    SSN_TEXT_BOX = By.ID, "ssn"
    USER_NAME_TEXT_BOX = By.ID, "pass_username"
    ADMIN_USER_NAME_TEXT_BOX = By.ID, "admin_username"
    SUBMIT_FORM = By.ID, "submitForm"
    INVALID_SSN_EL = By.ID, "ssn_validation"

    EMP_CREDENTIALS_RETRIEVAL_RADIO_BUTTON = By.ID, "employee_selection"
    ADMIN_CREDENTIALS_RETRIEVAL_RADIO_BUTTON = By.ID, "admin_selection"
    NEED_HELP_CONTINUE_BUTTON = By.ID, "continue"

    # hcm dashboard login
    HCM_DASHBOARD_USERNAME = By.ID, "txtUserEmail"
    HCM_DASHBOARD_PASSWORD = By.ID, "txtUserPassword"
    HCM_DASHBOARD_SUBMIT = By.XPATH, "//button[@type='submit']"
    # endregion Locators

    # page class constructor

    def __init__(self, driver, title="Flipkart Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['facebook']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    def goto_with_org_code(self, org_code, reuse_username=False, custom_login=False):
        if reuse_username and custom_login:
            self.goto_page(f"{self.url}/logon/{org_code}/?{org_code}")
        elif custom_login:
            self.goto_page(f"{self.url}/logon/?{org_code}")
        else:
            self.goto_page(f"{self.url}/logon/{org_code}")

    def username(self, value):
        self.fill_out_text_field(self.USERNAME_FIELD, value)

    def get_username_text(self):
        return self.get_text_field_text(self.USERNAME_FIELD)

    def password(self, value):
        self.fill_out_text_field(self.PASSWORD_FIELD, value)

    def login_button(self, ajax=True):
        timing = self.click_element(self.LOGIN_BUTTON_ELEMENT, ajax=ajax)
        return timing

    def click_need_help_link(self):
        self.click_element(self.NEED_HELP_EL)

    def get_alert_message(self):
        return self.get_element_text(self.ALERT_MESSAGE_EL)

    def forgot_password(self):
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def forgot_password_username(self, value):
        self.fill_out_text_field(self.FORGOT_PASSWORD_USERNAME_FIELD, value)

    def email(self, value):
        self.fill_out_text_field(self.EMAIL_FIELD, value)

    def new_password_button(self):
        self.click_element(self.NEW_PASSWORD_FIELD)

    def old_password(self, value):
        self.fill_out_text_field(self.OLD_PASSWORD_FIELD, value)

    def new_password(self, value):
        self.fill_out_text_field(self.NEW_PASSWORD_FIELD, value)

    def confirm_password(self, value):
        self.fill_out_text_field(self.CONFIRM_PASSWORD_FIELD, value)

    def save(self):
        self.click_element(self.SAVE_BUTTON)

    def username_hcm_dashboard(self, value):
        self.fill_out_text_field(self.HCM_DASHBOARD_USERNAME, value)

    def password_hcm_dashboard(self, value):
        self.fill_out_text_field(self.HCM_DASHBOARD_PASSWORD, value)

    def submit_hcm_dashboard(self):
        self.click_element(self.HCM_DASHBOARD_SUBMIT, ajax=False)

    # todo add alert check to the click element function
    def update_contact_info_save(self):
        self.click_element(self.UPDATE_CONTACT_INFO_SAVE_FIELD)

    def current_password(self, value):
        self.fill_out_text_field(self.CURRENT_PASSWORD_FIELD, value)

    def retype_new_password(self, value):
        self.fill_out_text_field(self.RETYPE_NEW_PASSWORD_FIELD, value)

