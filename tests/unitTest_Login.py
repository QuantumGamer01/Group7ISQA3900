import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/")
        driver.maximize_window()

        driver.find_element(By.ID, "id_username").send_keys("testuser")
        driver.find_element(By.ID, "id_password").send_keys("test123")
        time.sleep(2)
        driver.find_element(By.ID, "id_password").send_keys(Keys.RETURN)

        time.sleep(3)
        self.assertNotIn("login", driver.current_url.lower(), "Login may have failed.")

    def tearDown(self):
        self.driver.quit()
