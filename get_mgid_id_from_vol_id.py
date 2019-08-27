from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets

import pprint
pp=pprint.PrettyPrinter(indent=2)

def get_mgid_id_from_vol_id(vol_id):

    campaign_sets = create_complete_campaign_sets()

    for campaign_set in campaign_sets:
        if campaign_set['vol_campaign_id'] != vol_id:
            continue
        return campaign_set['mgid_campaign_id']

