from config.config import *
import os
import json

def create_p_widgets_for_one_campaign_dataset(vol_id, date_range,
        max_rec_bid):
    max_rec_bid = float(max_rec_bid)


    p_widgets_for_one_campaign = {"metadata": {},
                                 "data": [] 
                                } 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    p_widgets_for_one_campaign["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    p_widgets_for_one_campaign["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    p_widgets_for_one_campaign["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    p_widgets_for_one_campaign["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for p_widget in data:
        for campaign in data[p_widget]["for_each_campaign"]:
            if campaign["vol_id"] == vol_id:
                campaign["global_status"] = data[p_widget]["for_all_campaigns"]["global_status"]
                campaign["domain"] = data[p_widget]["for_all_campaigns"]["domain"]
                p_widgets_for_one_campaign["data"].append(campaign)

    for p_widget in p_widgets_for_one_campaign["data"]:
        sales = p_widget["sales"]
        mpl = p_widget["mpl"]
        if p_widget["leads"] > 0:
            cpl = p_widget["cost"]/p_widget["leads"]
        if p_widget["clicks"] > 0:
            epc = p_widget["revenue"]/p_widget["clicks"]
        c_bid = p_widget["c_bid"]
        w_bid = p_widget["w_bid"]
        coeff = p_widget["coeff"]

        if sales > 0:
            p_widget["rec_w_bid"] = epc - epc * .3
        elif p_widget["leads"] > 0:
            if cpl != 0:
                p_widget["rec_w_bid"] = c_bid * mpl / cpl / 2
            else:
                p_widget["rec_w_bid"] = c_bid
        else:
            p_widget["rec_w_bid"] = c_bid

        if p_widget["rec_w_bid"] > max_rec_bid:
            p_widget["rec_w_bid"] = max_rec_bid

        p_widget["rec_coeff"] = p_widget["rec_w_bid"] / c_bid

        rec_w_bid = p_widget["rec_w_bid"]
        rec_coeff = p_widget["rec_coeff"]

        if w_bid != rec_w_bid:
            p_widget["mismatch_w_bid_and_rec_w_bid"] = True
        else:
            p_widget["mismatch_w_bid_and_rec_w_bid"] = False

        if coeff != rec_coeff:
            p_widget["mismatch_coeff_and_rec_coeff"] = True
        else:
            p_widget["mismatch_coeff_and_rec_coeff"] = False

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)

    return json.dumps(p_widgets_for_one_campaign)
