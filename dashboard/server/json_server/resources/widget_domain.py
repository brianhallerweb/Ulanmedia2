from flask_restful import Resource
from flask import request, jsonify
from flask_jwt import JWT, jwt_required
from dashboard.server.json_server.models.widget_domain import WidgetDomainModel


class WidgetDomain(Resource):

    @jwt_required()
    def post(self):
        traffic_source = request.json['traffic_source']
        widget_id = request.json['widget_id']
        domain = request.json['domain']

        existing_widget_domain = WidgetDomainModel.find_widget_domain(traffic_source, widget_id, domain)
        if existing_widget_domain:
            return {'error message': f'widget domain {traffic_source},{widget_id},{domain} is already in the list'}, 400

        new_widget_domain = WidgetDomainModel(traffic_source, widget_id, domain)

        try:
            new_widget_domain.save_to_db()
            return {'success message': f'added widget domain {traffic_source},{widget_id},{domain}'} 
        except:
            return {'error message': f'error adding widget {traffic_source},{widget_id},{domain}'}, 500


    @jwt_required()
    def delete(self):
        traffic_source = request.json['traffic_source']
        widget_id = request.json['widget_id']
        domain = request.json['domain']

        widget_to_be_deleted = WidgetDomainModel.find_widget_domain(traffic_source, widget_id, domain)
        if widget_to_be_deleted:
           try:
               widget_to_be_deleted.delete_from_db()
               return {'success message': f'deleted widget domain {traffic_source},{widget_id},{domain}'}
           except:
               return {'error message': f'error deleting widget domain {traffic_source},{widget_id},{domain}'}, 500
        else:
            return {'error message': f'widget domain {traffic_source},{widget_id},{domain} does not exist in the list'}, 400 


class CompleteWidgetDomains(Resource):
    
    @jwt_required()
    def get(self):
        return {f'widget domains': [widget_domain.json() for widget_domain in
            WidgetDomainModel.query.order_by(WidgetDomainModel.traffic_source,
                WidgetDomainModel.widget_id, WidgetDomainModel.domain).all()]}
        


