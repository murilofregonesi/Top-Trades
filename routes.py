from flask import render_template, request
from flask import Blueprint

from twitter import Twitter
from db import Database

from datetime import datetime


routes = Blueprint('routes', __name__)

@routes.route("/")
def home():

    # TODO Do not reset all the time
    # Reset the DB
    reset_db = True
    if reset_db:
        Database.delete_comments()
        Database.delete_posts()

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

@routes.route("/chat/<post_id>", methods=["GET", "POST"])
def chat(post_id):

    if request.method == "POST":
        Database.add_comment(post_id, request.form.get('comment'))

    post = Database.get_post(post_id)
    comments = Database.get_post_comments(post_id)

    return render_template("chat.html", post=post, comments=comments)