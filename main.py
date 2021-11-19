import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
import time
browser = uc.Chrome()
os.system('cls')
browser.get('https://popcat.click')
input('Press Enter to start (your CPU usage may spike)')
os.system('cls')
print('Press Ctrl+C to stop clicking!')
while True:
    browser.find_element(By.XPATH, '//*[@id="app"]/div').click()
