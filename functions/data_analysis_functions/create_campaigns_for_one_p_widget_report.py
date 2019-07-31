import sys
import os
import json
import pandas as pd
import numpy as np

def create_campaigns_for_one_p_widget_report(date_range, widget_id, c1_input, c2_input,
        c3_input, c4_input, c5_input, c6_input, c1Value_input, c2Value_input, c3Value_input, c4Value_input,
        c5Value_input, c6Value_input):


    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_one_p_widget/{widget_id}_{date_range}_campaigns_for_one_p_widget_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    campaigns = json_file["data"]
    
    df = pd.DataFrame(campaigns)
    
    # this condition handles the case where the parent widget dataset is empty.
    # The first time I noticed this possibility was when mike excluded a widget
    # from all campaigns. The next day, when the app created a dataset for
    # campaigns_for_one_parent/child_widget, that dataset was empty. 
    if len(df.index) == 0:
        print(json.dumps(campaigns))
        sys.exit()
    
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
    domain = df["domain"][0] 
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["status"] == c2Value_input
    result2 = df[c2]
    
    c3 = df["cost"] >= c3Value_input
    result3 = df[c3]
    
    c4 = df["profit"] <= -1 * float(c4Value_input)
    result4 = df[c4]
    
    c5 = df["cpl"] <= (df["mpl"] - (df["mpl"] * float(c5Value_input)/100))
    result5 = df[c5]
    
    c6 = df["cps"] <= (df["mps"] - (df["mps"] * float(c6Value_input)/100))
    result6 = df[c6]
    
    
    conditions_args = [c1_input, c2_input, c3_input, c4_input, c5_input,
            c6_input]
    conditions_dfs = [result1, result2, result3, result4, result5, result6]
    
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
                "classification", "is_bad_and_included", "w_bid", "coeff", "rec_w_bid",
                "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
                "mismatch_coeff_and_rec_coeff", "domain"]
                )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result = final_result.sort_values("name", ascending=True)
    
    # add a summary row at the top
    if len(final_result.index) > 0:
        summary = final_result.sum(numeric_only=True)
        summary = summary.round(2)
        summary["name"] = "summary"
        summary["cpc"] = round(summary["cost"] / summary["clicks"], 2)
        summary["epc"] = round(summary["revenue"] / summary["clicks"], 2)
        summary["w_bid"] = "NA" 
        summary["coeff"] = "NA" 
        summary["rec_w_bid"] = "NA" 
        summary["rec_coeff"] = "NA" 
        summary["mpl"] = "NA"
        summary["mps"] = "NA" 
        summary["classification"] = "NA"  
        summary["status"] = "NA"  
        summary["domain"] = domain 
        summary["is_bad_and_included"] = False  
        if summary["clicks"] == 0:
            summary["lead_cvr"] = 0
        else:
            summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
            2)
        rows_with_leads = final_result[final_result["leads"] >= 1]
        number_of_rows_with_leads = len(rows_with_leads.index)
        if number_of_rows_with_leads > 0:
            summary["cpl"] = round(summary["cost"] / summary["leads"], 2)
            summary["epl"] = round(summary["revenue"] / summary["leads"], 2)
        else:
            summary["cpl"] = 0 
            summary["epl"] = 0 
        rows_with_sales = final_result[final_result["sales"] >= 1]
        number_of_rows_with_sales = len(rows_with_sales.index)
        if number_of_rows_with_sales > 0:
            summary["cps"] = round(summary["cost"] / summary["sales"], 2)
            summary["eps"] = round(summary["revenue"] / summary["sales"], 2)
        else:
            summary["cps"] = 0
            summary["eps"] = 0
        # Append summary onto the top
        final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result], sort=True)
        final_result = final_result.replace(np.nan, "")
    
    json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
                "cpc", "epc", "cpl", "epl", "mpl", "lead_cvr",
                "cps", "eps", "mps", "profit", "status",
                "classification", "is_bad_and_included", "w_bid", "coeff", "rec_w_bid",
                "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
                "mismatch_coeff_and_rec_coeff", "domain"]].to_dict("records"))
    
    return json_final_result
