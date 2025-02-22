import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = "unmeshraj.raj@gmail.com"
subject = "Regarding the subject".replace(" ", "%20")
body = "Hello this is a sample email that i need to edit.".replace(" ", "%20")
mailto_link = f"mailto:{email}?subject={subject}&body={body}"

driver = webdriver.Chrome()
driver.get("https://goto.now")

url_input = driver.find_element(By.ID, "urlInput")
url_input.send_keys(mailto_link)

shorten_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Shorten URL')]" )
shorten_button.click()

time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
shortened_url = soup.find("button", {"id": "copyButton"}).find_previous_sibling("a")["href"]

driver.quit()

import pyperclip

pyperclip.copy(shortened_url)
print("Shortened URL copied:", shortened_url)