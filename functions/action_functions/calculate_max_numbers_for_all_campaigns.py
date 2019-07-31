from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.send_email import send_email
import os
import json
import sys


def calculate_max_numbers_for_all_campaigns():

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_all_campaigns/oneeighty_campaigns_for_all_campaigns_dataset.json', 'r') as file:
        json_file = json.load(file)

    # create a dictionary of campaign sets
    # keys are vol_id, values are all the data for each campaign in campaign
    # sets
    campaigns = get_campaign_sets()
    campaigns_dict = {}
    for campaign in campaigns:
        campaigns_dict[campaign["vol_id"]] = campaign

    for campaign in json_file["data"]:
        name = campaign["name"]
        vol_id = campaign["vol_id"]
        revenue = campaign["revenue"]
        clicks = campaign["clicks"]
        leads = campaign["leads"]
        sales = campaign["sales"]
        print("###################")
        print(f"campaign name: {name}") 
        if clicks == 0:
            print(f"recommended maxBid (EPC): 0") 
        else:
            print(f"recommended maxBid (EPC): {revenue/clicks}") 
        if leads == 0:
            print(f"recommended maxLeadCPA (EPL): 0") 
            print(f"current maxLeadCPA: {campaigns_dict[vol_id]['max_lead_cpa']}") 
        else:
            print(f"recommended maxLeadCPA (EPL): {revenue/leads}") 
            print(f"current maxLeadCPA: {campaigns_dict[vol_id]['max_lead_cpa']}") 
        if sales == 0:
            print(f"recommended maxSaleCPA = EPS: 0") 
            print(f"current maxSaleCPA: {campaigns_dict[vol_id]['max_sale_cpa']}") 
        else:
            print(f"recommended maxSaleCPA = EPS: {revenue/sales}") 
            print(f"current maxSaleCPA: {campaigns_dict[vol_id]['max_sale_cpa']}") 
        print("###################")
        

calculate_max_numbers_for_all_campaigns()



            


