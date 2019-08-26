import requests
from datetime import datetime, timedelta
import pytz
import sys
import mysql.connector
from config.config import *
from create_complete_campaign_sets import create_complete_campaign_sets

import pprint
pp=pprint.PrettyPrinter(indent=2)

def set_cost_widgets(days_ago):
    ################
    # get mgid token
    
    res = requests.post("https://api.mgid.com/v1/auth/token",
            headers={"Content-type": "application/x-www-form-urlencoded",
                     "Cache-Control": "no-cache"},
             data={"email": mgid_login, "password": mgid_password})
    
    token = res.json()["token"] 
    
    ###############
    #mgid dates
    
    # days_ago = 1
    timezone = 'america/los_angeles'
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    # for mgid, the end date is inclusive, so the end date needs to be
    # yesterday in order to include yesterdays data.
    end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    
    start_date = start_date_pst.strftime("%Y-%m-%d")
    end_date = end_date_pst.strftime("%Y-%m-%d")

    date_to_put_in_sql = start_date_pst
    
    ##################
    # set up mysql
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="ulan",
      passwd="missoula1",
      database="ulanmedia"
    )
    
    mycursor = mydb.cursor()
    
    ##################
    # get data from mgid
    
    complete_campaign_sets = create_complete_campaign_sets()
    
    for campaign_set in complete_campaign_sets:
        mgid_campaign_id = campaign_set['mgid_campaign_id']
        vol_campaign_id = campaign_set['vol_campaign_id']
        campaign_name = campaign_set['campaign_name']
    
    
        url = f"https://api.mgid.com/v1/goodhits/campaigns/{mgid_campaign_id}/quality-analysis?token={token}&campaignId={mgid_campaign_id}&dateInterval=interval&startDate={start_date}&endDate={end_date}";
        res = requests.get(url) 
        res.raise_for_status()
        res = res.json()
    
        widgets_data = {}
        if res[mgid_campaign_id][start_date + "_" + end_date] == []:
            return widgets_data
        for id, data in res[mgid_campaign_id][start_date + "_" + end_date].items():
            widget_id = id
            if data["sources"]:
                for source_id, source_data in data["sources"].items():
                    if source_id is not "0":
                        widget_id = f"{id}s{source_id}"
                    if source_data['spent'] == 0:
                        continue
                         
                    widgets_data[widget_id] = {"widget_id": widget_id, "clicks":
                    source_data["clicks"], "cost": source_data["spent"],
                    "coeff": source_data["qualityFactor"], "cpc": source_data["cpc"]}
            else: 
                if data['spent'] == 0:
                    continue
                widgets_data[widget_id] = {"widget_id": widget_id, "clicks":
                        data["clicks"], "cost": data["spent"],
                        "coeff": data["qualityFactor"], "cpc":
                        data["cpc"]}
    
        for widget in widgets_data.values():
        
            sql = f"INSERT INTO cost_widgets(cost_date, voluum_campaign_id, traffic_campaign_id, traffic_campaign_name, traffic_widget_id, traffic_widget_cpc, traffic_widget_coefficient, traffic_widget_clicks, traffic_widget_cost) VALUES('{date_to_put_in_sql}', '{vol_campaign_id}', '{mgid_campaign_id}', '{campaign_name}', '{str(widget['widget_id'])}', '{str(widget['cpc'])}', '{str(widget['coeff'])}', '{str(widget['clicks'])}', '{str(widget['cost'])}')"
            mycursor.execute(sql)
    
            mydb.commit()

set_cost_widgets(1)
