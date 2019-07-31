import sys
import os
import json
import pandas as pd
import numpy as np

def create_campaigns_for_good_p_widgets_report(date_range, c3_input, c3Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json', 'r') as file:
         campaigns = json.load(file)
    
    df = pd.DataFrame(campaigns)
    
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["cost"] = round(df["cost"], 2)
    df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epc"] = round(df["revenue"] / df["clicks"], 2)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    df["w_bid"] = round(df["w_bid"], 2)
    df["rec_w_bid"] = round(df["rec_w_bid"], 2)
    df["rec_coeff"] = round(df["rec_coeff"], 1)
    
    c1 = df["cost"] >= float(c3Value_input)
    result1 = df[c1]
    
    conditions_args = [c3_input]
    conditions_dfs = [result1]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
                "cpc", "epc", "cpl", "epl", "mpl", "lead_cvr",
                "cps", "eps", "mps", "profit", "status",
                "widget_id", "global_status", "c_bid",
                "w_bid", "coeff", "rec_w_bid",
                "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
                "mismatch_coeff_and_rec_coeff", "domain"]
                )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result = final_result.sort_values("name", ascending=True)
    
    json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
                "cpc", "epc", "cpl", "epl", "mpl", "lead_cvr",
                "cps", "eps", "mps", "profit", "status",
                "widget_id", "global_status", "c_bid",
                "w_bid", "coeff", "rec_w_bid",
                "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
                "mismatch_coeff_and_rec_coeff", "domain"]].to_dict("records"))
    
    return json_final_result
