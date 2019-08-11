from flask_restful import Resource
from flask import request
from dashboard.server.json_server.models.user import UserModel

# 8/5/19 I included this code for completeness but there is no route for
# creating a new user
# Mike's user was inserted into mysql manually. Signing in (getting a new JWT)
# is done through the /auth endpoint

class UserRegister(Resource):

    def post(self):
        username = request.json['username']
        password = request.json['password']
        
        if UserModel.find_by_username(username):
            return {'message': f'user {username} already exists'}, 400 

        new_user = UserModel(username, password)

        try:
            new_user.save_to_db()
        except:
            return {'message': f'error adding new user {username}'}, 500

        return {'message': f'user {username} created successfully'}, 201

