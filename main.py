from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "username"
ACCOUNT_PASSWORD = "password"
PHONE = "phone_no"

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(3)

sign_in_button = driver.find_element(by="link text",value="Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(2)

email_field = driver.find_element(by="id", value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by="id", value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(3)
apply_field = driver.find_element(by="id", value="ember188")
apply_field.send_keys(Keys.ENTER)

time.sleep(2)

phone_field = driver.find_element(by="id", value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3415138937-9-phoneNumber-nationalNumber")
phone_field.send_keys(PHONE)

# assuming resume already uploaded, just have to choose
choose_field = driver.find_element(by="id", value="ember396")
choose_field.send_keys(Keys.ENTER)

time.sleep(2)

submit_field = driver.find_element(by="id", value="ember398")
submit_field.send_keys(Keys.ENTER)
