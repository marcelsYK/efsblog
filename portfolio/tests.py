# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class Selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_selenium(self):
        driver = self.driver
        driver.get(self.base_url + "/home/")

        driver.find_element_by_css_selector("a.btn.btn-primary").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("instructor")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("instructor1a")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Edit").click()
        driver.find_element_by_id("id_state").clear()
        driver.find_element_by_id("id_state").send_keys("NE")
        self.assertEqual("Edit Customer", driver.find_element_by_css_selector("h1").text)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertEqual("Katherine McClusky", driver.find_element_by_xpath(
            "//body[@id='app-layout']/div/div/div/div[3]/table/tbody/tr/td[2]").text)
        driver.find_element_by_link_text("Portfolio").click()
        for i in range(60):
            try:
                if "Mutual Funds Information" == driver.find_element_by_xpath("//div[3]/h2").text: break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()
