from functions.misc.get_new_mgid_token import get_new_mgid_token
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
import requests
import json
import os
import re


def exclude_campaign_for_one_p_or_c_widget(token, client_id, widget_id, campaign_id):
    url = f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns/{campaign_id}?token={token}";
    res = requests.patch(url, 
        headers ={"Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"}, 
          data = {"widgetsFilterUid": f"include,except,{widget_id}"})
          # 1/29/19 use the line below when you want to "include". I know it says
          # "exclude, except, widget_id", but this comment is correct, use the
          # line below if you want to include a campaign rather than exclude
          # it. Use the line above if you want to exclude a campaign. 
         # data = {"widgetsFilterUid": f"exclude,except,{widget_id}"})
    if res.status_code == 401:
        mgid_token = get_and_return_new_mgid_token()
        return exclude_campaign_for_one_p_or_c_widget(mgid_token, client_id, widget_id, campaign_id)
    res.raise_for_status() 
    res = res.json()
    # if successful, this function returns json that looks like this
    # {id: campaign_id}
    return json.dumps(res)



