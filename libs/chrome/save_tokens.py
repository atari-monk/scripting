from selenium_utils import get_driver, open_url, send_prompt, click_element, get_clipboard_text, save_text_to_file, close_driver
from selenium.webdriver.common.by import By

driver = get_driver()

open_url(driver, "https://chat.openai.com/")

send_prompt(driver, "Write a Python function that calculates the Fibonacci sequence.")

click_element(driver, By.XPATH, "//button[@data-testid='copy-turn-action-button']")

copied_text = get_clipboard_text()

save_text_to_file(copied_text)

close_driver(driver)
