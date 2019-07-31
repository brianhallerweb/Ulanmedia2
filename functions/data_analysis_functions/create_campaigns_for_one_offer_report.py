import sys
import os
import json
import pandas as pd
import numpy as np

def create_campaigns_for_one_offer_report(offer_id, date_range, c1_input,
        c2_input, c3_input, c1Value_input, c2Value_input,
        c3Value_input): 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_one_offer/{offer_id}_{date_range}_campaigns_for_one_offer_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    data = json_file["data"]
    
    df = pd.DataFrame(data)
    df["cost"] = round(df["cost"], 2)
    df["revenue"] = round(df["revenue"], 2)
    df["profit"] = round(df["profit"], 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epc"] = (df["revenue"] / df["clicks"]).round(3)
    df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
            2)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    df["roi"] = round(df["roi"] * 100, 2)
    
    c1 = df["cost"] >= float(c1Value_input)
    result1 = df[c1]
    
    c2 = df["profit"] <= -1 * float(c2Value_input)
    result2 = df[c2]
    
    c3 = df["lead_cvr"] <= float(c3Value_input)
    result3 = df[c3]
    
    conditions_args = [c1_input, c2_input, c3_input]
    conditions_dfs = [result1, result2, result3]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["campaign_name", "offer_id","offer_name", "flow_rule", "campaign_id", "clicks",
        "cost", "revenue", "profit","conversions", "lead_cvr",
        "epc", "cpl", "epl", "cpc", "cps", "eps", "leads", "sales", "roi"])
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result = final_result.sort_values(["flow_rule", "clicks"],
            ascending=[True, False])
    
    # Add a summary row at the top
    if len(final_result.index) > 0:
        summary = final_result.sum(numeric_only=True)
        summary = summary.round(2)
        summary["campaign_name"] = "summary"
        summary["roi"] = round(summary["profit"] / summary["cost"] * 100, 2)
        if summary["clicks"] == 0:
            summary["lead_cvr"] = "NaN" 
            summary["epc"] = "NaN" 
        else:
            summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
            2)
            summary["epc"] = round(summary["revenue"] / summary["clicks"], 3)
        if summary["leads"] == 0:
            summary["cpl"] = "NaN" 
            summary["epl"] = "NaN"
        else:
            summary["cpl"] = round(summary["cost"] / summary["leads"], 2)
            summary["epl"] = round(summary["revenue"] / summary["leads"], 2)
        if summary["sales"] == 0:
            summary["cps"] = "NaN"
            summary["eps"] = "NaN"
        else:
            summary["cps"] = round(summary["cost"] / summary["sales"], 2)
            summary["eps"] = round(summary["revenue"] / summary["sales"], 2)
        final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
        final_result = final_result.replace(np.nan, "")
    
    json_final_result = json.dumps(final_result[["campaign_name", "offer_id","offer_name", "flow_rule", "campaign_id", "clicks",
        "cost", "revenue", "profit","conversions", "lead_cvr",
        "epc", "cpl", "epl", "cpc", "cps", "eps", "leads", "sales", "roi"]].to_dict("records"))
    
    return json_final_result
    
