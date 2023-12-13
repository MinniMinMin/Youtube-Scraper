from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#webscraping using Selenium

term = str(input("What do you want to look for on youtube?"))

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options) # actually creating the chrome driver
driver.maximize_window() # auto maximise window

driver.get(f'https://www.youtube.com/results?search_query={term}') #opens the created chrome tab to the url given

data = []

videos = driver.find_elements('xpath', '//*[@id="video-title"]') # find everything with the tag id=video-title on the page

for video in videos:
   data.append(video)

for i in data:
   title = i.text
   link = i.get_attribute("href")

   if title == None or link == None: continue

   print(f'-------------\n{title}\n{link}\n-------------')
