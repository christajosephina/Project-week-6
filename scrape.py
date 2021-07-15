#!/usr/bin/env python
# coding: utf-8

# In[69]:


from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import json
import pandas as pd


# In[2]:


url = 'https://www.booking.com/searchresults.nl.html?label=gen173nr-1FCAEoggI46AdIM1gEaDuIAQGYARy4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AuaDsocGwAIB0gIkN2UzYTE4ZmQtYTlhZC00NjY1LWFmMTctNzY1NDljMjkyMWJj2AIG4AIB&sid=e5cb477f66581f1895119ed9df6cb6b2&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.nl.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaDuIAQGYARy4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AuaDsocGwAIB0gIkN2UzYTE4ZmQtYTlhZC00NjY1LWFmMTctNzY1NDljMjkyMWJj2AIG4AIB%3Bsid%3De5cb477f66581f1895119ed9df6cb6b2%3Bsb_price_type%3Dtotal%26%3B&ss=Hamburg%2C+Hansestadt+Hamburg%2C+Duitsland&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&search_pageview_id=100a7df32af6001a&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&ac_position=0&ac_langcode=nl&ac_click_type=b&dest_id=-1785434&dest_type=city&iata=HAM&place_id_lat=53.549999&place_id_lon=10&search_pageview_id=100a7df32af6001a&search_selected=true&ss_raw=hamburg'


# # Parsing it (Soma's way)

# In[4]:


response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')


# In[5]:


#doc


# In[62]:


names = doc.find_all('span', itemprop='name')


# In[63]:


prices = doc.find_all(class_='bui-price-display__value bui-f-color-constructive')


# In[65]:


for price, name in zip(prices, names):
    print('---')
    print(name.text)
    print(price.text)


# In[73]:


rows = []

for price, name in zip(prices, names):
    row = {}
    print('---')
    #print(name.text)
    #print(price.text)
    row['Hotel'] = name.text
    row['Price'] = price.text
    print(row)
    rows.append(row)


# In[90]:


df = pd.DataFrame(rows)
df


# In[105]:


df=df.replace(to_replace = '€', value ='')
df


# In[106]:


df.to_csv("hamburghotelprices.csv")

