from dashboard.server.json_server.db import db
import datetime

class CampaignSetModel(db.Model):

    __tablename__ = 'campaign_sets'
    id = db.Column(db.Integer, primary_key=True)
    campaign_set_date = db.Column(db.DateTime, default=datetime.datetime.now)
    vol_campaign_id = db.Column(db.String(80), unique=True)
    mgid_campaign_id = db.Column(db.String(80), unique=True)
    campaign_name = db.Column(db.String(80))
    max_lead_cpa = db.Column(db.Numeric(10,2))
    max_sale_cpa = db.Column(db.Numeric(10,2))

    def __init__(self, vol_campaign_id, mgid_campaign_id, campaign_name,
            max_lead_cpa, max_sale_cpa):
        self.vol_campaign_id = vol_campaign_id
        self.mgid_campaign_id = mgid_campaign_id
        self.campaign_name = campaign_name
        self.max_lead_cpa = max_lead_cpa
        self.max_sale_cpa = max_sale_cpa

    def json(self):
        return {'vol_campaign_id': self.vol_campaign_id, 'mgid_campaign_id':
                self.mgid_campaign_id, 'campaign_name':
                self.campaign_name, 'max_lead_cpa': float(self.max_lead_cpa),
                'max_sale_cpa': float(self.max_sale_cpa)}

    @classmethod
    def find_by_vol_campaign_id(cls, vol_campaign_id):
        return cls.query.filter_by(vol_campaign_id=vol_campaign_id).first()

    def find_by_mgid_campaign_id(cls, mgid_campaign_id):
        return cls.query.filter_by(mgid_campaign_id=mgid_campaign_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

