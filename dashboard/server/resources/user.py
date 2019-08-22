from flask_restful import Resource
from flask import request
from dashboard.server.models.user import UserModel, RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class UserRegistration(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        if UserModel.find_by_username(username):
          return {'message': f'User {username} already exists'}, 400

        new_user = UserModel(username, UserModel.generate_hash(password))

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return {
                'message': f'User {username} was created',
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': f'error adding new user {username}'}, 500

class UserLogin(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        current_user = UserModel.find_by_username(username)
        if not current_user:
            return {'message': f'User {username} doesn\'t exist'}
        
        if UserModel.verify_hash(password, current_user.password):
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return {
                'message': f'Logged in as {username}',
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}, 500
      
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500 

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token} 


