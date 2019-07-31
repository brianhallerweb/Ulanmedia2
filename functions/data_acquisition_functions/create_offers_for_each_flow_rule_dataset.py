from config.config import *
from datetime import datetime
import json
import sys
import re
import os

def create_offers_for_each_flow_rule_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_campaign/{date_range}_offers_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ######################################

    # 1. create_offers_for_each_flow_rule_dataset

    flow_rules = []
    for campaign in data:
        for offer in data[campaign]:
            if data[campaign][offer]["flow_rule"] in flow_rules:
                continue
            else:
                flow_rules.append(data[campaign][offer]["flow_rule"])

    offers_for_each_flow_rule = {"metadata": metadata, "data": {}}
    for flow_rule in flow_rules:
        offers_for_each_flow_rule["data"][flow_rule] = {}

    for campaign in data:
        for offer in data[campaign]:
            flow_rule = data[campaign][offer]["flow_rule"]
            if offer in offers_for_each_flow_rule["data"][flow_rule]: 
                offers_for_each_flow_rule["data"][flow_rule][offer]["clicks"] += data[campaign][offer]["clicks"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["cost"] += data[campaign][offer]["cost"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["profit"] += data[campaign][offer]["profit"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["conversions"] += data[campaign][offer]["conversions"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["sales"] += data[campaign][offer]["sales"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["leads"] += data[campaign][offer]["leads"]
                offers_for_each_flow_rule["data"][flow_rule][offer]["revenue"] += data[campaign][offer]["revenue"]
            else:
                offers_for_each_flow_rule["data"][flow_rule][offer] = {
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "flow_rule_index": data[campaign][offer]["flow_rule_index"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"], 
                                                           "conversions": data[campaign][offer]["conversions"],
                                                           "sales": data[campaign][offer]["sales"],
                                                           "leads": data[campaign][offer]["leads"],
                                                           "revenue": data[campaign][offer]["revenue"],
                                                           "vol_weight": data[campaign][offer]["vol_weight"]
                                                          }

    # At this point, offers_for_each_flow_rule has been created
    #########################################
    
    # 2. create_p_offers_gpr_lookup

    c_offers_for_all_campaigns = {}

    for campaign in data:
        for offer in data[campaign]:
            if offer in c_offers_for_all_campaigns:
                c_offers_for_all_campaigns[offer]["clicks"] += data[campaign][offer]["clicks"]
                c_offers_for_all_campaigns[offer]["cost"] += data[campaign][offer]["cost"]
                c_offers_for_all_campaigns[offer]["profit"] += data[campaign][offer]["profit"]
                c_offers_for_all_campaigns[offer]["conversions"] += data[campaign][offer]["conversions"]
                c_offers_for_all_campaigns[offer]["sales"] += data[campaign][offer]["sales"]
                c_offers_for_all_campaigns[offer]["leads"] += data[campaign][offer]["leads"]
                c_offers_for_all_campaigns[offer]["revenue"] += data[campaign][offer]["revenue"]
            else:
                c_offers_for_all_campaigns[offer] = {
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "flow_rule_index": data[campaign][offer]["flow_rule_index"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"],
                                                           "conversions": data[campaign][offer]["conversions"],
                                                           "sales": data[campaign][offer]["sales"],
                                                           "leads": data[campaign][offer]["leads"],
                                                           "revenue": data[campaign][offer]["revenue"]
                                                          }

    p_offers_gpr_lookup = {}

    for offer in c_offers_for_all_campaigns.values():
        p_offer_name = offer["p_offer_name"]
        if p_offer_name in p_offers_gpr_lookup:
            p_offers_gpr_lookup[p_offer_name]["profit"] += offer["profit"]
        else:
            p_offers_gpr_lookup[p_offer_name] = {"profit": offer["profit"]}


    unordered_p_offers = []
    for p_offer in p_offers_gpr_lookup:
        unordered_p_offers.append({"p_offer_name": p_offer, "profit":
            p_offers_gpr_lookup[p_offer]["profit"]})

    df = pd.DataFrame(unordered_p_offers)
    df = df.sort_values("profit")
    ordered_p_offers = list(df["p_offer_name"])

    number_of_offers = len(ordered_p_offers)
    number_of_offers_to_keep = round(number_of_offers * 0.3)

    rank = 1
    for i in range(0, len(ordered_p_offers)):
        p_offer_name = ordered_p_offers[i]
        if i > number_of_offers - number_of_offers_to_keep:
            p_offers_gpr_lookup[p_offer_name]["rank"] = rank
            rank += 1
        else: 
            p_offers_gpr_lookup[p_offer_name]["rank"] = 0

    for p_offer in p_offers_gpr_lookup.values():
        p_offer["gpr"] = p_offer["rank"]
        p_offer["gpr_formula"] = f"gpr = rank"
        p_offer["roi_formula"] = "if roi >= 5:\n    return ceil(5 * sales/2)\nelif roi >= 4:\n    return ceil(4 * sales/2)\nelif roi >= 3:\n    return ceil(3 * sales/2)\nelif roi >= 0:\n    return ceil(2 * sales/2)\nelif roi > -1:\n    return ceil(1 * sales/2)\nelse:\n    return 0\n" 
        p_offer["cvr_formula"] = "if cvr >= .02:\n    return 8\nelif cvr >= .015:\n    return 7\nelif cvr >= .0125:\n    return 6\nelif cvr >= .010:\n    return 5\nelif cvr >= .006:\n    return 4\nelif cvr >= .005:\n    return 3\nelif cvr >= .003:\n    return 2\nelif cvr >= .002:\n    return 1\nelif cvr >= .001:\n    return 1\nelse:\n    return 0" 

    # At this point, offers_for_each_flow_rule exists and you have a
    # p_offers_gpr_lookup dictionary which tells you the gpr of each parent
    # offer

    ##################################

    # 3. Add roi cvr and gpr to offers_for_each_flow_rule

    for flow_rule in offers_for_each_flow_rule["data"]:
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            profit = offers_for_each_flow_rule["data"][flow_rule][offer]["profit"]
            cost = offers_for_each_flow_rule["data"][flow_rule][offer]["cost"]
            if cost == 0:
                offers_for_each_flow_rule["data"][flow_rule][offer]["roi"] = 0
            else:
                offers_for_each_flow_rule["data"][flow_rule][offer]["roi"] = profit/cost

            conversions = offers_for_each_flow_rule["data"][flow_rule][offer]["conversions"]
            clicks = offers_for_each_flow_rule["data"][flow_rule][offer]["clicks"]
            if clicks == 0:
                offers_for_each_flow_rule["data"][flow_rule][offer]["cvr"] = 0
            else:
                offers_for_each_flow_rule["data"][flow_rule][offer]["cvr"] = conversions/clicks

            p_offer_name = offers_for_each_flow_rule["data"][flow_rule][offer]["p_offer_name"]
            gpr = p_offers_gpr_lookup[p_offer_name]["gpr"]
            p_offer_profit = p_offers_gpr_lookup[p_offer_name]["profit"]
            p_offer_profit_rank = p_offers_gpr_lookup[p_offer_name]["rank"]
            gpr_formula = p_offers_gpr_lookup[p_offer_name]["gpr_formula"]
            roi_formula = p_offers_gpr_lookup[p_offer_name]["roi_formula"]
            cvr_formula = p_offers_gpr_lookup[p_offer_name]["cvr_formula"]
            offers_for_each_flow_rule["data"][flow_rule][offer]["gpr"] = gpr
            offers_for_each_flow_rule["data"][flow_rule][offer]["p_offer_profit"] = p_offer_profit
            offers_for_each_flow_rule["data"][flow_rule][offer]["p_offer_profit_rank"] = p_offer_profit_rank
            offers_for_each_flow_rule["data"][flow_rule][offer]["gpr_formula"] = gpr_formula
            offers_for_each_flow_rule["data"][flow_rule][offer]["roi_formula"] = roi_formula
            offers_for_each_flow_rule["data"][flow_rule][offer]["cvr_formula"] = cvr_formula

    ###############################
    # 4. Calculate the total score of each offer (uses helper functions at the
    # bottom of this file)
    # total_score = roi_score + cvr_score + gpr

    for flow_rule in offers_for_each_flow_rule["data"]:
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            roi = offers_for_each_flow_rule["data"][flow_rule][offer]["roi"]
            sales = offers_for_each_flow_rule["data"][flow_rule][offer]["sales"]
            cvr = offers_for_each_flow_rule["data"][flow_rule][offer]["cvr"]
            gpr = offers_for_each_flow_rule["data"][flow_rule][offer]["gpr"]

            roi_score = get_roi_score(roi, sales)

            cvr_score = get_cvr_score(cvr)
            total_score = roi_score + cvr_score + gpr

            offers_for_each_flow_rule["data"][flow_rule][offer]["roi_score"] = roi_score
            offers_for_each_flow_rule["data"][flow_rule][offer]["cvr_score"] = cvr_score
            offers_for_each_flow_rule["data"][flow_rule][offer]["total_score"] = total_score
        ###############
        # this part ranks the offers by total_score
        # the rank is used later when assigning a weight
        offers_in_one_flow_rule = []
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            offers_in_one_flow_rule.append(offers_for_each_flow_rule["data"][flow_rule][offer])
        df = pd.DataFrame(offers_in_one_flow_rule)
        df = df.sort_values("total_score", ascending=False)
        ordered_offers_in_one_flow_rule = df[["offer_id", "total_score"]].to_dict("records")
        count = 1
        for offer in ordered_offers_in_one_flow_rule:
            offers_for_each_flow_rule["data"][flow_rule][offer["offer_id"]]["total_score_rank"] = count
            count += 1
            
    ####################################

    # 5. Calculate the weight of each offer
    
    for flow_rule in offers_for_each_flow_rule["data"]:
        number_of_offers_in_flow_rule = 0
        total_flow_rule_score = 0
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            number_of_offers_in_flow_rule += 1
            total_flow_rule_score += offers_for_each_flow_rule["data"][flow_rule][offer]["total_score"]
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            total_score = offers_for_each_flow_rule["data"][flow_rule][offer]["total_score"] 
            if total_flow_rule_score == 0:
                offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] = round(100 / number_of_offers_in_flow_rule, 0)
            else:
                offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] = round(total_score / total_flow_rule_score * 100, 0)

        # The lines below handles the sitation where one offer is 100 and others are 0
        # it should reduce the top offer to 90 and give 10 to the second best
        # offer
        # Every offer was given a total_score_rank so if one offer is 100 and
        # the others are 0, the 100 should be reduced to 90 and the offer with
        # total_score_rank of 2 should be increased to 10. 
        best_offer_weight = 0
        best_offer_id = "" 
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            if offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] > best_offer_weight:
                best_offer_weight = offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"]
                best_offer_id = offers_for_each_flow_rule["data"][flow_rule][offer]["offer_id"]
        if (number_of_offers_in_flow_rule > 1) & (best_offer_weight == 100):
            for offer in offers_for_each_flow_rule["data"][flow_rule]:
                if offers_for_each_flow_rule["data"][flow_rule][offer]["offer_id"] == best_offer_id:
                    offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] = 90
            for offer in offers_for_each_flow_rule["data"][flow_rule]:
                if offers_for_each_flow_rule["data"][flow_rule][offer]["total_score_rank"] == 2: 
                    offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] = 10
                    break
        # 5/15/19 
        # if (offerCost < $10) OR (offerClicks < 1000) than recommended weight = existing voluum weight.
        for offer in offers_for_each_flow_rule["data"][flow_rule]:
            cost = offers_for_each_flow_rule["data"][flow_rule][offer]["cost"]
            clicks = offers_for_each_flow_rule["data"][flow_rule][offer]["clicks"]
            vol_weight = offers_for_each_flow_rule["data"][flow_rule][offer]["vol_weight"]
            if cost < 10 or clicks < 1000:
                offers_for_each_flow_rule["data"][flow_rule][offer]["rec_weight"] = vol_weight


    # At this point, offers_for_each_flow_rule is a lookup dictionary to find
    # the weight of each offer. In the next step you will add that weight to
    # the offers_for_all_campaigns dataset

    ########################################

    # 6. Save file and return

    with open(f"../../data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json", "w") as file:
        json.dump(offers_for_each_flow_rule, file)



#################################
# helper functions
import math

def get_roi_score(roi, sales):
    # if roi >= 10:
        # return 10 * sales/2
    # elif roi >= 9:
        # return 9 * sales/2
    # elif roi >= 8:
        # return 8 * sales/2
    # elif roi >= 7:
        # return 7 * sales/2
    # elif roi >= 6:
        # return 6 * sales/2
    if roi >= 5:
        return math.ceil(5 * sales/2)
    elif roi >= 4:
        return math.ceil(4 * sales/2)
    elif roi >= 3:
        return math.ceil(3 * sales/2)
    elif roi >= 0:
        return math.ceil(2 * sales/2)
    elif roi > -1:
        return math.ceil(1 * sales/2)
    else:
        return 0 

def get_cvr_score(cvr):
    if cvr >= .02:
        return 8
    elif cvr >= .015:
        return 7 
    elif cvr >= .0125:
        return 6 
    elif cvr >= .010:
        return 5 
    elif cvr >= .006:
        return 4 
    elif cvr >= .005:
        return 3 
    elif cvr >= .003:
        return 2 
    elif cvr >= .002:
        return 1 
    elif cvr >= .001:
        return 1 
    else:
        return 0 

