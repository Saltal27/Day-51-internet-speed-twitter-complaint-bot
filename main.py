import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# my Twitter credentials
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# driver path
chrome_driver_path = "C:\Development\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = WebDriver(service=service, options=options)
driver.maximize_window()

driver.get("https://www.speedtest.net/")


# Metering internet speed
go = driver.find_element(By.CSS_SELECTOR, '.start-text')
go.click()
time.sleep(60)

# Getting hold of the internet speed
download_speed = driver.find_element(By.CSS_SELECTOR, '.download-speed')
print(f"Download speed: {download_speed.text}")

upload_speed = driver.find_element(By.CSS_SELECTOR, '.upload-speed')
print(f"Upload speed: {upload_speed.text}")


tweet_content = f"Hey Internet provider, why is my internet speed" \
                f" {download_speed.text} down / {upload_speed.text} up when I pay for 2 down / 0.5 up?"


# Opening a new tab
driver.execute_script("window.open('');")

# Switching to the new tab
driver.switch_to.window(driver.window_handles[1])

# # Navigating to the Twitter login page
driver.get('https://twitter.com/login?lang=en')
time.sleep(20)

# Signing in to Twitter
email = driver.find_element(By.TAG_NAME, 'input')
email.send_keys("omarmobarak53@gmail.com")
email.send_keys(Keys.ENTER)

time.sleep(5)

try:
    username = driver.find_element(By.TAG_NAME, 'input')
except selenium.common.exceptions.ElementNotInteractableException:
    pass
else:
    username.send_keys("@SalTal27")
    username.send_keys(Keys.ENTER)
    time.sleep(5)

password = driver.find_elements(By.TAG_NAME, 'input')[1]
password.send_keys("omarammarraghad")
password.send_keys(Keys.ENTER)
time.sleep(30)

# Tweeting
try:
    little_x = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                             '/div/div[1]/div/div/div/div[1]/div/div/svg')
except selenium.common.exceptions.NoSuchElementException:
    pass
else:
    little_x.click()

tweet = driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block')
tweet.send_keys(tweet_content)
tweet.send_keys(Keys.CONTROL + Keys.ENTER)

# Switching back to the original tab
driver.switch_to.window(driver.window_handles[0])


driver.quit()
