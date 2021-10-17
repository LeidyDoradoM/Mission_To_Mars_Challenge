# Mission To Mars Website

This week project is all about web-scraping and visualizing the information we have gathered from specific websites about the Moon.  News, images, fun facts and comparison between earth and the moon are presented.

## Process

To perform this project, we used BeautifulSoup and Splinter to automatically scrapping four  specific websites about the moon: 
 - [Hemispheres Moon Images](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
 - Fun facts:
 - Recent Moon News:
 - Moon Image:

All the gathered information is stored in a Mongo Database.  The information is also visualized in a webpage created with the help of Flask and Bootstrap as the main template for our html file.

### 1. Scrapping

During the study of this week module, we scraped three out of the four websites are listed above.  Now, we needed to do the same process to scrape the **Hemispheres Moon Images**. The process was implemented in Python using Jupyter notebook: [Mission_to_Mars_Challenge.ipynb](https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Mission_to_Mars_Challenge.ipynb).

### 2. MongoDB and HTML template

As it was mentioned before, we use mongodb for storing the scrapped information and then using Flask we created a webpage for visualizing all the information.  This process was implemented using a Python script: [scraping.py](https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/scraping.py) and a HTML template: [index.html](https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/templates/index.html).

### 3. Customizing our website

The html file is customized by adding some styling to our web site. Specifically, the colors of the  and the button were changed from the original version.  In addition, the hemispheres images were reorganized so the four images fit the wide of the webpage. This customizing was made by using a `css` file that helps us to overrule the original bootstrap template. The changes are in file [custom.css](https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/static/assets/css/custom.css) and Table 1 has images of the website before and after the stylingcus.

| Original WebSite             | Customized Version        |
|------------------------------|---------------------------|
|<img width="50%" src="https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Images/MissionToMars_1.png"> |
 <img width="50%" src="https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Images/customMTM_1.png">|
|<img width="50%" src="https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Images/MissionToMars2.png">|
|<img width="50%" src="https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Images/customMTM_2.png">|

Figure 1. Original Website layout vs. Customized version

In addition, the button for scraping change of color when it is hover-in as it is shown below

![hover](https://raw.githubusercontent.com/LeidyDoradoM/Mission_To_Mars_Challenge/main/Images/hover-inMTM.png)