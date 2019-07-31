from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
import os
import json

def get_new_mgid_token():
    mgid_token = get_mgid_access_token(mgid_login, mgid_password)
    
    with open(f'{os.environ.get("ULANMEDIAAPP")}/config/mgid_token.py', 'w') as file:
        file.write(f'mgid_token = "{mgid_token}"')


