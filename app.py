# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def home():
    mars_data = mongo.db.mars_data.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def web_scrape():
    mars_data = mongo.db.mars_data
    mars = scrape.scrape()
    mars_data.update({}, mars, upsert=True)
    return "FMGDL"

if __name__ == "__main__":
    app.run(debug=True)