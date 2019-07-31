from config.config import *
from config.mgid_token import mgid_token
from functions.classification_functions.classify_campaign_for_one_p_or_c_widget import classify_campaign_for_one_p_or_c_widget
from functions.classification_functions.classify_p_widget_for_all_campaigns import classify_p_widget_for_all_campaigns
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.data_acquisition_functions.get_mgid_included_widgets_by_campaign import get_mgid_included_widgets_by_campaign
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
import json
import os
import re
import sys

def create_complete_p_widgets_dataset(date_range, output_name):

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

    complete_p_widgets = {}

    #########################################################

    # 3. create the "for_all_campaigns" part of each p widget

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        pattern = re.compile(r'\d*')

        for widget in json_file["data"]:
           p_widget = pattern.search(widget).group()
           if p_widget in complete_p_widgets:
               complete_p_widgets[p_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               complete_p_widgets[p_widget] = {"for_all_campaigns": {}}
               complete_p_widgets[p_widget]["for_all_campaigns"] = json_file["data"][widget]
               complete_p_widgets[p_widget]["for_all_campaigns"]["widget_id"] = p_widget

               if p_widget in widget_whitelist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_whitelist" 
               elif p_widget in widget_greylist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_greylist" 
               elif p_widget in widget_blacklist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_blacklist" 
               else:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "waiting" 

           if widget is not p_widget:
               complete_p_widgets[p_widget]["for_all_campaigns"]["has_children"] = True
           else:
               complete_p_widgets[p_widget]["for_all_campaigns"]["has_children"] = False


    #########################################################

    # 4.  create the "for_each_campaign" part of each p widget
    
    for p_widget in complete_p_widgets:
        complete_p_widgets[p_widget]["for_each_campaign"] = []
    
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        mgid_id = campaign["mgid_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        included_widgets = get_mgid_included_widgets_by_campaign(mgid_token,
                mgid_id, mgid_start_date, mgid_end_date)
        excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, mgid_id)

        mpc_pattern = re.compile(r'.*cpc_(.*)')
        p_widgets_for_one_campaign = {}
        for widget in json_file["data"]:
            p_widget = pattern.search(widget).group()
            if p_widget in p_widgets_for_one_campaign:
                p_widgets_for_one_campaign[p_widget]["clicks"] += json_file["data"][widget]["clicks"]
                p_widgets_for_one_campaign[p_widget]["cost"] += json_file["data"][widget]["cost"]
                p_widgets_for_one_campaign[p_widget]["revenue"] += json_file["data"][widget]["revenue"]
                p_widgets_for_one_campaign[p_widget]["leads"] += json_file["data"][widget]["leads"]
                p_widgets_for_one_campaign[p_widget]["sales"] += json_file["data"][widget]["sales"]
            else:
                p_widgets_for_one_campaign[p_widget] = json_file["data"][widget]
                p_widgets_for_one_campaign[p_widget]["widget_id"] = p_widget
                if p_widget in excluded_widgets:
                    p_widgets_for_one_campaign[p_widget]['status'] = "excluded" 
                elif p_widget in included_widgets:
                    p_widgets_for_one_campaign[p_widget]['status'] = "included" 
                else:
                    p_widgets_for_one_campaign[p_widget]['status'] = "inactive" 
                #############
                # hardcoded inactive
                # this is for when the mgid api shows clicks for a campaign
                # widget, but the mgid web dashboard doesn't show any clicks for
                # the same campaign widget, even though the date range is the
                # same. 
                # These should manually removed after enough time has passed
                # for the api to no longer show any clicks for the campaign
                # widget
                hardcoded_campaigns = ["506299", "506320", "506244", "506323"]
                hardcoded_p_widgets = ["5722923"]
                if p_widgets_for_one_campaign[p_widget]["widget_id"] in hardcoded_p_widgets and mgid_id in hardcoded_campaigns:
                    p_widgets_for_one_campaign[p_widget]['status'] = "inactive" 
                ############
                ############
                ############
                p_widgets_for_one_campaign[p_widget]["vol_id"] = campaign["vol_id"]
                p_widgets_for_one_campaign[p_widget]["mgid_id"] = campaign["mgid_id"]
                p_widgets_for_one_campaign[p_widget]["name"] = campaign["name"]
                p_widgets_for_one_campaign[p_widget]["mpl"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[p_widget]["mps"] = campaign["max_sale_cpa"]
                res = mpc_pattern.findall(campaign["name"])
                p_widgets_for_one_campaign[p_widget]["c_bid"] = float(list(res)[0])
                p_widgets_for_one_campaign[p_widget]["w_bid"] = p_widgets_for_one_campaign[p_widget]["c_bid"] * p_widgets_for_one_campaign[p_widget]["coeff"]

        for p_widget in p_widgets_for_one_campaign:
            if complete_p_widgets[p_widget]["for_each_campaign"]:
                complete_p_widgets[p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                complete_p_widgets[p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]

    #################################################################33
     
    # 5. Create the "campaign_counts" part of each p widget
    
    for p_widget in complete_p_widgets:
        complete_p_widgets[p_widget]["good_campaigns_count"] = 0
        complete_p_widgets[p_widget]["bad_campaigns_count"] = 0
        complete_p_widgets[p_widget]["wait_campaigns_count"] = 0

    for p_widget in complete_p_widgets:
        total_sales = complete_p_widgets[p_widget]["for_all_campaigns"]["sales"]
        complete_p_widgets[p_widget]["for_all_campaigns"]["has_bad_and_included_campaigns"] = False
        for campaign in complete_p_widgets[p_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/not
            # yet
            # counts are recorded
            classification = classify_campaign_for_one_p_or_c_widget(campaign, total_sales)
            campaign["classification"] = classification
            if classification == "good":
               complete_p_widgets[p_widget]["good_campaigns_count"] += 1
            elif classification == "half good": 
               complete_p_widgets[p_widget]["good_campaigns_count"] += .5 
            elif classification == "bad": 
               complete_p_widgets[p_widget]["bad_campaigns_count"] += 1 
               if campaign["status"] == "included":
                   complete_p_widgets[p_widget]["for_all_campaigns"]["has_bad_and_included_campaigns"] = True
            elif classification == "half bad": 
               complete_p_widgets[p_widget]["bad_campaigns_count"] += .5 
            elif classification == "wait": 
               complete_p_widgets[p_widget]["wait_campaigns_count"] += 1

    #############################################################

    # 6. create is_bad_and_included variable for each campaign

    for p_widget in complete_p_widgets:
        for campaign in complete_p_widgets[p_widget]["for_each_campaign"]:
            if (campaign["classification"] == "bad") & (campaign["status"] ==
                    "included"):
                campaign["is_bad_and_included"] = True
            else:
                campaign["is_bad_and_included"] = False

    #############################################################

    # 7. create the classification of each p widget

    for p_widget in complete_p_widgets.values():
        p_widget["for_all_campaigns"]["classification"] = classify_p_widget_for_all_campaigns(p_widget)

    #############################################################

    # 8. create has_mismatch_classification_and_global_status variable in
    # "for_all_campaigns"

    for p_widget in complete_p_widgets.values():
        if (p_widget['for_all_campaigns']['classification'] != "wait") & (p_widget["for_all_campaigns"]["global_status"] != f"p_{p_widget['for_all_campaigns']['classification']}list"):
            p_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"] = True
        else:
            p_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"] = False

    ###########################################################

    # add domains, if possible

    with open(f'{os.environ.get("ULANMEDIAAPP")}/curated_lists/widget_domains/widget_domains.json', 'r') as file:
            widget_domains_lookup = json.load(file)
    for p_widget in complete_p_widgets:

        if p_widget in widget_domains_lookup:
            complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] = ""
            for domain in widget_domains_lookup[p_widget]:
                if complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] == "":
                    complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] = domain
                else:
                    complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] = complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] + "," + domain
        else:
            complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] = ""

    
    #############################################################

    # 9. Save complete_p_widgets to a json file and return it as a
    # json file 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_p_widgets/{output_name}.json", "w") as file:
        json.dump(complete_p_widgets, file)

    return complete_p_widgets

