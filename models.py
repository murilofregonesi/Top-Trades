

class Post(db.Model):
    __tablename__ = 'post'

    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, _id, content, date):
        self._id = _id
        self.content = content
        self.date = date