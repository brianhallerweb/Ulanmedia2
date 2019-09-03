from flask_restful import Resource, abort
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ulanmedia2_dashboard.server.models.good_widget import GoodWidgetModel


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
        return {f'good_widgets': [good_widget.json() for good_widget in
            GoodWidgetModel.query.all()]}
        


