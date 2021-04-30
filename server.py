# library
from flask import Flask, render_template, make_response
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import sys

from pytz import timezone 
from datetime import datetime

# Configs
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_EXTENSION_CONFIGS = {
    'codehilite': {'linenums': False}
}

# for gh-pages
FREEZER_DESTINATION='docs'

app=Flask(__name__)
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config.from_object(__name__) # 무슨뜻인지 모르겠다.
pages=FlatPages(app)
freezer=Freezer(app)

# URL Routing

# homepage
@app.route("/")
def index():
    latest=sorted(pages,reverse=True,key=lambda p:p.meta["published"])
    return render_template("index.html",posts=latest[:5])

# tags
@app.route("/tag/<string:tag>.html")
def tag(tag):
    tags=[p for p in pages if tag in p.meta.get("tags",[])]
    return render_template("tag.html",tag=tag,pages=tags)

# posts
@app.route("/posts/")
def posts():
    posts=[p for p in pages]
    return render_template("post.html",pages=posts)

# page
@app.route("/posts/<path:path>.html")
def page(path):
    page=pages.get_or_404(path)
    return render_template("page.html",page=page,pages=pages)

# code highlight
@app.route('/pygments.css')
def pygments():
    return pygments_style_defs(style='algol_nu'), 200, {'Content-Type':'text/css'}

# # resume
# @app.route('/resume.html')
# def resume():
#     return render_template('resume.html')

# sitemap
@app.route('/sitemap.xml')
def sitemap():
    latest=sorted(pages,reverse=True,key=lambda p:p.meta['published'])
    response=render_template('sitemap.xml',pages=latest,base_url='https://98hyun.github.io/')
    response=make_response(response)
    response.headers['Content-Type']='application/xml'
    return response

# rss
@app.route('/rss.xml')
def rss():
    latest=sorted(pages,reverse=True,key=lambda p:p.meta['published'])
    res=render_template('rss.xml', pages=latest, time=datetime.now(timezone('Asia/Seoul')), base_url='https://98hyun.github.io/')
    response=make_response(res)
    response.headers['Content-Type']='application/xml'
    return response

# robots.txt
@app.route('/robots.txt')
def robots():
    return render_template("robots.html")

# main
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=='build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0',port=8000)