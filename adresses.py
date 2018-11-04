# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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


#launch url
url = "https://www.chrono24.fr/search/browse.htm?char=A-Z"

# create a new Chrome session
driver = webdriver.Chrome("/Users/Louis/desktop/scrapingchrono/chromedriver")
driver.implicitly_wait(5)
driver.get(url)

marques = driver.find_elements_by_class_name('text-default')
sitewebs= open('adresse.txt','a')

for items in marques:
    adresses = items.get_attribute("href")
    print(adresses)
    sitewebs.write(str(adresses) +'\n')
    
    
    
    