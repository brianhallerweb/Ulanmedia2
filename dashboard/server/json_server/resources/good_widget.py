from flask_restful import Resource
from flask import request
from flask_jwt import JWT, jwt_required
from models.good_widget import GoodWidgetModel


class GoodWidget(Resource):

    def post(self):
        widget_id = request.json['widget_id']

        existing_widget = GoodWidgetModel.find_by_widget_id(widget_id)
        if existing_widget:
            return {'message': f'widget {widget_id} already in good list'}, 400

        new_widget = GoodWidgetModel(widget_id)

        try:
            new_widget.save_to_db()
        except:
            return {'message': f'error good-listing widget {widget_id}'}, 500



    def delete(self):
        widget_id = request.json['widget_id']

        widget_to_be_deleted = GoodWidgetModel.find_by_widget_id(widget_id)
        if widget_to_be_deleted:
           widget_to_be_deleted.delete_from_db()
           return {'message': f'widget {widget_id} deleted'}
        else:
            return {'message': f'widget {widget_id} does not exist in good list'}, 400 


class CompleteGoodWidgets(Resource):
    
    def get(self):
        return {f'good list': [goodwidget.json() for goodwidget in
            GoodWidgetModel.query.all()]}
        


