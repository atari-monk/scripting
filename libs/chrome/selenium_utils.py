import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

def get_driver(user_data_dir=r"C:\Users\ASUS\AppData\Local\Google\Chrome\User Data", profile_directory="Default"):
    options = create_chrome_options(user_data_dir, profile_directory)
    driver = webdriver.Chrome(options=options)
    return driver

def wait_for_element(driver, by, value, timeout=2000):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, value)))

def send_prompt(driver, prompt, input_element_id="prompt-textarea"):
    input_area = wait_for_element(driver, By.ID, input_element_id)
    input_area.send_keys(prompt)
    input_area.send_keys(Keys.RETURN)

def close_driver(driver):
    driver.quit()
