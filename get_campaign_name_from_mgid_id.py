from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets

import pprint
pp=pprint.PrettyPrinter(indent=2)

def get_campaign_name_from_mgid_id(mgid_id):

    campaign_sets = create_complete_campaign_sets()

    for campaign_set in campaign_sets:
        if campaign_set['mgid_campaign_id'] != mgid_id:
            continue
        return campaign_set['campaign_name']

