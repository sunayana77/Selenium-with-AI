from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

# Open Chrome
driver = webdriver.Chrome()
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service,options=options)
url ='https://accounts.lambdatest.com/dashboard'
driver.get(url)


def EnterUserName(driver):
        element_email = driver.find_element(By.XPATH, "//input[@name='email']")
        element_email.send_keys("your@gmail.com") 
        print("email done")

       

def EnterPassword(driver):
        element_password = driver.find_element(By.XPATH, "//input[@name='password']")
        element_password.send_keys("yourpassword")  
        print("password done")

def ClickOnSignIn(driver):
        element_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        element_click.click()
        print("login ")
    


EnterUserName(driver)
EnterPassword(driver)
ClickOnSignIn(driver)

WebDriverWait(driver,10).until(EC.url_contains("/dashboard"))

print("current url",driver.current_url)
time.sleep(10)

dashboard_element = driver.find_elements(By.TAG_NAME,"button")

for element in dashboard_element:
        print(element.text)
driver.quit()

