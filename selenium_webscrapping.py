import re
import os.path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
import selenium.webdriver.support.ui as UI
import csv

start = time.time()
driver = Service(executable_path="/home/rahul/Documents/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=driver, options=options)
driver.get("https://en.wikipedia.org/wiki/Genomics")

links = []
elems = driver.find_elements(By.XPATH, "//a[@href]")
print("Number of hyperlinks on the page having href attribute are:", len(elems))

for link in elems:
    link_id = link.get_attribute("href")
    links.append(link_id)
    
print(links)

def get_text_from_links(links):
    text_list = []
    #driver = webdriver.Chrome()
    for link in links:
        try:
            driver.get(link)
            page_text = driver.find_element(By.TAG_NAME, 'body').text
            text_list.append(page_text)
        except Exception as e:
            print(f"An error occured while fetching text from {link}: {str(e)}")
    driver.quit()
    return text_list
result_text = get_text_from_links(links)

file_name = "Genomics_content.text"
with open(file_name, 'w', encoding='utf-8') as file:
    try:
        for link in result_text:
            file.write(f"Text from link: {link}\n")
            print("Web scraping process completed successfully!")
    except Exception as e:
        print(f"An error occured: {e}")




