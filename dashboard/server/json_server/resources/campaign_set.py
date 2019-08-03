from flask_restful import Resource
from flask import request, jsonify
from flask_jwt import JWT, jwt_required
from models.campaign_set import CampaignSetModel


class CampaignSet(Resource):

    def post(self):
        vol_campaign_id = request.json['vol_campaign_id']
        mgid_campaign_id = request.json['mgid_campaign_id']
        campaign_name = request.json['campaign_name']
        max_lead_cpa = request.json['max_lead_cpa']
        max_sale_cpa = request.json['max_sale_cpa']
        campaign_status = request.json['campaign_status']

        existing_campaign_set = CampaignSetModel.find_by_vol_campaign_id(vol_campaign_id)
        if existing_campaign_set:
            return {'error message': f'campaign set with vol id {vol_campaign_id} is already in the list'}, 400

        new_campaign_set = CampaignSetModel(vol_campaign_id, mgid_campaign_id,
                campaign_name, max_lead_cpa, max_sale_cpa, campaign_status)

        try:
            new_campaign_set.save_to_db()
            return {'success message': f'added campaign set with vol id {vol_campaign_id}'} 
        except:
            return {'error message': f'error adding campaign set with vol id {vol_campaign_id}'}, 500


    def delete(self):
        vol_campaign_id = request.json['vol_campaign_id']

        campaign_set_to_be_deleted = CampaignSetModel.find_by_vol_campaign_id(vol_campaign_id)
        if campaign_set_to_be_deleted:
           try:
               campaign_set_to_be_deleted.delete_from_db()
               return {'success message': f'deleted campaign set with vol id {vol_campaign_id}'}
           except:
               return {'error message': f'error deleting campaign set with vol id {vol_campaign_id}'}, 500
        else:
            return {'error message': f'campaign set with vol id {vol_campaign_id} does not exist in the list'}, 400 

    def put(self):
        vol_campaign_id = request.json['vol_campaign_id']
        mgid_campaign_id = request.json['mgid_campaign_id']
        campaign_name = request.json['campaign_name']
        max_lead_cpa = request.json['max_lead_cpa']
        max_sale_cpa = request.json['max_sale_cpa']
        campaign_status = request.json['campaign_status']

        campaign_set_to_be_updated = CampaignSetModel.find_by_vol_campaign_id(vol_campaign_id)
        if campaign_set_to_be_updated:
           try:
               campaign_set_to_be_updated.campaign_name = campaign_name
               campaign_set_to_be_updated.max_lead_cpa = max_lead_cpa
               campaign_set_to_be_updated.max_sale_cpa = max_sale_cpa
               campaign_set_to_be_updated.campaign_status = campaign_status
               campaign_set_to_be_updated.save_to_db()
               return {'success message': f'updated campaign set with vol id {vol_campaign_id}'}
           except:
               return {'error message': f'error updating campaign set with vol id {vol_campaign_id}'}, 500
        else:
            return {'error message': f'campaign set with vol id {vol_campaign_id} does not exist in the list'}, 400 


class CompleteCampaignSets(Resource):
    
    def get(self):
        return {f'campaign sets': [campaign_set.json() for campaign_set in
            CampaignSetModel.query.all()]}
        


