from config.config import *
import os
import json

def create_c_widgets_for_one_campaign_dataset(vol_id, date_range,
        max_rec_bid):

    max_rec_bid = float(max_rec_bid)

    c_widgets_for_one_campaign = {"metadata": {},
                                 "data": [] 
                                } 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    c_widgets_for_one_campaign["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    c_widgets_for_one_campaign["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    c_widgets_for_one_campaign["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    c_widgets_for_one_campaign["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_c_widgets/{date_range}_complete_c_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for c_widget in data:
        for campaign in data[c_widget]["for_each_campaign"]:
            if campaign["vol_id"] == vol_id:
                campaign["global_status"] = data[c_widget]["for_all_campaigns"]["global_status"]
                campaign["domain"] = data[c_widget]["for_all_campaigns"]["domain"]
                c_widgets_for_one_campaign["data"].append(campaign)

    for c_widget in c_widgets_for_one_campaign["data"]:
        sales = c_widget["sales"]
        mpl = c_widget["mpl"]
        if c_widget["leads"] > 0:
            cpl = c_widget["cost"]/c_widget["leads"]
        if c_widget["clicks"] > 0:
            epc = c_widget["revenue"]/c_widget["clicks"]
        c_bid = c_widget["c_bid"]
        w_bid = c_widget["w_bid"]
        coeff = c_widget["coeff"]

        if sales > 0:
            c_widget["rec_w_bid"] = epc - epc * .3
        elif c_widget["leads"] > 0:
            # 6/4 there was a row with a lead and cpl=0, which doens't make
            # sense, so I just added this to stop the error. 
            if cpl == 0:
                c_widget["rec_w_bid"] = 0
            else:
                c_widget["rec_w_bid"] = c_bid * mpl / cpl / 2
        else:
            c_widget["rec_w_bid"] = c_bid

        if c_widget["rec_w_bid"] > max_rec_bid:
            c_widget["rec_w_bid"] = max_rec_bid

        c_widget["rec_coeff"] = c_widget["rec_w_bid"] / c_bid

        rec_w_bid = c_widget["rec_w_bid"]
        rec_coeff = c_widget["rec_coeff"]

        if w_bid != rec_w_bid:
            c_widget["mismatch_w_bid_and_rec_w_bid"] = True
        else:
            c_widget["mismatch_w_bid_and_rec_w_bid"] = False

        if coeff != rec_coeff:
            c_widget["mismatch_coeff_and_rec_coeff"] = True
        else:
            c_widget["mismatch_coeff_and_rec_coeff"] = False

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/c_widgets_for_one_campaign/{vol_id}_{date_range}_c_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(c_widgets_for_one_campaign, file)

    return json.dumps(c_widgets_for_one_campaign)
