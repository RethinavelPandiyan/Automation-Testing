from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://demoqa.com/browser-windows")

main_window = driver.current_window_handle


driver.find_element(By.ID, "tabButton").click()


time.sleep(2)

all_windows = driver.window_handles

for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break


time.sleep(2)


driver.switch_to.window(main_window)
time.sleep(2)


driver.quit()
