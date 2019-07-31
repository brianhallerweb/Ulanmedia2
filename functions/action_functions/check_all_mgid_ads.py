from config.config import *
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from functions.misc.send_email import send_email
import requests


def check_all_mgid_ads(token):
    request_number = 0
    ads_data = {}
    while len(ads_data) == request_number * 700:
        url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/teasers?token={token}&limit=700&start={request_number * 700}";
        request_number = request_number + 1
        res = requests.get(url)
        if res.status_code == 401:
            mgid_token = get_and_return_new_mgid_token()
            return check_all_mgid_ads(mgid_token)
        res.raise_for_status()
        res = res.json()
        if len(res) == 0:
            break
        for ad_id in res:
            ads_data[ad_id] = res[ad_id]


    ad_status_counts = {"active": 0,
            "paused": 0, "rejected": 0}
    rejected_ads = {}
    for ad_id in ads_data:
        if (ads_data[ad_id]["status"]["code"] == 'goodPerformance'):
            ad_status_counts["active"] += 1
        elif (ads_data[ad_id]["status"]["code"] == 'new'):
            ad_status_counts["active"] += 1
        elif (ads_data[ad_id]["status"]["code"] == 'campaignBlocked'):
            ad_status_counts["paused"] += 1
        elif (ads_data[ad_id]["status"]["code"] == 'blocked'):
            ad_status_counts["paused"] += 1
        else:
            ad_status_counts["rejected"] += 1
            rejected_ads[ad_id] = {"ad_id": ad_id, "campaign_id":
                    ads_data[ad_id]["campaignId"]}


    subject = f"ok - {len(ads_data)} ads: {ad_status_counts['active']} active, {ad_status_counts['paused']} paused, {ad_status_counts['rejected']} rejected"
    body = f"{ad_status_counts['active']} of {len(ads_data)} ads in all campaigns are active.\n{ad_status_counts['paused']} of {len(ads_data)} ads in all campaigns are paused.\n{ad_status_counts['rejected']} of {len(ads_data)} ads in all campaigns are rejected."
    if ad_status_counts["rejected"] > 0:
        subject = f"ALERT - {len(ads_data)} ads: {ad_status_counts['active']} active, {ad_status_counts['paused']} paused, {ad_status_counts['rejected']} rejected"
        for ad_id in rejected_ads:
            body += f'\n\nad {rejected_ads[ad_id]["ad_id"]} rejected in campaign {rejected_ads[ad_id]["campaign_id"]}\nhttps://dashboard.mgid.com/advertisers/teasers-goods/campaign_id/{rejected_ads[ad_id]["campaign_id"]}'
    print(subject)
    print(body)
    send_email("brianshaller@gmail.com", subject, body)
    send_email("mikeseo@gmail.com", subject, body)


            


