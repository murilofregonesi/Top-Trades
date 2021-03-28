from flask import current_app
from models import Post, Comment
from datetime import datetime


class Database():

    def __init__(self):
        pass

    @staticmethod
    def add_post(user: str, content: str, date: datetime) -> bool:
        try:
            post = Post(None, user, content, date)
            current_app.db.session.add(post)
            current_app.db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_posts() -> list:
        posts = Post.query.order_by(Post.date.desc()).all()
        return posts

    @staticmethod
    def get_post(_id):
        post = Post.query.filter(Post._id == _id).first()
        return post

    @staticmethod
    def delete_posts():
        Post.query.delete()
        current_app.db.session.commit()

    @staticmethod
    def delete_post(_id):
        Post.query.filter(Post._id==_id).delete()
        current_app.db.session.commit()

    @staticmethod
    def add_comment(id_post: int, content: str, user: str='Unknown') -> bool:
        date = datetime.now()
        try:
            comment = Comment(None, id_post, user, content, date)
            current_app.db.session.add(comment)
            current_app.db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_post_comments(id_post: int) -> list:
        comments = Comment.query.filter(Comment.id_post==id_post).order_by(Comment.date.desc()).all()
        return comments

    @staticmethod
    def delete_post_comments(id_post: int):
        Comment.query.filter(Comment.id_post==id_post).delete()
        current_app.db.session.commit()

    @staticmethod
    def delete_comments():
        Comment.query.delete()
        current_app.db.session.commit()