from flask import render_template
from flask import Blueprint

from twitter import Twitter
from db import Database

from datetime import datetime


routes = Blueprint('routes', __name__)

@routes.route("/")
def home():

    topics = Twitter.trending_topics()
    
    # Add all trending topics to the DB
    for topic in topics:
        user = topic['name']
        content = topic['query']
        date = datetime.now()

        Database.add_post(user, content, date)

    # Post all trending topics to the Blog
    posts = Database.get_all_posts()

    return render_template("blog.html", posts=posts)
