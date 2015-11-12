
# coding: utf-8

# In[1]:

import urllib.request as ul #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page

url = "http://www.slate.com"

#Do stuff necessary to get the page text into a string
url_response=ul.urlopen(url,timeout=5)



soup = BeautifulSoup(url_response) #Soup stores the data in a structured way to make retrieval easy
#Soup also automatically decodes the page correctly (most of the time!)

print(soup.prettify()) #Prints page contents 


# In[ ]:

#Soup stores the page as a dictionary with tags for retrieval. 
#For example, the first div tag on the page is:
soup.div

#Or, to get the first link out of the page
soup.a

#To find all links on the page
soup.find_all('a')




