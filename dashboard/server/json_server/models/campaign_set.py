from dashboard.server.json_server.db import db
import datetime

class CampaignSetModel(db.Model):

    __tablename__ = 'campaign_sets'
    id = db.Column(db.Integer, primary_key=True)
    campaign_set_date = db.Column(db.DateTime, default=datetime.datetime.now)
    vol_id = db.Column(db.String(80), unique=True)
    mgid_id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    max_lead_cpa = db.Column(db.Numeric(10,2))
    max_sale_cpa = db.Column(db.Numeric(10,2))

    def __init__(self, vol_id, mgid_id, name, mpl, mps):
        self.vol_id = vol_id
        self.mgid_id = mgid_id
        self.name = name
        self.mpl = mpl
        self.mps = mps

    def json(self):
        return {'vol_id': self.vol_id, 'mgid_id': self.mgid_id, 'name':
                self.name, 'mpl': float(self.mpl), 'mps': float(self.mps)}

    @classmethod
    def find_by_vol_id(cls, vol_id):
        return cls.query.filter_by(vol_id=vol_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

