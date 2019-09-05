from flask_restful import Resource, abort
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ulanmedia2_dashboard.server.models.good_widget import GoodWidgetModel
from ulanmedia2_dashboard.server.models.widget_domain import WidgetDomainModel
from ulanmedia2_dashboard.server.db import db



class GoodWidget(Resource):

    @jwt_required
    def post(self):
        widget_id = request.json['widget_id']

        existing_widget = GoodWidgetModel.find_by_widget_id(widget_id)
        if existing_widget:
            return {'error_message': f'widget {widget_id} is already in the list'}, 400

        new_widget = GoodWidgetModel(widget_id)

        try:
            new_widget.save_to_db()
            return {'success_message': f'added widget {widget_id}'} 
        except:
            return {'error_message': f'error adding widget {widget_id}'}, 500




    @jwt_required
    def delete(self):
        widget_id = request.json['widget_id']

        widget_to_be_deleted = GoodWidgetModel.find_by_widget_id(widget_id)
        if widget_to_be_deleted:
           try:
               widget_to_be_deleted.delete_from_db()
               return {'success_message': f'deleted widget {widget_id}'}
           except:
               return {'error_message': f'error deleting widget {widget_id}'}, 500
        else:
            return {'error_message': f'widget {widget_id} does not exist in the list'}, 400 


class CompleteGoodWidgets(Resource):
    
    @jwt_required
    def get(self):
        query_results = db.session.query(GoodWidgetModel, WidgetDomainModel).outerjoin(WidgetDomainModel, GoodWidgetModel.widget_id == WidgetDomainModel.widget_id).all()
        json_to_return = {'good_widgets_and_domains':[]}
        for result in query_results:
            if result[1] != None:
                widget_id = result[0].json()['widget_id']
                domain = result[1].json()['domain']
                row = {'widget_id': widget_id, 'domain': domain}
            else:
                widget_id = result[0].json()['widget_id']
                row = {'widget_id': widget_id, 'domain': None}
            json_to_return['good_widgets_and_domains'].append(row)

        return json_to_return    

        


