import sys
import os
import json
import pandas as pd
import numpy as np

def create_languages_for_one_campaign_report(campaign_id, date_range, c1_input, c2_input,
        c3_input, c1Value_input, c2Value_input, c3Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/languages_for_one_campaign/{date_range}_{campaign_id}_languages_for_one_campaign_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    data = json_file["data"]
    
    df = pd.DataFrame(data)
    df["cost"] = round(df["cost"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
            2)
    df["epc"] = (df["revenue"] / df["clicks"]).round(3)
    df["cpa"] = round(df["cost"] / df["conversions"], 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epa"] = round(df["revenue"] / df["conversions"], 2)
    df["roi"] = round((df["profit"] / df["cost"])*100, 2)
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["cost"] >= float(c2Value_input)
    result2 = df[c2]
    
    c3 = df["profit"] <= -1 * float(c3Value_input)
    result3 = df[c3]
    
    conditions_args = [c1_input, c2_input, c3_input]
    conditions_dfs = [result1, result2, result3]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["language_name", "classification", "clicks", "cost", "conversions", "profit","revenue", "cvr", "epc", "cpa", "cpc", "epa", "roi"] )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result["sort"] = final_result["cost"]
    final_result = final_result.sort_values("sort", ascending=False)
    
    # add a summary row at the top
    if len(final_result.index) > 0:
        summary = final_result.sum(numeric_only=True)
        summary = summary.round(2)
        summary["language_name"] = "summary"
        summary["roi"] = round(summary["cost"] / summary["profit"], 2)
        if summary["clicks"] == 0:
            summary["cvr"] = 0
            summary["epc"] = 0
        else:
            summary["cvr"] = round((summary["conversions"] / summary["clicks"]) * 100,
            2)
            summary["epc"] = round((summary["revenue"] / summary["clicks"]),
            2)
        if summary["conversions"] == 0:
            summary["cpa"] = 0
            summary["epa"] = 0
        else:
            summary["cpa"] = round((summary["cost"] / summary["conversions"]),
            2)
            summary["epa"] = round(summary["revenue"] / summary["conversions"], 2)
        final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
        final_result = final_result.replace(np.nan, "")
    
    json_final_result = json.dumps(final_result[["language_name", "classification", "clicks", "cost", "conversions", "profit","revenue", "cvr", "epc", "cpa", "cpc", "epa", "roi"]].to_dict("records"))
    
    return json_final_result
