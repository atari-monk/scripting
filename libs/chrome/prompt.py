from selenium_utils import get_driver, send_prompt, wait_and_notify, close_driver

driver = get_driver()

driver.get("https://chat.openai.com/")

send_prompt(driver, "Write a Python function that calculates the Fibonacci sequence.")

wait_and_notify("Waiting for response...", 10)

close_driver(driver)
