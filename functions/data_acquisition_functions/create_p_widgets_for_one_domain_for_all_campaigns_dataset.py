from config.config import *
import json
import sys
import re
import os

def create_p_widgets_for_one_domain_for_all_campaigns_dataset(date_range, domain):
    
    domains_to_check = domain.split(",")

    p_widgets_for_one_domain_for_all_campaigns = {"metadata": {"vol_start_date":
        "none", "vol_end_date":
        "none"}, "data": {}}

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)
    
    for p_widget in complete_p_widgets:
        domains_to_match = complete_p_widgets[p_widget]["for_all_campaigns"]["domain"].split(",")
        for domain_to_check in domains_to_check:
            if domain_to_check in domains_to_match:
                p_widgets_for_one_domain_for_all_campaigns["data"][p_widget] = complete_p_widgets[p_widget]["for_all_campaigns"]
                p_widgets_for_one_domain_for_all_campaigns["data"][p_widget]["good_campaigns_count"] = complete_p_widgets[p_widget]["good_campaigns_count"]
                p_widgets_for_one_domain_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] = complete_p_widgets[p_widget]["bad_campaigns_count"]
                p_widgets_for_one_domain_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] = complete_p_widgets[p_widget]["wait_campaigns_count"]
                break

    if len(domain) > 20:
        domain = domain[:20]

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/p_widgets_for_one_domain_for_all_campaigns/{date_range}_{domain}_p_widgets_for_one_domain_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_domain_for_all_campaigns, file)

    return json.dumps(p_widgets_for_one_domain_for_all_campaigns)


