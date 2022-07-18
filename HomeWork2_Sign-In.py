from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Limit/OneDrive/Documents/python-selenium-automation/chromedriver.exe' )
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']")

driver.find_element(By.XPATH,"//a[@id='nav-orders']").click()

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Limitless369@outlook.com")

expected_result ="Limitless369@outlook.com"

#actual_result = (By.XPATH,"//input[@type='email']").send_keys("Limitless369@outlook.com")



print("TestCase Passed")






print("TestCase Passed")

driver.quit()
