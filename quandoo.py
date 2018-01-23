from selenium import webdriver
from pages.quandoologin import QuandooLogin
from pages.quandoohovers import QuandooHovers
from pages.quandootables import QuandooTables
import unittest
import random

class TestQuandoo(unittest.TestCase):

    def setUp(self):
        # This is just to demonstrate that browser type can be varied
        # (actual mechanism for varying not addressed here)
        browser = random.choice(['firefox','chrome'])
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

    def test_login_successs(self):
        """ Test correct message shown following valid user credentials
        """
        # Go to http://the-internet.herokuapp.com/login
        self.driver.get("http://the-internet.herokuapp.com/login")
        quandoo_login = QuandooLogin(self.driver)

        # Fill in valid user credentials 
        quandoo_login.input_username("tomsmith")
        quandoo_login.input_password("SuperSecretPassword!")
        quandoo_login.click_login()

        # Verify that "You logged into a secure area" is displayed
        self.assertTrue(quandoo_login.is_login_message_shown(
            "You logged into a secure area"))

    def test_login_invalid_username(self):
        """ Test correct message shown following invalid username
        """
        # Go to http://the-internet.herokuapp.com/login
        self.driver.get("http://the-internet.herokuapp.com/login")
        quandoo_login = QuandooLogin(self.driver)

        # Fill in invalid username, valid password 
        quandoo_login.input_username("nottomsmith")
        quandoo_login.input_password("SuperSecretPassword!")
        quandoo_login.click_login()

        # Verify that "Your username is invalid" is displayed
        self.assertTrue(quandoo_login.is_login_message_shown(
            "Your username is invalid"))

    def test_login_invalid_password(self):
        """ Test correct message shown following invalid password
        """
        # Go to http://the-internet.herokuapp.com/login
        self.driver.get("http://the-internet.herokuapp.com/login")
        quandoo_login = QuandooLogin(self.driver)

        # Fill in valid username, invalid password 
        quandoo_login.input_username("tomsmith")
        quandoo_login.input_password("notSuperSecretPassword!")
        quandoo_login.click_login()

        # Verify that "Your password is invalid" is displayed
        self.assertTrue(quandoo_login.is_login_message_shown(
            "Your password is invalid"))

    def test_hovers(self):
        """ Test correct usernames shown during hovers
        """
        # Go to http://the-internet.herokuapp.com/hovers
        self.driver.get("http://the-internet.herokuapp.com/hovers")
        quandoo_hovers = QuandooHovers(self.driver)

        # Hover over each avatar and check that correct username shown
        for x in range(1, quandoo_hovers.get_number_avatars()):
            quandoo_hovers.hover(x)
            self.assertTrue(quandoo_hovers.is_username_shown(x))

    def test_tables(self):
        """ Test tables sorted correctly
        """
        # Go to http://the-internet.herokuapp.com/tables
        self.driver.get("http://the-internet.herokuapp.com/tables")
        quandoo_tables = QuandooTables(self.driver)

        # Sort table 2 by "Last Name" ascending and check sorted correctly
        quandoo_tables.click_column_heading("Example 2", "Last Name")
        last_names = quandoo_tables.get_column_values("Example 2", "Last Name")
        sorted_last_names = last_names
        sorted_last_names.sort()
        self.assertEqual(last_names, sorted_last_names)

        # Sort table 2 by "Last Name" descending and check sorted correctly
        quandoo_tables.click_column_heading("Example 2", "Last Name")
        last_names = quandoo_tables.get_column_values("Example 2", "Last Name")
        sorted_last_names.sort(reverse=True)
        self.assertEqual(last_names, sorted_last_names)
                               
    def tearDown(self):
        self.driver.close()
        


