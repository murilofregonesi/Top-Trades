from app import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, id, content, date):
        self.id = id
        self.content = content
        self.date = date

    def __repr__(self):
        return '<Post {}, from {}>'.format(self.content, self.date)
