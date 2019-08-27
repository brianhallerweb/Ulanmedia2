import requests 
from datetime import datetime, timedelta
import pytz
import sys
import mysql.connector
import re
from config.config import *
from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets
from get_vol_id_from_mgid_id import get_vol_id_from_mgid_id
from get_campaign_name_from_mgid_id import get_campaign_name_from_mgid_id

import pprint
pp=pprint.PrettyPrinter(indent=2)

def set_cost_ads(days_ago):


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
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    
    start_date = start_date_pst.strftime("%Y-%m-%d")
    end_date = end_date_pst.strftime("%Y-%m-%d")

    date_to_put_in_sql = start_date_pst.replace(tzinfo=None, microsecond=0)

    ##################
    # set up mysql

    mydb = mysql.connector.connect(
      host="localhost",
      user= mysql_user,
      passwd= mysql_password,
      database="ulanmedia"
    )

    mycursor = mydb.cursor()

    sql = f"delete from cost_ads where cost_date like '{start_date}%'"

    mycursor.execute(sql)
    ####################

    campaigns = create_complete_campaign_sets()

    ads_data = {}

    request_number = 0
    ads_data = {}
    while len(ads_data) == request_number * 700:
        url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/teasers?token={token}&limit=700&start={request_number * 700}"
        request_number = request_number + 1
        res = requests.get(url)
        if res.status_code == 401:
            mgid_token = get_and_return_new_mgid_token()
            return get_mgid_ads_data(mgid_token, mgid_client_id)
        res.raise_for_status()
        res = res.json()
        # The response is a dictionary of ad ids. Each ad is a dictionary
        # that includes a bunch of data. My dictionary called ads_data will
        # have the same basic structure, except the data for each ad id will be
        # modified and customized. 

        # in rare situations the response could be empty. If so, it means there
        # are no more ads to get. Breaking out of the while loop will cause the
        # while condition to no longer be met, which makes sense because all
        # the ad data has been retrieved. 
        if len(res) == 0:
            break
            
        for ad in res.values():
            # extract data and put into variables
            ad_id = str(ad["id"])
            campaign_id = str(ad["campaignId"])
            clicks = ad["statistics"]["clicks"]
            cost = ad["statistics"]["spent"]
            imps = ad["statistics"]["hits"]
            if imps == 0:
                ctr = 0
            else:
                ctr = clicks/imps
            url = ad["url"]
            status = ad["status"]["code"]
            # extract image name from the url using regex
            pattern = re.compile(r'(&img=)([^&]*)')
            res = pattern.findall(url)
            image = res[0][1]
            # add an ad to ads_data
            # ads_data is a dictionary of ad ids. Each ad id is a dictionary of data for that ad. 
            ads_data[ad_id] = {}
            # fill in the data for a particular ad.  
            ads_data[ad_id]["ad_id"] = ad_id
            ads_data[ad_id]["mgid_id"] = campaign_id
            ads_data[ad_id]["clicks"] = clicks
            ads_data[ad_id]["cost"] = cost
            ads_data[ad_id]["imps"] = imps
            ads_data[ad_id]["ctr"] = ctr
            ads_data[ad_id]["url"] = url
            ads_data[ad_id]["image"] = image
            if status == "goodPerformance":
                ads_data[ad_id]["status"] = "active"
            elif status == "onModeration":
                ads_data[ad_id]["status"] = "pending"
            elif status == "rejected":
                ads_data[ad_id]["status"] = "rejected"
            else:
                # I believe this is from status = blocked or status =
                # campaignBlocked
                ads_data[ad_id]["status"] = "paused"

    for ad in ads_data.values():
        ad_id = ad['ad_id']
        mgid_id = ad['mgid_id']
        campaign_name = get_campaign_name_from_mgid_id(mgid_id)
        vol_id = get_vol_id_from_mgid_id(mgid_id)
        cost = ad['cost']
        clicks = ad['clicks']
        if clicks > 0:
            cpc = cost/clicks
        else:
            cpc = 0
        sql = f"INSERT INTO cost_ads(cost_date, voluum_campaign_id, traffic_campaign_id, traffic_campaign_name, traffic_ad_id, traffic_ad_cpc, traffic_ad_clicks, traffic_ad_cost) VALUES('{date_to_put_in_sql}', '{vol_id}', '{mgid_id}', '{campaign_name}', '{str(ad_id)}','{str(cpc)}', '{str(clicks)}', '{str(cost)}')"

        mycursor.execute(sql)

        mydb.commit()

    return ads_data


