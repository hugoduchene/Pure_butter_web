from selenium import webdriver
from substitute.models import Categories, Products, User_record
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model


class TestProjectPage(StaticLiveServerTestCase):

    def setUp(self):
        self.User = get_user_model()
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')
        self.index_url = self.live_server_url + reverse('index')
        self.result_url = self.live_server_url + reverse('result')
        self.registrer_url = self.live_server_url + reverse('registration')
        self.login_url = self.live_server_url + reverse('login')
        self.account_url = self.live_server_url + reverse('account')
        self.food_url = self.live_server_url + reverse('myfood')

    def test_click_account(self):
        self.browser.get(self.index_url)
        self.browser.find_element_by_id('icon_menu').click()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('id_account').click()
        self.assertEquals(
            self.browser.current_url,
            self.registrer_url
        )
        self.browser.close()

    def test_click_logout(self):
        self.browser.get(self.index_url)
        self.browser.find_element_by_id('icon_menu').click()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('id_logout').click()
        self.assertEquals(
            self.browser.current_url,
            self.registrer_url
        )
        self.browser.close()

    def test_click_myfood(self):
        self.browser.get(self.index_url)
        self.browser.find_element_by_id('icon_menu').click()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('id_food').click()
        self.assertEquals(
            self.browser.current_url,
            self.registrer_url
        )
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        self.browser.close()


    def test_no_projects_alert_button_redirects_to_index_page(self):
        index_url = self.live_server_url + reverse('index')
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url,
            index_url
        )
        self.browser.close()

    def test_user_redirected(self):
        self.browser.get(self.index_url)
        self.browser.find_element_by_class_name('test_button')
        self.assertEquals(
            self.browser.current_url,
            self.index_url
        )
        self.browser.close()

    def test_search(self):
        self.browser.get(self.index_url)
        element = self.browser.find_element_by_id('SearchSubstitute')
        element.send_keys('nutella')
        element.submit()
        self.assertEquals(
            self.browser.current_url,
            self.index_url
        )
        self.browser.close()

    def test_registrer(self):
        self.browser.get(self.registrer_url)
        element = self.browser.find_element_by_id('form_registrer')
        element_username = self.browser.find_element_by_id('id_username')
        element_username.send_keys('jk')
        element_email = self.browser.find_element_by_id('id_email')
        element_email.send_keys('h@g.com')
        element_password1 = self.browser.find_element_by_id('id_password1')
        element_password1.send_keys('mlkjhg1234')
        element_password2 = self.browser.find_element_by_id('id_password2')
        element_password2.send_keys('mlkjhg1234')
        element.submit()
        self.assertEquals(
            self.browser.current_url,
            self.index_url
        )
        self.browser.close()
