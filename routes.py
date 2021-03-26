from flask import render_template
from flask import Blueprint

from twitter import Twitter
from db import Database

from datetime import datetime


routes = Blueprint('routes', __name__)

@routes.route("/")
def home():

    # Reset the DB
    Database.delete_posts()
    Database.delete_comments()

    # Add Tweets to the DB
    screen_names = ["interinvest", "rafabevilacqua2", "dinheirosabr"]
    for screen_name in screen_names:
        for status in Twitter.user_timeline(screen_name):
            user = status.user.name
            content = status.text
            date = status.created_at

            Database.add_post(user, content, date)

    # Post Tweets to the Blog
    posts = Database.get_all_posts()

    return render_template("blog.html", posts=posts)
