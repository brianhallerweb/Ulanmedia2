from config.config import *
from datetime import datetime
import json
import sys
import re
import os
from functions.classification_functions.classify_offer_for_all_campaigns import classify_offer_for_all_campaigns
import pandas as pd

def create_gprs_for_each_p_offer_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json', 'r') as file:
        json_file = json.load(file)
    offers_for_each_flow_rule = json_file["data"]

    #####################################

    gprs_for_each_p_offer = {}   

    for flow_rule in offers_for_each_flow_rule:
        for offer in offers_for_each_flow_rule[flow_rule]:
            p_offer_name = offers_for_each_flow_rule[flow_rule][offer]["p_offer_name"]
            gpr = offers_for_each_flow_rule[flow_rule][offer]["gpr"]
            p_offer_profit = round(offers_for_each_flow_rule[flow_rule][offer]["p_offer_profit"], 2)
            p_offer_profit_rank = offers_for_each_flow_rule[flow_rule][offer]["p_offer_profit_rank"]
            gpr_formula = offers_for_each_flow_rule[flow_rule][offer]["gpr_formula"]
            roi_formula = offers_for_each_flow_rule[flow_rule][offer]["roi_formula"]
            cvr_formula = offers_for_each_flow_rule[flow_rule][offer]["cvr_formula"]
            if p_offer_name not in gprs_for_each_p_offer:
                gprs_for_each_p_offer[p_offer_name] = {"p_offer_name": p_offer_name,
                        "gpr": gpr, "p_offer_profit": p_offer_profit,
                        "p_offer_profit_rank": p_offer_profit_rank,
                        "gpr_formula": gpr_formula, "roi_formula": roi_formula,
                        "cvr_formula": cvr_formula}

    gprs_for_each_p_offer_list = []
    for p_offer_name in gprs_for_each_p_offer:
        gprs_for_each_p_offer_list.append(gprs_for_each_p_offer[p_offer_name])

    gprs_for_each_p_offer_list = pd.DataFrame(gprs_for_each_p_offer_list)
    gprs_for_each_p_offer_list = gprs_for_each_p_offer_list.sort_values("p_offer_profit", ascending=True)
    
    return json.dumps(gprs_for_each_p_offer_list[["p_offer_profit_rank",
        "p_offer_profit", "p_offer_name", "gpr", "gpr_formula", "roi_formula",
        "cvr_formula"]].to_dict("records"))


