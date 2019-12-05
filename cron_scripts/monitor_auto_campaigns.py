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
from utility_functions.send_email import send_email

import pprint
pp=pprint.PrettyPrinter(indent=2)

def monitor_auto_campaigns():
    try:
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
        start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(180)
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

        sql = f"SELECT DISTINCT traffic_campaign_id from auto_campaigns"

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

            url = f"https://api.mgid.com/v1/goodhits/campaigns/{campaign_id}/quality-analysis/?token={token}&dateInterval=interval&startDate={start_date}&endDate={end_date}"

            res = requests.get(url)
            res = res.json()
            for widget_id in res[campaign_id][f"{start_date}_{end_date}"]:
                # if widget_id == "5763297":
                    # print(res[campaign_id][f"{start_date}_{end_date}"][widget_id])
                cost = 0
                if "spent" in res[campaign_id][f"{start_date}_{end_date}"][widget_id]:
                    cost = res[campaign_id][f"{start_date}_{end_date}"][widget_id]["spent"]
                clicks = 0
                if "clicks" in res[campaign_id][f"{start_date}_{end_date}"][widget_id]:
                    clicks = res[campaign_id][f"{start_date}_{end_date}"][widget_id]["clicks"]
                leads = 0
                if "buy" in res[campaign_id][f"{start_date}_{end_date}"][widget_id]:
                    leads = res[campaign_id][f"{start_date}_{end_date}"][widget_id]["buy"]
                sales = 0
                if "decision" in res[campaign_id][f"{start_date}_{end_date}"][widget_id]:
                    sales = res[campaign_id][f"{start_date}_{end_date}"][widget_id]["decision"]
                

                #Rule 1)
                #Exclude any widget with no sales, no leads, and 2 or more clicks.
                #rule_name = 2_clicks_no_leads_no_sales_exclude_widget
                #For each widget in one campaign for last180days:
                #IF sales = 0
                #AND leads = 0
                #AND clicks > 1
                #THAN exclude widget
                #
                if (sales == 0) & (leads == 0) & (clicks > 1):
                    print(f"2_clicks_no_leads_no_sales_exclude_widget: exclude widget {widget_id}")
                    # url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{campaign_id}?token={token}";
                    # response = requests.patch(url, headers ={"Content-Type": "application/x-www-form-urlencoded", "Cache-Control": "no-cache"}, data = {"widgetsFilterUid": f"include,except,{widget_id}"})
                    continue
                #Rule 2)
                #Exclude any widget with no sales and with a leadCVR less than 0.25%
                #rule_name = leadcvr_lessthan_0.25_no_sales_exclude_widget
                #IF sales = 0
                #AND leads >= 1
                #AND leads/clicks < 0.25
                #THAN exclude widget
                if clicks != 0:
                    if (sales == 0) & (leads >= 1) & (leads/clicks < 0.25):
                        print(f"leadcvr_lessthan_0.25_no_sales_exclude_widget: exclude widget {widget_id}")
                        # url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{campaign_id}?token={token}";
                        # response = requests.patch(url, headers ={"Content-Type": "application/x-www-form-urlencoded", "Cache-Control": "no-cache"}, data = {"widgetsFilterUid": f"include,except,{widget_id}"})
                        continue
                
                #Rule 3)
                #Exclude any widget with no sales and cost over $250
                #rule_name = cost_morethan_250_no_sales_exclude_widget
                #IF sales = 0
                #AND cost >= 250
                #THAN exclude widget
                if (sales == 0) & (cost >= 250):
                    print(f"cost_morethan_250_no_sales_exclude_widget: exclude widget {widget_id}")
                    # url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{campaign_id}?token={token}";
                    # response = requests.patch(url, headers ={"Content-Type": "application/x-www-form-urlencoded", "Cache-Control": "no-cache"}, data = {"widgetsFilterUid": f"include,except,{widget_id}"})
                    continue
    except Exception as e:
        print("Failed - email sent")
        send_email("brianshaller@gmail.com", "Failed - monitor_auto_campaigns()", e)
        sys.exit()


monitor_auto_campaigns()
