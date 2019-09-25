import requests 
from datetime import datetime, timedelta
import pytz
import sys
import mysql.connector
import re
from ulanmedia2_config.config import * 
from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets
from get_vol_id_from_mgid_id import get_vol_id_from_mgid_id
from get_campaign_name_from_mgid_id import get_campaign_name_from_mgid_id

import pprint
pp=pprint.PrettyPrinter(indent=2)

def monitor_whitelist_campaigns():
    # ##############
    # get mgid token
    
    res = requests.post("https://api.mgid.com/v1/auth/token",
            headers={"Content-type": "application/x-www-form-urlencoded",
                     "Cache-Control": "no-cache"},
             data={"email": mgid_login, "password": mgid_password})
    
    token = res.json()["token"] 

    #############
    # mgid dates
    
    timezone = 'america/los_angeles'
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(0)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(0)
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    
    start_date = start_date_pst.strftime("%Y-%m-%d")
    end_date = end_date_pst.strftime("%Y-%m-%d")


    ##################
    # set up mysql

    mydb = mysql.connector.connect(
      host="localhost",
      user= mysql_user,
      passwd= mysql_password,
      database="ulanmedia"
    )

    mycursor = mydb.cursor()

    sql = f"SELECT DISTINCT traffic_campaign_id from whitelist_campaigns"

    mycursor.execute(sql)
    result = mycursor.fetchall()
    campaign_ids = []
    for row in result:
        campaign_ids.append(row[0])



    for campaign_id in campaign_ids:
        url=f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{campaign_id}?token={token}";
        res = requests.get(url)
        res = res.json()
        excluded_widgets = []
        if len(res["widgetsFilterUid"]["widgets"]) > 0:
            for key, value in res["widgetsFilterUid"]["widgets"].items():
                if (value == "[]") | (value == None):
                    excluded_widgets.append(key)
                else:
                    value = value.replace("[", "")
                    value = value.replace("]", "")
                    value = value.replace(",", "")
                    c_widgets = value.split(" ")
                    for c_widget in c_widgets:
                        excluded_widgets.append(f"{key}s{c_widget}")

        sql = f"SELECT widget_id from whitelist_campaigns WHERE traffic_campaign_id = '{campaign_id}'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        whitelist_widget_ids = []
        for row in result:
            whitelist_widget_ids.append(row[0])

        url = f"https://api.mgid.com/v1/goodhits/campaigns/{campaign_id}/quality-analysis/?token={token}&dateInterval=today"

        res = requests.get(url)
        res = res.json()
        for widget_id in res[campaign_id][f"{start_date}_{end_date}"]:

            clicks = res[campaign_id][f"{start_date}_{end_date}"][widget_id]['clicks']

            if widget_id in whitelist_widget_ids:
                print(f"widget {widget_id} in whitelist")
            elif widget_id not in whitelist_widget_ids and widget_id in excluded_widgets:
                print(f"widget {widget_id} not in whitelist but is already excluded")
            else:
                print(f"widget {widget_id} needs to be paused")
                # url to use for pausing
                # https://api.mgid.com/v1/goodhits/clients/{$mgidClientID}/campaigns/{$traffic_campaign_id}?token={$mgid_access_token}&widgetsFilterUid=include,except,{$widget_id}


monitor_whitelist_campaigns()
