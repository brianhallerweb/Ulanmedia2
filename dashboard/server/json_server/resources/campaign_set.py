from flask_restful import Resource
from flask import request, jsonify
from flask_jwt import JWT, jwt_required
from models.campaign_set import CampaignSetModel


class CampaignSet(Resource):

    def post(self):
        vol_id = request.json['vol_id']
        mgid_id = request.json['mgid_id']
        name = request.json['name']
        mpl = request.json['mpl']
        mps = request.json['mps']

        existing_campaign_set = CampaignSetModel.find_by_vol_id(vol_id)
        if existing_campaign_set:
            return {'error message': f'campaign set with vol id {vol_id} is already in the list'}, 400

        new_campaign_set = CampaignSetModel(vol_id, mgid_id, name, mpl, mps)

        try:
            new_campaign_set.save_to_db()
            return {'success message': f'added campaign set with vol id {vol_id}'} 
        except:
            return {'error message': f'error adding campaign set with vol id {vol_id}'}, 500




    def delete(self):
        vol_id = request.json['vol_id']

        campaign_set_to_be_deleted = CampaignSetModel.find_by_vol_id(vol_id)
        if campaign_set_to_be_deleted:
           try:
               campaign_set_to_be_deleted.delete_from_db()
               return {'success message': f'deleted campaign set with vol id {vol_id}'}
           except:
               return {'error message': f'error deleting campaign set with vol id {vol_id}'}, 500
        else:
            return {'error message': f'campaign set with vol id {vol_id} does not exist in the list'}, 400 

    def put(self):
        vol_id = request.json['vol_id']
        mgid_id = request.json['mgid_id']
        name = request.json['name']
        mpl = request.json['mpl']
        mps = request.json['mps']

        campaign_set_to_be_updated = CampaignSetModel.find_by_vol_id(vol_id)
        if campaign_set_to_be_updated:
           try:
               campaign_set_to_be_updated.name = name
               campaign_set_to_be_updated.mpl = mpl
               campaign_set_to_be_updated.mps = mps
               campaign_set_to_be_updated.save_to_db()
               return {'success message': f'updated campaign set with vol id {vol_id}'}
           except:
               return {'error message': f'error updating campaign set with vol id {vol_id}'}, 500
        else:
            return {'error message': f'campaign set with vol id {vol_id} does not exist in the list'}, 400 


class CompleteCampaignSets(Resource):
    
    def get(self):
        return {f'campaign sets': [campaign_set.json() for campaign_set in
            CampaignSetModel.query.all()]}
        


