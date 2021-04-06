from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests 
import pandas as pd
import pymongo as Mongo




def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    news_title = BeautifulSoup(html, "html.parser")
    slide_element_df = news_title.select_one("ul.item_list li.slide")
    slide_element_df.find("div", class_="content_title")
    news_title_soup = slide_element_df.find("div", class_="content_title").get_text()
    print(news_title_soup)
    news_paragraph_soup = slide_element_df.find("div", class_="article_teaser_body").get_text()
    print(news_paragraph_soup)





    #Step 2 Image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    featured_image_url  = "https://spaceimages-mars.com/image/featured/mars2.jpg"
    browser.visit(featured_image_url )
    print(featured_image_url)


    #Step 3 Mars facts
    mars_facts = pd.read_html("https://galaxyfacts-mars.com/")[0]
    print(mars_facts)
    mars_facts.reset_index(inplace=True)
    mars_facts.columns=["ID", "Properties", "Mars", "Earth"]
    mars_facts  

    #Step 4 Mars Hemispheres
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url) 
    print(hemispheres_url)



