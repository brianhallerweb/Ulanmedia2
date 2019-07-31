from config.config import *
import os
import json

def create_campaigns_for_good_p_widgets_dataset(date_range, max_rec_bid, default_coeff):
    max_rec_bid = float(max_rec_bid)
    default_coeff = float(default_coeff)

    with open(f'{os.environ.get("ULANMEDIAAPP")}/curated_lists/good_widgets/good_widgets.json', 'r') as file:
       good_widgets = json.load(file)

    campaigns_for_good_p_widgets = []

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for p_widget in data:
        if p_widget not in good_widgets:
            continue
        for campaign in data[p_widget]["for_each_campaign"]:
            campaign["global_status"] = data[p_widget]["for_all_campaigns"]["global_status"]
            campaign["domain"] = data[p_widget]["for_all_campaigns"]["domain"]
            campaigns_for_good_p_widgets.append(campaign)

    for campaign in campaigns_for_good_p_widgets:
        sales = campaign["sales"]
        mpl = campaign["mpl"]
        if campaign["leads"] > 0:
            cpl = campaign["cost"]/campaign["leads"]
        if campaign["clicks"] > 0:
            epc = campaign["revenue"]/campaign["clicks"]
        c_bid = campaign["c_bid"]
        w_bid = campaign["w_bid"]
        coeff = campaign["coeff"]

        if sales > 0:
            campaign["rec_w_bid"] = epc - epc * .3
        elif campaign["leads"] > 0:
            campaign["rec_w_bid"] = c_bid * mpl / cpl / 2
        else:
            campaign["rec_w_bid"] = c_bid * default_coeff

        if campaign["rec_w_bid"] > max_rec_bid:
            campaign["rec_w_bid"] = max_rec_bid

        campaign["rec_coeff"] = campaign["rec_w_bid"] / c_bid
        
        rec_w_bid = campaign["rec_w_bid"]
        rec_coeff = campaign["rec_coeff"]

        if w_bid != rec_w_bid:
            campaign["mismatch_w_bid_and_rec_w_bid"] = True
        else:
            campaign["mismatch_w_bid_and_rec_w_bid"] = False

        if coeff != rec_coeff:
            campaign["mismatch_coeff_and_rec_coeff"] = True
        else:
            campaign["mismatch_coeff_and_rec_coeff"] = False

        
    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json", "w") as file:
        json.dump(campaigns_for_good_p_widgets, file)

    return json.dumps(campaigns_for_good_p_widgets)
