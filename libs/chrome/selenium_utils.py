from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def create_chrome_options(user_data_dir=r"C:\Users\ASUS\AppData\Local\Google\Chrome\User Data", profile_directory="Default"):
    options = Options()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument(f"profile-directory={profile_directory}")
    #options.add_argument("--headless")

    return options

def open_url_with_selenium(url, options=None):    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def wait_and_notify(message, wait_time_minutes=10):
    print(message)
    wait_time_seconds = wait_time_minutes * 60
    time.sleep(wait_time_seconds)
