from app import db
from models import Post


class Database():

    def __init__(self):
        pass

    @staticmethod
    def add_post(id: int, content: str, date: str) -> bool:
        try:
            post = Post(id, content, date)
            db.session.add(post)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_all_posts() -> list:
        return Post.query.all()