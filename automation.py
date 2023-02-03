from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('./chromedriver.exe')
chrome_browser = webdriver.Chrome(service=s)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title

#Gets the text from the button
show_message_button = chrome_browser.find_element(By.CLASS_NAME,'btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

input_box = chrome_browser.find_element(By.ID, 'user-message')
input_box.clear()
input_box.send_keys('Yo dawg!')

show_message_button.click()

message = chrome_browser.find_element(By.ID, 'display').get_attribute('innerHTML')
assert 'Yo dawg!' in message

time.sleep(3)

