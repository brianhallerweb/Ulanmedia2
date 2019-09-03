from ulanmedia2_dashboard.server.db import db
import datetime

class GoodWidgetModel(db.Model):

    __tablename__ = 'good_widgets'
    id = db.Column(db.Integer, primary_key=True)
    good_widget_date = db.Column(db.DateTime, default=datetime.datetime.now)
    widget_id = db.Column(db.String(50), unique=True)

    def __init__(self, widget_id):
        self.widget_id = widget_id

    def json(self):
        return {'widget_id': self.widget_id}

    @classmethod
    def find_by_widget_id(cls, widget_id):
        return cls.query.filter_by(widget_id=widget_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

