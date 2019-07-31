from functions.misc.get_new_mgid_token import get_new_mgid_token
import os
import re

def get_and_return_new_mgid_token():
    get_new_mgid_token()
    with open(f'{os.environ.get("ULANMEDIAAPP")}/config/mgid_token.py', 'r') as file:
        mgid_token = file.read()
    pattern = re.compile(r'(")(.*)(")')
    res = pattern.findall(mgid_token)
    mgid_token = list(res[0])[1]
    return mgid_token


