#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


# look inside slide_elem and find the specific element: content_title and anything nested into it
slide_elem.find('div', class_='content_title') # this return the title as a html class


# In[6]:


# we need the title, wich is the class a. Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# ### Visit the NASA Mars News Site
# 

# In[15]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[16]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[17]:


slide_elem.find('div', class_='content_title')


# In[18]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[19]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[20]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[21]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[22]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[23]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[24]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[25]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[26]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[27]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres
# 

# In[36]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[40]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemispheres_soup = soup(html, 'html.parser')
items = hemispheres_soup.find_all('div', class_='item')  # keeping the 4 images
print(len(items))
for i in range(len(items)):
    print(f'item = {i}')
    hemispheres = {}
    full_image_link = items[i].find_all('a',class_='itemLink product-item')[0].get('href')
    browser.visit(url+full_image_link)
    print(f'visiting url:{url+full_image_link}')
    html = browser.html
    newpage = soup(html, 'html.parser')
    image_link = newpage.find_all('div', class_='downloads')[0].find_all('a')[0].get('href')
    hemispheres['img_url'] = url+image_link
    print(f'image: {image_link}')
    image_title = newpage.find_all('div', class_='cover')[0].find_all('h2', class_='title')[0].get_text()
    hemispheres['title'] = image_title
    print(f'image: {image_title}')
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[41]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[42]:


# 5. Quit the browser
browser.quit()


# In[ ]:




