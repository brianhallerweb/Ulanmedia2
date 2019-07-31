import sys
import os
import json
import pandas as pd
import numpy as np

def create_c_widgets_for_one_p_widget_report(date_range, p_widget_id, c1_input, c2_input,
        c3_input, c1Value_input, c2Value_input, c3Value_input):


    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/c_widgets_for_one_p_widget/{p_widget_id}_{date_range}_c_widgets_for_one_p_widget_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    data = json_file["data"]
    
    # The json data is a dictionary with each widget id as a key and each widget as
    # a value. The loop below simple takes the values and puts them into a list. 
    widgets = []
    for widget in data.values():
        widgets.append(widget)
    
    df = pd.DataFrame(widgets)
    
    if len(df.index) == 0:
        print(json.dumps({}))
        sys.exit()
    
    df["cost"] = round(df["cost"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epc"] = round(df["revenue"] / df["clicks"], 2)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    
    # widget cost is more than xxx
    c1 = df["cost"] >= float(c1Value_input)
    result1 = df[c1]
    
    # widget lost more than xxx
    c2 = df["profit"] <= -1 * float(c2Value_input)
    result2 = df[c2]
    
    # widget leadCVR is less than or equal to xxx
    c3 = np.isfinite(df["lead_cvr"]) & (df["lead_cvr"] <= float(c3Value_input))
    result3 = df[c3]
    
    conditions_args = [c1_input, c2_input, c3_input]
    conditions_dfs = [result1, result2, result3]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id", "lead_cvr",
                "profit","cpc","epc","mpc", "cpl", "epl", "mpl", "cps",
                "eps", "mps", "global_status", "domain"]
                )                                                                             
    if final_result is None:                                                                  
        final_result = df                                                                     
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result = final_result.sort_values("cost", ascending=False)
    
    # add a summary row at the top
    if len(final_result.index) > 0:
        summary = final_result.sum(numeric_only=True)
        summary = summary.round(2)
        summary["widget_id"] = "summary"
        summary["cpc"] = round(summary["cost"] / summary["clicks"], 2)
        summary["epc"] = round(summary["revenue"] / summary["clicks"], 2)
        summary["global_status"] = "NA"
        summary["domain"] = final_result["domain"][0] 
        if summary["clicks"] == 0:
            summary["lead_cvr"] = 0
        else:
            summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100, 2)
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
        final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
        final_result = final_result.replace(np.nan, "")
    
    
    json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
                "revenue", "sales", "widget_id", "lead_cvr",
                "profit","cpc","epc","mpc", "cpl", "epl", "mpl", "cps",
                "eps", "mps", "global_status", "domain"]].to_dict("records"))
    
    return json_final_result
    
