import sys
import os
import json
import pandas as pd
import numpy as np
import math

def create_c_widgets_for_all_campaigns_report(date_range, c1_input, c2_input,
        c3_input, c4_input, c5_input, c6_input, c7_input, c8_input,
        c1Value_input, c2Value_input, c3Value_input, c4Value_input,
        c5Value_input, c6Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/c_widgets_for_all_campaigns/{date_range}_c_widgets_for_all_campaigns_dataset.json', 'r') as file:
         json_file = json.load(file)
    data = json_file["data"]     
    
    # The json data is a dictionary with each widget id as a key and each widget
    # (summary of all campaigns) as 
    # a value. The loop below simple takes the values and puts them into a list. 
    widgets = []
    for widget in data.values():
        widgets.append(widget)
    
    df = pd.DataFrame(widgets)
    
    df["cost"] = round(df["cost"], 2)
    df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epc"] = round(df["revenue"] / df["clicks"], 2)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["global_status"] == c2Value_input
    result2 = df[c2]
    
    c3 = df["cost"] >= float(c3Value_input)
    result3 = df[c3]
    
    c4 = df["profit"] <= -1 * float(c4Value_input)
    result4 = df[c4]
    
    c5 = df["leads"] >= float(c5Value_input)
    result5 = df[c5]
    
    c6 = df["sales"] >= float(c6Value_input)
    result6 = df[c6]
    
    c7 = df["has_bad_and_included_campaigns"] == True 
    result7 = df[c7]
    
    c8 = df["has_mismatch_classification_and_global_status"] == True
    result8 = df[c8]
    
    conditions_args = [c1_input, c2_input, c3_input, c4_input, c5_input, c6_input, c7_input, c8_input]
    conditions_dfs = [result1, result2, result3, result4, result5, result6,
            result7, result8]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id", "lead_cvr", "profit",
                "global_status", "classification", "has_mismatch_classification_and_global_status", "has_bad_and_included_campaigns",
                "good_campaigns_count", "bad_campaigns_count",
                "wait_campaigns_count", "cpc", "epc", "cpl", "epl", "cps", "eps",
                "domain"]
                )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result = final_result.sort_values(["profit", "classification"],
            ascending=[True, True])
    
    json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id", "lead_cvr", "profit",
                "global_status", "classification", "has_mismatch_classification_and_global_status", "has_bad_and_included_campaigns",
                "good_campaigns_count", "bad_campaigns_count",
                "wait_campaigns_count", "cpc", "epc", "cpl", "epl", "cps", "eps",
                "domain"]].to_dict("records"))
    
    return json_final_result
