from flask import render_template, request, redirect, url_for
from flask import Blueprint

from twitter import Twitter
from db import Database

from datetime import datetime
import os


routes = Blueprint('routes', __name__)

@routes.route("/")
def home():

    # Database posts
    db_posts = Database.get_posts()

    # Remove old posts
    for post in db_posts:
        past_days = (datetime.now() - post.date).days
        if past_days > int(os.environ['DAYS_TO_HOLD_DATA']):
            Database.delete_post_comments(post._id)
            Database.delete_post(post._id)
            db_posts.remove(post)

    # Tweets
    screen_names = ["interinvest", "rafabevilacqua2", "dinheirosabr"]
    contents = [db_post.content for db_post in db_posts]

    for screen_name in screen_names:
        for status in Twitter.user_timeline(screen_name):
            content = status.text
            date = status.created_at

            # Add new Tweets
            past_days = (datetime.now() - date).days
            if past_days < int(os.environ['DAYS_TO_HOLD_DATA']):
                if content not in contents:
                    user = status.user.name
                    Database.add_post(user, content, date)

    return render_template("blog.html", posts=db_posts)

@routes.route("/chat/<post_id>", methods=["GET", "POST"])
def chat(post_id):

    if request.method == "POST":
        Database.add_comment(post_id, request.form.get('comment'))
        return redirect(url_for('routes.chat', post_id=post_id))

    post = Database.get_post(post_id)
    comments = Database.get_post_comments(post_id)

    return render_template("chat.html", post=post, comments=comments)