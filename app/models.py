from datetime import datetime
from app import db


class Path(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path_name = db.Column(db.String(64), index=True, unique=True)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    Points = db.relationship('Points', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Path {}>'.format(self.path_name)


class Points(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    logtitude = db.Column(db.Float)
    lattitude = db.Column(db.Float)
    path_id = db.Column(db.Integer, db.ForeignKey('path.id'))

    def __repr__(self):
        return '<Points [{},{}]>'.format(self.logtitude, self.lattitude)
