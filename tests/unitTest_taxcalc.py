import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestTaxCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tax_calculation(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/")
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000/tax-calculator/")
        time.sleep(1)

        driver.find_element(By.NAME, "income").send_keys("50000")
        driver.find_element(By.NAME, "tax_rate").send_keys("10")
        time.sleep(1)

        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)

        headers = driver.find_elements(By.TAG_NAME, "h2")
        result_found = False
        for header in headers:
            if "Tax Amount" in header.text:
                result_found = True
                print("Tax calculation successful: ", header.text)
                break

        self.assertTrue(result_found, "Tax result not found on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
