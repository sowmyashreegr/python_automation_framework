import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest


class Test_GuidedRenewalGeneral3(BaseTest):
    # @pytest.mark.guided_renewal_general_three
    def test_automate_filpkart(self):
        a=4
        b=5
        c=a+b
        print(c)
        login_page = LoginPage(self.driver)
        login_page.goto()
        login_page.create_new_account()

    def test_pranali(self):
        login_page = LoginPage(self.driver)
        login_page.goto()
        login_page.create_new_account()


