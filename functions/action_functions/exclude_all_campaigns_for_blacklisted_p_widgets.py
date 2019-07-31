from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.misc.send_email import send_email
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
import re
import os
import sys
import json

def exclude_all_campaigns_for_blacklisted_p_widgets(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)

    emails_sent = 0
    for p_widget in complete_p_widgets.values():
        if p_widget["for_all_campaigns"]["global_status"] == "p_blacklist":
            for campaign in p_widget["for_each_campaign"]:
                if campaign["status"] == "included":
                    subject = 'ALERT - found an "included" campaign in a blacklisted widget' 
                    message = f'found an included campaign on a blacklisted p widget:\np widget id {p_widget["for_all_campaigns"]["widget_id"]}\ncampaign {campaign["mgid_id"]}\nhttps://ulanmedia.brianhaller.net/campaignsforonepwidget/{p_widget["for_all_campaigns"]["widget_id"]}'
                    print(message)
                    emails_sent += 1
                    send_email("brianshaller@gmail.com", subject, message)
                    send_email("mikeseo@gmail.com", subject, message)

    if emails_sent == 0:
        # send email saying no "included" campaigns on blacklisted widgets were found. 
        message = 'ok - campaigns for blacklisted widgets are all excluded'
        print(message)
        send_email("brianshaller@gmail.com", message, message)
        send_email("mikeseo@gmail.com", message, message)



# def exclude_all_campaigns_for_blacklisted_p_widgets(date_range):
    # campaigns = get_campaign_sets()
    # widget_whitelist = get_whitelist()
    # widget_greylist = get_greylist()
    # widget_blacklist = get_blacklist()

    # p_widgets_for_all_campaigns = {}

    # for campaign in campaigns:
        # vol_id = campaign["vol_id"] 
        # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            # json_file = json.load(file)


        # pattern = re.compile(r'\d*')
        # for widget in json_file["data"]:
           # parent_widget = pattern.search(widget).group()
           # if parent_widget in p_widgets_for_all_campaigns:
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           # else:
               # p_widgets_for_all_campaigns[parent_widget] = {"for_all_campaigns": {}, "for_each_campaign": []}
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"] = json_file["data"][widget]
               # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["widget_id"] = parent_widget

               # if parent_widget in widget_whitelist:
                   # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "p_whitelist" 
               # elif parent_widget in widget_greylist:
                   # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "p_greylist" 
               # elif parent_widget in widget_blacklist:
                   # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "p_blacklist" 
               # else:
                   # p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "not yet listed" 




        # # for each campaign, accumulate c widgets for one p widget together
        # # into one p widget
        # # The result of this is that p_widgets_for_one_campaign is a dictionary
        # # of individual p_widgets in one campaign. 
        # # 1/14/19 I'm not sure why I have to load the file again here but I was
        # # having some unexpected results when I tried to reuse the file data
        # # that was loaded in the previous step. It's as if that data was
        # # mutated in some way, but I don't see how that is possible. Anyway, it
        # # works properly when I reload the data at this step. 
        # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            # json_file = json.load(file)

        # p_widgets_for_one_campaign = {}
        # for widget in json_file["data"]:
            # parent_widget = pattern.search(widget).group()
            # if parent_widget in p_widgets_for_one_campaign:
                # p_widgets_for_one_campaign[parent_widget]["clicks"] += json_file["data"][widget]["clicks"]
                # p_widgets_for_one_campaign[parent_widget]["cost"] += json_file["data"][widget]["cost"]
                # p_widgets_for_one_campaign[parent_widget]["revenue"] += json_file["data"][widget]["revenue"]
                # p_widgets_for_one_campaign[parent_widget]["leads"] += json_file["data"][widget]["leads"]
                # p_widgets_for_one_campaign[parent_widget]["sales"] += json_file["data"][widget]["sales"]
            # else:
                # p_widgets_for_one_campaign[parent_widget] = json_file["data"][widget]
                # p_widgets_for_one_campaign[parent_widget]["mgid_id"] = campaign["mgid_id"]
                # p_widgets_for_one_campaign[parent_widget]["widget_id"] = parent_widget
                

        # # Add each p_widget_for_one_campaign to the list of campaigns for each p widget
        # for p_widget in p_widgets_for_one_campaign:
            # if p_widgets_for_all_campaigns[p_widget]["for_each_campaign"]:
                # p_widgets_for_all_campaigns[p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            # else:
                # p_widgets_for_all_campaigns[p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]


    # ############################################################
    # # At this point, p_widgets_for_all_campaigns["data"] is a dictionary of
    # # p_widgets, each with accumulated data for all campaigns (the
    # # "for_all_campaigns" value) and data for each campaign (the
    # # "for_each_campaign" value)
     
    # # loop through each campaign and look for blacklisted p widgets with
    # # "included" campaigns

    # # emails_sent acts as a counter for the number of found blacklisted p
    # # wicdgets with included campaigns. The count is only important because if
    # # > 0, which is what it will be most days, I need to send an email that
    # # says all is well. 
    # emails_sent = 0
    # for p_widget in p_widgets_for_all_campaigns.values():
        # if p_widget["for_all_campaigns"]["global_status"] == "p_blacklist":
            # for campaign in p_widget["for_each_campaign"]:
                # if campaign["status"] == "included":
                    # message = f'found an included campaign on a blacklisted p widget:\np widget id {p_widget["for_all_campaigns"]["widget_id"]}\ncampaign {campaign["mgid_id"]}'
                    # print(message)
                    # emails_sent += 1
                    # send_email("brianshaller@gmail.com", 'ALERT - found an "included" campaign in a blacklisted widget', message)

    # if emails_sent == 0:
        # # send email saying no "included" campaigns on blacklisted widgets
        # # were found. 
        # message = 'ok - campaigns for blacklisted widgets are all excluded'
        # print(message)
        # send_email("brianshaller@gmail.com", message, message)
        # send_email("mikeseo@gmail.com", message, message)

