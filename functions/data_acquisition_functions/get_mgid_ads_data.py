from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from datetime import datetime
import requests
import re
import sys

import pprint
pp=pprint.PrettyPrinter(indent=2)


def get_mgid_ads_data(token, mgid_client_id):
    try:
        # ads_data is a dictionary of ad ids. Each ad id is unique. The value of
        # each ad id is a dictionary of data for that ad, such as its id and image
        # name. All data retrieved is independent on a time period. 

        # The data need to be retrieved with multiple requests because mgid limits
        # each request to 1000 responses. For example, if there are 1050 ads, 2
        # requests are needed - the first request gets 1000 and the second gets 50.
        # The need for multiple requests is handled by a while loop. 
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
                # ads_data is a dictionary of ad ids. Each ad id is a dictionary of data
                # for that ad. 
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
        
        return ads_data
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_ads_data")
        send_email("brianshaller@gmail.com", "Failed - get_mgid_ads_data() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

