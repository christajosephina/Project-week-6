#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install selenium
#!pip install webdriver_manager


# In[2]:


import selenium


# In[3]:


#pip install selenium


# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


# In[5]:


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


# In[6]:


from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')


# In[7]:


driver = webdriver.Chrome(options=options)


# In[8]:


from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import json
import pandas as pd
from datetime import date
import datetime as datetime


# In[9]:


today = date.today() 
year = today.year
day = today.day
month = today.month


# In[10]:


tomorrow = date.today() + datetime.timedelta(days=1)
yeartm = tomorrow.year
daytm = tomorrow.day
monthtm = tomorrow.month


# In[11]:


year = str(year)
day = str(day)
month = str(month)
yeartm = str(yeartm)
daytm = str(daytm)
monthtm = str(monthtm)


# In[12]:


urltime = "https://www.booking.com/searchresults.nl.html?aid=376373&label=Boekings-nl-Nmlwg4ZjCgLYTSLOHsJrjgS267724993818%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9043480%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGtdKYocc2a8Y&sid=552e2254bbf42007c1fa7f86a7c26c19&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.nl.html%3Faid%3D376373%3Blabel%3DBoekings-nl-Nmlwg4ZjCgLYTSLOHsJrjgS267724993818%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp9043480%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGtdKYocc2a8Y%3Bsid%3D552e2254bbf42007c1fa7f86a7c26c19%3Bsb_price_type%3Dtotal%26%3B&ss=Hamburg&is_ski_area=0&ssne=Hamburg&ssne_untouched=Hamburg&dest_id=-1785434&dest_type=city&checkin_year=" + year + "&checkin_month=" + month + "&checkin_monthday=" + day + "&checkout_year=" + yeartm + "&checkout_month=" + monthtm + "&checkout_monthday=" + daytm + "&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"


# In[13]:


driver.get(urltime)


# In[14]:


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[15]:


names = []
prices = []


# In[16]:


for item in soup.findAll('span', {'class': 'sr-hotel__name'}):
        names.append(item.get_text(strip=True))


# In[17]:


for item in soup.findAll('div', {'class':'bui-price-display__value prco-inline-block-maker-helper'}):
    prices.append(item.get_text(strip=True))


# In[18]:


for price, name in zip(prices, names):
    print('---')
    print(name)
    print(price)


# In[19]:


rows = []

for price, name in zip(prices, names):
    row = {}
    print('---')
    #print(name.text)
    #print(price.text)
    row['Hotel'] = name
    row['Price'] = price
    print(row)
    rows.append(row)


# In[20]:


df = pd.DataFrame(rows)
df


# In[21]:


df['Date']=today


# In[22]:


df


# In[23]:


pd.read_csv('hamburghotelprices.csv')


# In[24]:


pd.read_csv('hamburghotelprices.csv').append(df).drop_duplicates().to_csv('hamburghotelprices.csv', index=False)

