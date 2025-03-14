from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://chat.openai.com/")

time.sleep(60*10)
print("Page opened. You can now inspect the elements.")
