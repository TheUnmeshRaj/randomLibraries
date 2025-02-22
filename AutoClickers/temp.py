from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://hyperplexed.io/events/live-thumbnail")  
element = driver.find_element(By.CLASS_NAME, "w-40")
for i in range(3000):
  element.click()
  print(f"Clicked {i+1}th time")
driver.quit()