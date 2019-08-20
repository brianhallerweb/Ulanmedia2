from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from dashboard.server.models.colorlist import ColorlistModel


class Colorlist(Resource):

    @jwt_required
    def post(self, color):
        widget_id = request.json['widget_id']

        existing_widget = ColorlistModel.find_by_widget_id(widget_id)
        existing_color = None
        switch_flag = False
        if existing_widget:
            existing_color = existing_widget.color
            if existing_color == color:
                return {'error_message': f'widget {widget_id} already in {color}list'}, 400
            switch_flag = True
            existing_widget.delete_from_db()

        new_widget = ColorlistModel(widget_id, color)

        try:
            new_widget.save_to_db()
        except:
            return {'error_message': f'error {color}listing widget {widget_id}'}, 500

        if switch_flag:
            return {'success_message': f'widget {widget_id} successfully switched from the {existing_color}list to the {color}list'}, 201
        else:
            return {'success_message': f'widget {widget_id} successfully added to the {color}list'}, 201


    @jwt_required
    def delete(self, color):
        widget_id = request.json['widget_id']

        widget_to_be_deleted = ColorlistModel.find_by_widget_id(widget_id)
        if widget_to_be_deleted:
            try:
                widget_to_be_deleted.delete_from_db()
                return {'success_message': f'deleted widget {widget_id}'}
            except:
                return {'error_message': f'error deleting widget {widget_id}'}, 500

        else:
            return {'error_message': f'widget {widget_id} does not exist in any list'}, 400 


class CompleteColorlist(Resource):

    @jwt_required
    def get(self, color):
        return {f'{color}list': [colorlist.json() for colorlist in
            ColorlistModel.query.filter_by(color=color)]}
        


