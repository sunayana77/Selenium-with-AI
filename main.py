from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from model import Model
from credentials import Credentials
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False


url = "https://accounts.lambdatest.com/login"
# url = "https://test.io"
service = Service("/usr/bin/chromedriver")


driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.maximize_window()
self_healing_model = Model()
email, password = Credentials.get_credentials()



def EnterUserName(driver):
    try:
        element_email = driver.find_element(By.XPATH, "//input[@name='email']")
    except NoSuchElementException as e:
        element_email = self_healing_model.InvokeSelfHealing(e, driver, "//input[@name='email']")
    element_email.send_keys(email)
    print("Enter username executed.")


def EnterPassword(driver):
    try:
        element_password = driver.find_element(By.XPATH, "//input[@name='password']")
    except NoSuchElementException as e:
        element_password = self_healing_model.InvokeSelfHealing(e, driver, "//input[@name='password']")
    element_password.send_keys(password)
    print("Enter password executed.")


def ClickOnSignIn(driver):
    try:
        element_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    except NoSuchElementException as e:
        element_click = self_healing_model.InvokeSelfHealing(e, driver, "//button[contains(text(), 'Login')]")
    element_click.click()
    print("Click on SignIn executed.")


EnterUserName(driver)
EnterPassword(driver)
ClickOnSignIn(driver)


time.sleep(10)
driver.quit()
