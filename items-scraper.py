# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import numpy as np
import selenium

download_dir = "exampleCsv.csv" 
csv = open(download_dir, "w") 
#launch url
url = "https://www.chrono24.fr/search/browse.htm?char=A-Z"

# create a new Chrome session
driver = webdriver.Chrome("/Users/Louis/desktop/scrapingchrono/chromedriver")
driver.implicitly_wait(1)

christophe2 = open('christophe2.txt','a')

with open("adresse.txt") as f:
        for line in f:
            driver.get(line)
            
            watch =  driver.find_elements_by_class_name('article-item-container')
            
            for items in watch:
                christophe2.write(items.text)
                print(items.text)
    
            

              
        





