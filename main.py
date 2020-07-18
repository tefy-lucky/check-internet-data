import selenium.webdriver as webdriver
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

driver = webdriver.Chrome()

driver.get("https://moncompte.orange.mg/")

phone_number = driver.find_element_by_name("phone-numb")
phone_number.send_keys(config["default"]["phone_number"])

password = driver.find_element_by_name("password")
password.send_keys(config["default"]["password"])

login = driver.find_element_by_id("login_button")
login.click()

time.sleep(10)

parent = driver.find_element_by_xpath('//span[@class="icom-orange_Coin"]/following-sibling::div')
date = parent.find_element_by_class_name("kpi-title")
data = parent.find_element_by_class_name("kpi-value")

print(f"{date.text}: {data.text}")

