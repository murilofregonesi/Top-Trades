from flask import current_app


db = current_app.db

class Post(db.Model):
    __tablename__ = 'post'

    _id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.String(280), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, _id, user, content, date):
        self._id = _id
        self.user = user
        self.content = content
        self.date = date


class Comment(db.Model):
    __tablename__ = 'comment'

    _id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('post._id'))
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.String(280), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, _id, id_post, user, content, date):
        self._id = _id
        self.id_post = id_post
        self.user = user
        self.content = content
        self.date = date

