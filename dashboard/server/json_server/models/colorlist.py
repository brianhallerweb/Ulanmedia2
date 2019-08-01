from dashboard.server.json_server.db import db
import datetime

class ColorlistModel(db.Model):

    __tablename__ = 'colorlist'
    id = db.Column(db.Integer, primary_key=True)
    color_date = db.Column(db.DateTime, default=datetime.datetime.now)
    widget_id = db.Column(db.String(50), unique=True)
    color = db.Column(db.String(20))

    def __init__(self, widget_id, color):
        self.widget_id = widget_id
        self.color = color

    def json(self):
        return {'widget_id': self.widget_id, 'color': self.color}

    @classmethod
    def find_by_widget_id(cls, widget_id):
        return cls.query.filter_by(widget_id=widget_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

