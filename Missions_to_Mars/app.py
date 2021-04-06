from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
import os 



app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

@app.route('/')
def home():
    mars_info = mongo.db.mars_info.find_all()
    return render_template('Index.html', mars_info=mars_info)


@app.route('/scrape')
def scrape():

    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_mars_news_title_soup()
    mars_data = scrape_mars.scrape_mars_news_paragraph_soup()
    mars_data = scrape_mars.scrape_mars_featured_image_url()
    mars_data = scrape_mars.scrape_mars_mars_facts()
    mars_data = scrape_mars.scrape_mars_hemispheres_url()

    mars.update({}, mars_data, upsert=True)
    
    if __name__ == "__main__":
    app.run(debug=True)


    