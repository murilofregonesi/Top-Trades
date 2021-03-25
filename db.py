from flask import current_app
from models import Post


class Database():

    def __init__(self):
        pass

    @staticmethod
    def add_post(user: str, content: str, date: 'datetime') -> bool:
        try:
            post = Post(None, user, content, date)
            current_app.db.session.add(post)
            current_app.db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_all_posts() -> list:
        return Post.query.all()