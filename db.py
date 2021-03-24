from flask import current_app
from models import Post


class Database():

    def __init__(self):
        pass

    @staticmethod
    def add_post(_id: int, content: str, date: str) -> bool:
        try:
            post = Post(_id, content, date)
            current_app.db.session.add(post)
            current_app.db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_all_posts() -> list:
        return Post.query.all()