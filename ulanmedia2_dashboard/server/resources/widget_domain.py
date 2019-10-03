from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ulanmedia2_dashboard.server.models.widget_domain import WidgetDomainModel


class WidgetDomain(Resource):

    @jwt_required
    def post(self):
        traffic_source = request.json['traffic_source']
        widget_id = request.json['widget_id']
        domain = request.json['domain']
        widget_domain_source = request.json['widget_domain_source']

        existing_widget_domain = WidgetDomainModel.find_widget_domain(traffic_source, widget_id, domain, widget_domain_source)
        if existing_widget_domain:
            return {'error_message': f'widget domain {traffic_source}, {widget_id}, {domain}, {widget_domain_source} is already in the list'}, 400

        new_widget_domain = WidgetDomainModel(traffic_source, widget_id, domain, widget_domain_source)

        try:
            new_widget_domain.save_to_db()
            return {'success_message': f'added widget domain {traffic_source}, {widget_id}, {domain}, {widget_domain_source}'} 
        except:
            return {'error_message': f'error adding widget {traffic_source}, {widget_id}, {domain}, {widget_domain_source}'}, 500


    @jwt_required
    def delete(self):
        traffic_source = request.json['traffic_source']
        widget_id = request.json['widget_id']
        domain = request.json['domain']
        widget_domain_source = request.json['widget_domain_source']

        widget_to_be_deleted = WidgetDomainModel.find_widget_domain(traffic_source, widget_id, domain, widget_domain_source)
        if widget_to_be_deleted:
           try:
               widget_to_be_deleted.delete_from_db()
               return {'success_message': f'deleted widget domain {traffic_source}, {widget_id}, {domain}, {widget_domain_source}'}
           except:
               return {'error_message': f'error deleting widget domain {traffic_source}, {widget_id}, {domain}, {widget_domain_source}'}, 500
        else:
            return {'error_message': f'widget domain {traffic_source}, {widget_id}, {domain}, {widget_domain_source} does not exist in the list'}, 400 


class CompleteWidgetDomains(Resource):
    
    @jwt_required
    def get(self):
        return {f'widget_domains': [widget_domain.json() for widget_domain in
            WidgetDomainModel.query.order_by(WidgetDomainModel.traffic_source,
                WidgetDomainModel.widget_id, WidgetDomainModel.domain,
                WidgetDomainModel.widget_domain_source).all()]}
        


