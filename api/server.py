import sys, os
from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer # Added

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'pages'
app.config['DEBUG'] = 'True'
app.config['FLATPAGES_AUTO_RELOAD'] = 'DEBUG'
pages = FlatPages(app)
freezer = Freezer(app) # Added

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"

# URL Routing - Flat Pages
# Retrieves the page path and
@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)

@app.route('/about')
def about():
    return 'About'

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)