from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
import os
from config.config import *

from dashboard.server.security import authenticate, identity

from dashboard.server.db import db
from dashboard.server.models.user import UserModel, RevokedTokenModel
from dashboard.server.resources.colorlist import Colorlist, CompleteColorlist
from dashboard.server.resources.good_widget import GoodWidget, CompleteGoodWidgets
from dashboard.server.resources.campaign_set import CampaignSet, CompleteCampaignSets
from dashboard.server.resources.widget_domain import WidgetDomain, CompleteWidgetDomains
from dashboard.server.resources.user import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"{os.environ.get('ULANMEDIAMYSQLURL')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['SECRET_KEY'] = flask_secret_key
app.config['JWT_SECRET_KEY'] = flask_secret_key
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

@app.route("/jsonapi")
def index():
    return render_template('index.html')

#this route only exists to add mike's credentials to the db
@app.route("/jsonapi/addusermike")
def add_user_mike():
    username = 'michael@hallerweb.com'
    password = mike_login_password

    if UserModel.find_by_username(username):
      return {'message': f'User {username} already exists'}, 400

    new_user = UserModel(username, UserModel.generate_hash(password))
    print(new_user)

    try:
        new_user.save_to_db()
        access_token = create_access_token(identity = username)
        refresh_token = create_refresh_token(identity = username)
        return jsonify({
            'message': f'User {username} was created',
            'access_token': access_token,
            'refresh_token': refresh_token
            })
    except:
        return jsonify({'message': f'error adding new user {username}'})

api.add_resource(UserRegistration, '/jsonapi/registration')
api.add_resource(UserLogin, '/jsonapi/login')
api.add_resource(UserLogoutAccess, '/jsonapi/logout/access')
api.add_resource(UserLogoutRefresh, '/jsonapi/logout/refresh')
api.add_resource(TokenRefresh, '/jsonapi/token/refresh')

api.add_resource(Colorlist, '/jsonapi/<string:color>list')
api.add_resource(CompleteColorlist, '/jsonapi/complete<string:color>list')

api.add_resource(GoodWidget, '/jsonapi/goodwidget')
api.add_resource(CompleteGoodWidgets, '/jsonapi/completegoodwidgets')

api.add_resource(CampaignSet, '/jsonapi/campaignset')
api.add_resource(CompleteCampaignSets, '/jsonapi/completecampaignsets')

api.add_resource(WidgetDomain, '/jsonapi/widgetdomain')
api.add_resource(CompleteWidgetDomains, '/jsonapi/completewidgetdomains')

if __name__ == '__main__':
    app.run(port=5001, debug=True)

