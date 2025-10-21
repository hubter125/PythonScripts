# Author: Hubter125
# Date: 10/15/2025
# Note: Feel free to mess with timing, this is just what worked for me
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
load_dotenv()
# Create some environment variable so you aren't hard coding creds
pwd = os.getenv("POLLEV_PASSWORD")
user = os.getenv("POLLEV_USER")
# Switch to whatever browser you want
driver = webdriver.Firefox()
driver.get("https://pollev.com/login")
driver.switch_to.active_element.send_keys(user)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(1)
driver.switch_to.active_element.send_keys(Keys.TAB)
time.sleep(.1)
driver.switch_to.active_element.send_keys(Keys.TAB)
time.sleep(.1)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(.5)
driver.switch_to.active_element.send_keys(pwd)
time.sleep(.5)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(2)
driver.switch_to.active_element.send_keys("pollName")
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(.5)
driver.switch_to.active_element.send_keys(Keys.ENTER)

# Assuming that the response type for attendance is open-ended question, if different just copy css selector and replace below

text_box = WebDriverWait(driver, 3600).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".component-response-open-ended__input > textarea:nth-child(1)"))
)
text_box.send_keys("Your Name")
time.sleep(10) # Little sketch if you submit instantly as it opens
text_box.send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()






