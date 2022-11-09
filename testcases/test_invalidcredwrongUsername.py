# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInvalidcredwrongUsername():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def logintest(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1317, 741)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys(self.vars["username"])
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys(self.vars["pwd"])
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    [object Object]
  
  def test_invalidcredwrongUsername(self):
    self.vars["username"] = "wrong_user_3"
    self.vars["pwd"] = "testpwd3"
    self.logintest()
  
