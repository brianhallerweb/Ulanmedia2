import sys
import os
import json
import pandas as pd
import numpy as np

def create_days_for_one_campaign_report(campaign_id):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/days_for_one_campaign/days_for_one_campaign_dataset.json', 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data[campaign_id])
    
    df["cost"] = round(df["cost"], 2)
    df["profit"] = round((df["revenue"] - df["cost"]), 2)
    df["cpc"] = round(df["cost"]/df["clicks"], 3)
    df["epc"] = round(df["revenue"]/df["clicks"], 3)
    df["cpa"] = round(df["cost"]/df["conversions"], 2)
    df["epa"] = round(df["revenue"]/df["conversions"], 2)
    df["cvr"] = round(df["conversions"]/df["clicks"], 3)
    
    df = df.replace([np.inf, -np.inf], "NaN")
    df = df.replace(np.nan, "NaN")
    df = df.sort_values("day", ascending=False)
    
    json_final_result = json.dumps(df[["vol_id", "name", "day", "clicks", "cost",
        "cpc", "revenue", "conversions", "cpa", "profit", "epc", "epa", "cvr"]].to_dict("records"))
    
    return json_final_result

