from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import numpy as np
from tqdm import tqdm
#instantiate the driver(a mandatory process for selenium)
#driver = webdriver.Chrome(‘chromedriver’)
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://images.google.com/'
driver.get(url)
#next grabs the search bar
input = driver.find_element_by_css_selector('#sbtc > div > div.a4bIc > input')
#next line put search keyword in search bar
input.send_keys('Indian portrait')
#now we select the search button and click it
search_button= driver.find_element_by_css_selector('#sbtc > button > div > span > svg')
search_button.click()
page_scroll_sleep = 2
import time

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(page_scroll_sleep)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
        #break #insert press load more
            try:
                element = driver.find_elements_by_class_name('mye4qd') #returns list
                element[0].click()
            except:
                break
        last_height = new_height
image_links = driver.find_elements_by_class_name('rg_i.Q4LuWd')
#len(image_links)
final=list()
for i in range(len(image_links)):
    final.append(image_links[i].get_attribute('src'))
#print(final)
print( len(final))

sleeps = [1,0.5,1.5,0.7]
a=0
for j, link in enumerate(tqdm(final)):
    name = 'C:\\Users\\HP\\Desktop\\TRIAL\\PYTHON\\Scraper\\demo\\image' + f'{j}.jpeg'

    try:
    	urllib.request.urlretrieve(link, name)
    except:
    	#print(name + ' not downloaded')
    	a=a+1
    	continue
    time.sleep(np.random.choice(sleeps))
print('Not downloaded {} images'.format(a))
driver.quit()
