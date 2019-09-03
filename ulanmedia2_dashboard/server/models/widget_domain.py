from ulanmedia2_dashboard.server.db import db
import datetime

class WidgetDomainModel(db.Model):

    __tablename__ = 'widget_domains'
    id = db.Column(db.Integer, primary_key=True)
    widget_domain_date = db.Column(db.DateTime, default=datetime.datetime.now)
    traffic_source = db.Column(db.String(50))
    widget_id = db.Column(db.String(50))
    domain = db.Column(db.String(50))
    widget_domain_source = db.Column(db.String(100))

    def __init__(self, traffic_source, widget_id, domain, widget_domain_source):
        self.traffic_source = traffic_source
        self.widget_id = widget_id
        self.domain = domain
        self.widget_domain_source = widget_domain_source

    def json(self):
        return {'id': self.id, 'traffic_source': self.traffic_source, 'widget_id': self.widget_id, 'domain': self.domain, 'widget_domain_source': self.widget_domain_source}

    @classmethod
    def find_widget_domain(cls, traffic_source, widget_id, domain, widget_domain_source):
        return cls.query.filter_by(traffic_source=traffic_source, widget_id=widget_id, domain=domain, widget_domain_source=widget_domain_source).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

