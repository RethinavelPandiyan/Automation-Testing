from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
from selenium.webdriver.chrome.service import Service
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
username=driver.find_element(By.ID,"username")
username.send_keys("student")
password=driver.find_element(By.ID,"password")
password.send_keys("Password123")
submit_button=driver.find_element(By.ID,"submit")
submit_button.click()
time.sleep(2)
msg=driver.find_element(By.TAG_NAME,'h1').text
if msg=="Logged In Successfully":
    para=["Hello","Practice","Courses","Unlock Your Future: Selenium WebDriver Career Launcher Part 6","Contact"]
    i=0
    count=0
    menu={"home":"menu-item-43","practice":"menu-item-20","course":"menu-item-21","Blog":"menu-item-19","Contact":"menu-item-18"}
    for link,page in menu.items():
        b=driver.find_element(By.ID,page)
        b.click()
        p=driver.find_element(By.CLASS_NAME,"post-title").text
        if p==para[i]:
            count+=1
        i+=1
        time.sleep(1)
if count==5:
    print("Test Success")
else:
    print("Test Fail")
driver.quit()
