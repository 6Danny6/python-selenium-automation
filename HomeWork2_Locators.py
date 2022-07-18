from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Limit/OneDrive/Documents/python-selenium-automation/chromedriver.exe' )
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH,"//input[@id='continue']")
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")




print("Test Passed")

driver.quit()
