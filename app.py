from flask import Flask, render_template
from scraper.flipkart import flipkart

app = Flask(__name__)    #contains main 
print(__name__)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/learnmore")
def learnmore():
  return render_template("learnmore.html")  

@app.route("/webscraping")
def webscraping():
  return render_template("webscraping.html")  

@app.route("/staticscraping")
def staticscraping():
  return render_template("staticscraping.html")

@app.route("/flipkart")
def flip():
    f_data = flipkart()
    return render_template("flipkart.html", products=f_data)
@app.route("/apiscraping")
def apis():
  return render_template("apis.html")

if (__name__ == "__main__"):
     app.run(host = "0.0.0.0", port = 5000, debug = True)  # host, port are optional, change in file server restart ->debug = true