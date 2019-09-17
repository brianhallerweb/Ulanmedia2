import requests 
from datetime import datetime, timedelta
import pytz
import sys
import mysql.connector
import re
from ulanmedia2_config.config import * 
from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets
from utility_functions.get_vol_access_token import get_vol_access_token
from get_vol_id_from_mgid_id import get_vol_id_from_mgid_id
from get_campaign_name_from_mgid_id import get_campaign_name_from_mgid_id

import pprint
pp=pprint.PrettyPrinter(indent=2)

def update_traffic_click_id_in_conversions_table():
    # this function only updates clicks ids for today
    
    ###########
    token = get_vol_access_token(vol_access_id, vol_access_key)

    #############
    # vol dates
    
    timezone = 'america/los_angeles'
    start_date_utc = pytz.utc.localize(datetime.utcnow())
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) + timedelta(1) 
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

    ####################

    url = f"https://api.voluum.com/report/conversions?from={start_date}T00%3A00%3A00Z&to={end_date}T00%3A00%3A00Z&tz=America%2FLos_Angeles&sort=postbackTimestamp&direction=desc&columns=postbackTimestamp&columns=externalId&columns=clickId&columns=transactionId&columns=revenue&groupBy=conversion&offset=0&limit=100000&include=ACTIVE" 
    res = requests.get(url, headers = {"cwauth-token": token}) 
    res = res.json() 
    for row in res["rows"]: 
        vol_click_id = row["clickId"] 
        vol_campaign_id = row["campaignId"] 
        mgid_campaign_id = row["customVariable2"] 
        mgid_click_id = row["externalId"] 
        conversion_type = row["transactionId"] 
        postback_timestamp = row["postbackTimestamp"] 
        postback_timestamp = datetime.strptime(postback_timestamp, '%Y-%m-%d %I:%M:%S %p') 
        revenue = row["revenue"] 
        sql = f"UPDATE conversions SET traffic_click_id='{mgid_click_id}' AND traffic_campaign_id='{mgid_campaign_id}' AND voluum_campaign_id='{vol_campaign_id}' WHERE traffic_click_id is NULL AND voluum_click_id='{vol_click_id}'" 
        mycursor.execute(sql) 
        if mycursor.rowcount == 0: 
            sql = f"SELECT COUNT(*) FROM conversions WHERE voluum_click_id='{vol_click_id}' AND conversion_type='{conversion_type}'" 
            mycursor.execute(sql) 
            for count in mycursor: 
                if count[0] == 0: 
                    sql = f"INSERT INTO conversions (`id`, `conversion_date`, 'traffic_campaign_id', 'voluum_campaign_id, `traffic_click_id`, `voluum_click_id`,`conversion_type`,`conversion_revenue`) VALUES (NULL, '{postback_timestamp}', '{mgid_campaign_id}', '{vol_campaign_id}', '{mgid_click_id}', '{vol_click_id}', '{conversion_type}', '{revenue}')" 
                    mycursor.execute(sql) 
    
        mydb.commit() 



