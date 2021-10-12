
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment  # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres":  mars_hemispheres(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for erro handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # look inside slide_elem and find the specific element: content_title and anything nested into it
        # we need the title, wich is the class a. Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return news_title, news_p

# ### JPL Space Featured Images

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

### Mars Facts
def mars_facts():

    # Add try/except for error handling
    try:
        #Use 'read_html to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace = True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes = "table table-striped")

def mars_hemispheres(browser):
    # Visit URL to moon-hemispheres website
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    html = browser.html
    hemispheres_soup = soup(html, 'html.parser')
    #finding the tag item common to the  4 images
    items = hemispheres_soup.find_all('div', class_='item')  
    #loop through the 4 items
    for i in range(len(items)):
        hemispheres = {}
        # get link to each full-image resolution
        full_image_link = items[i].find_all('a',class_='itemLink product-item')[0].get('href')
        # visit the new page, where there is the info of each image 
        browser.visit(url+full_image_link)
        html = browser.html
        newpage = soup(html, 'html.parser')
        # get relative url link of image
        image_link = newpage.find_all('div', class_='downloads')[0].find_all('a')[0].get('href')
        # full url image 
        hemispheres['img_url'] = url+image_link
        # get name of the image and saving it in the dictionary
        image_title = newpage.find_all('div', class_='cover')[0].find_all('h2', class_='title')[0].get_text()
        hemispheres['title'] = image_title
        # adding the image info to the list of dictionaries w/all information about the 4 images
        hemisphere_image_urls.append(hemispheres)
        browser.back()
        
    return hemisphere_image_urls

if __name__ ==  "__main__":
    # If running as sript, print scraped data
    print(scrape_all())
