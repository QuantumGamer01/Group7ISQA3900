import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestBudgetPageAccess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_budget_page_access(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/")
        driver.maximize_window()

        driver.find_element(By.ID, "id_username").send_keys("testuser")
        driver.find_element(By.ID, "id_password").send_keys("test123")
        driver.find_element(By.ID, "id_password").send_keys(Keys.RETURN)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/advanced-budget/")
        time.sleep(3)

        heading = driver.find_element(By.TAG_NAME, "h1").text.lower()
        self.assertIn("budget", heading, "Budget page not loaded correctly.")

    def tearDown(self):
        self.driver.quit()
