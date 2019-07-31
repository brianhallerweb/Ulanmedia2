import sys
import os
import json
import pandas as pd
import numpy as np

def create_ads_for_all_campaigns_report(date_range, c1_input, c2_input,
        c3_input, c4_input, c5_input, c1Value_input, c2Value_input, c3Value_input, c4Value_input,
        c5Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    data = json_file["data"]
    
    ads = []
    for ad in data.values():
        ads.append(ad)
    
    df = pd.DataFrame(ads)
    df["cost"] = round(df["cost"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epc"] = (df["revenue"] / df["clicks"]).round(3)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
            2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    df["roi"] = round(df["roi"] * 100, 2)
    df["ctr"] = round(df["ctr"] * 100, 2) 
    df["ppi"] = round(df["profit"] / df["imps"], 6) 
    df["global_rank"] = round(df["global_rank"], 0)
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["cost"] >= float(c2Value_input)
    result2 = df[c2]
    
    c3 = df["profit"] <= -1 * float(c3Value_input)
    result3 = df[c3]
    
    c4 = df["ctr"] <= float(c4Value_input)
    result4 = df[c4]
    
    c5 = np.isfinite(df["lead_cvr"]) & (df["lead_cvr"] <= float(c5Value_input))
    result5 = df[c5]
    
    conditions_args = [c1_input, c2_input, c3_input, c4_input, c5_input]
    conditions_dfs = [result1, result2, result3, result4, result5]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["image", "name", "clicks",
        "cost", "revenue", "profit","conversions", "cpc", "epc", "cpl", "epl", "lead_cvr", "cps",
    "eps", "mgid_id", "vol_id", "roi", "global_rank", "global_rank_order",
    "classification", "imps", "ctr", "ppi", "leads", "sales"] )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result["sort"] = final_result["global_rank"]
    final_result = final_result.sort_values("sort", ascending=False)
    json_final_result = json.dumps(final_result[["image", "name", "clicks",
        "cost", "revenue", "profit","conversions", "cpc", "epc", "cpl", "epl", "lead_cvr", "cps",
    "eps", "mgid_id", "vol_id", "roi", "global_rank", "global_rank_order",
    "classification", "imps", "ctr", "ppi", "leads", "sales"]].to_dict("records"))
    
    return json_final_result
    
