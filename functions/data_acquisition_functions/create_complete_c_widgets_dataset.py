from config.config import *
from config.mgid_token import mgid_token
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.data_acquisition_functions.get_mgid_included_widgets_by_campaign import get_mgid_included_widgets_by_campaign
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.classification_functions.classify_campaign_for_one_p_or_c_widget import classify_campaign_for_one_p_or_c_widget
from functions.classification_functions.classify_c_widget_for_all_campaigns import classify_c_widget_for_all_campaigns
import re
import os
import sys
import json

def create_complete_c_widgets_dataset(date_range, output_name):
    
    # 1. get some prerequisite data

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    # these dates are only used for determining status = included. 
    # that is why they are hard coded to 90 days
    mgid_dates = create_mgid_date_range(90, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]

    ########################################################

    # 2. set up the basic data structure you want to create

    complete_c_widgets = {}

    #########################################################

    # 3. create the "for_all_campaigns" part of each c widget

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        c_widget_pattern = re.compile(r'.*s.*')
        p_widget_pattern = re.compile(r'\d*')

        for widget in json_file["data"]:
           c_widget = c_widget_pattern.search(widget)
           if c_widget == None:
               continue
           c_widget = c_widget.group()
           p_widget = p_widget_pattern.search(widget).group()

           if c_widget in complete_c_widgets:
               complete_c_widgets[c_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               complete_c_widgets[c_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               complete_c_widgets[c_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               complete_c_widgets[c_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               complete_c_widgets[c_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               complete_c_widgets[c_widget] = {"for_all_campaigns": {}}
               complete_c_widgets[c_widget]["for_all_campaigns"] = json_file["data"][widget]
               complete_c_widgets[c_widget]["for_all_campaigns"]["widget_id"] = c_widget

               if p_widget in widget_whitelist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "p_whitelist" 
               elif p_widget in widget_greylist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "p_greylist" 
               elif p_widget in widget_blacklist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "p_blacklist" 
                   
               if c_widget in widget_whitelist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "c_whitelist" 
               elif c_widget in widget_greylist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "c_greylist" 
               elif c_widget in widget_blacklist:
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "c_blacklist" 

               if (c_widget in widget_whitelist) & (p_widget in widget_whitelist):
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "pc_whitelist" 
               elif (c_widget in widget_greylist) & (p_widget in widget_greylist):
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "pc_greylist" 
               elif (c_widget in widget_blacklist) & (p_widget in widget_blacklist):
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "pc_blacklist" 

               if (c_widget not in widget_whitelist) & (p_widget not in
                   widget_whitelist) & (c_widget not in widget_greylist) & (p_widget not in widget_greylist) & (c_widget not in widget_blacklist) & (p_widget not in widget_blacklist):
                   complete_c_widgets[c_widget]["for_all_campaigns"]['global_status'] = "waiting" 


    #########################################################

    # 5. 
    
    for c_widget in complete_c_widgets:
        complete_c_widgets[c_widget]["for_each_campaign"] = []
    
    for campaign in campaigns:
        vol_id = campaign["vol_id"]
        mgid_id = campaign["mgid_id"]
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             json_file = json.load(file)

        included_widgets = get_mgid_included_widgets_by_campaign(mgid_token,
                mgid_id, mgid_start_date, mgid_end_date)
        excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, mgid_id)

        c_widgets_for_one_campaign = {}
        c_widget_pattern = re.compile(r'.*s.*')
        p_widget_pattern = re.compile(r'\d*')
        mpc_pattern = re.compile(r'.*cpc_(.*)')
        for widget in json_file["data"]:
           c_widget = c_widget_pattern.search(widget)
           if c_widget == None:
               continue
           c_widget = c_widget.group()
           p_widget = p_widget_pattern.search(widget).group()
           if c_widget in c_widgets_for_one_campaign:
                c_widgets_for_one_campaign[c_widget]["clicks"] += json_file["data"][widget]["clicks"]
                c_widgets_for_one_campaign[c_widget]["cost"] += json_file["data"][widget]["cost"]
                c_widgets_for_one_campaign[c_widget]["revenue"] += json_file["data"][widget]["revenue"]
                c_widgets_for_one_campaign[c_widget]["leads"] += json_file["data"][widget]["leads"]
                c_widgets_for_one_campaign[c_widget]["sales"] += json_file["data"][widget]["sales"]
           else:
                c_widgets_for_one_campaign[c_widget] = json_file["data"][widget]
                if c_widget in excluded_widgets or p_widget in excluded_widgets:
                    c_widgets_for_one_campaign[c_widget]['status'] = "excluded"
                elif c_widget in included_widgets or p_widget in included_widgets:
                    c_widgets_for_one_campaign[c_widget]['status'] = "included"
                else:
                    c_widgets_for_one_campaign[c_widget]['status'] = "inactive"
                c_widgets_for_one_campaign[c_widget]["vol_id"] = campaign["vol_id"]
                c_widgets_for_one_campaign[c_widget]["mgid_id"] = campaign["mgid_id"]
                c_widgets_for_one_campaign[c_widget]["name"] = campaign["name"]
                c_widgets_for_one_campaign[c_widget]["mpl"] = campaign["max_lead_cpa"]
                c_widgets_for_one_campaign[c_widget]["mps"] = campaign["max_sale_cpa"]
                res = mpc_pattern.findall(campaign["name"])
                c_widgets_for_one_campaign[c_widget]["c_bid"] = float(list(res)[0])
                c_widgets_for_one_campaign[c_widget]["w_bid"] = c_widgets_for_one_campaign[c_widget]["c_bid"] * c_widgets_for_one_campaign[c_widget]["coeff"]

        for c_widget in c_widgets_for_one_campaign:
            if complete_c_widgets[c_widget]["for_each_campaign"]:
                complete_c_widgets[c_widget]["for_each_campaign"].append(c_widgets_for_one_campaign[c_widget])
            else:
                complete_c_widgets[c_widget]["for_each_campaign"] = [c_widgets_for_one_campaign[c_widget]]



    #################################################################33
     
    # 5. Create the "campaign_counts" part of each c widget
    
    for c_widget in complete_c_widgets:
        complete_c_widgets[c_widget]["good_campaigns_count"] = 0
        complete_c_widgets[c_widget]["bad_campaigns_count"] = 0
        complete_c_widgets[c_widget]["wait_campaigns_count"] = 0

    for c_widget in complete_c_widgets:
        total_sales = complete_c_widgets[c_widget]["for_all_campaigns"]["sales"]
        complete_c_widgets[c_widget]["for_all_campaigns"]["has_bad_and_included_campaigns"] = False
        for campaign in complete_c_widgets[c_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/wait counts are recorded
            classification = classify_campaign_for_one_p_or_c_widget(campaign, total_sales)
            campaign["classification"] = classification
            if classification == "good":
               complete_c_widgets[c_widget]["good_campaigns_count"] += 1
            elif classification == "half good": 
               complete_c_widgets[c_widget]["good_campaigns_count"] += .5 
            elif classification == "bad": 
               complete_c_widgets[c_widget]["bad_campaigns_count"] += 1 
               if campaign["status"] == "included":
                   complete_c_widgets[c_widget]["for_all_campaigns"]["has_bad_and_included_campaigns"] = True
            elif classification == "half bad": 
               complete_c_widgets[c_widget]["bad_campaigns_count"] += .5 
            elif classification == "wait": 
               complete_c_widgets[c_widget]["wait_campaigns_count"] += 1


    #############################################################
    
    # 6. create isBadAndIncluded variable for each campaign

    for c_widget in complete_c_widgets:
        for campaign in complete_c_widgets[c_widget]["for_each_campaign"]:
            if (campaign["classification"] == "bad") & (campaign["status"] ==
                    "included"):
                campaign["is_bad_and_included"] = True
            else:
                campaign["is_bad_and_included"] = False

    #############################################################

    # 7. Classify the c widget

    for c_widget in complete_c_widgets.values():
        c_widget["for_all_campaigns"]["classification"] = classify_c_widget_for_all_campaigns(c_widget)

    #############################################################

    # 8. create hasMismatchClassificationAndGlobalStatus variable in
    # "for_all_campaigns"

    for c_widget in complete_c_widgets.values():
        if (c_widget['for_all_campaigns']['classification'] != "wait") & ((c_widget["for_all_campaigns"]["global_status"] != f"p_{c_widget['for_all_campaigns']['classification']}list") & (c_widget["for_all_campaigns"]["global_status"] != f"c_{c_widget['for_all_campaigns']['classification']}list") & (c_widget["for_all_campaigns"]["global_status"] != f"pc_{c_widget['for_all_campaigns']['classification']}list")):
            c_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"] = True
        else:
            c_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"] = False

    ###########################################################

    # add domains, if possible

    with open(f'{os.environ.get("ULANMEDIAAPP")}/curated_lists/widget_domains/widget_domains.json', 'r') as file:
        widget_domains_lookup = json.load(file)

    p_widget_pattern = re.compile(r'\d*')

    for c_widget in complete_c_widgets:

        p_widget = p_widget_pattern.search(c_widget).group()

        if p_widget in widget_domains_lookup:
            complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] = ""
            for domain in widget_domains_lookup[p_widget]:
                if complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] == "":
                    complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] = domain
                else:
                    complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] = complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] + "," + domain
        else:
            complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] = ""


    ############################################################

    # 9. Save complete_p_widgets to a json file and return it as a
    # json file 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_c_widgets/{output_name}.json", "w") as file:
        json.dump(complete_c_widgets, file)

    return complete_c_widgets



