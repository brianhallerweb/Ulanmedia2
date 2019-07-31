import sys
import os
import json
import pandas as pd
import numpy as np

def create_campaigns_for_all_campaigns_report(date_range, c1_input,
        c1Value_input ,c2_input,
        c2Value_input, c3_input, c3Value_input, c4_input, c5_input, c6_input, c6Value_input, c7_input, c7Value_input, c8_input, c8Value_input,
        c9_input, c9Value_input, c10_input, c10Value_input, c11_input, c11Value_input, c12_input, c12Value_input, c13_input,
        c13Value_input, c14_input, c14Value_input, c15_input, c15Value_input, c16_input, c16Value_input, c17_input, c17Value_input,
        c18_input, c18Value_input, c19_input, c19Value_input, c20_input, c20Value_input, c21_input, c21Value_input, c22_input, c22Value_input, c23_input, c23Value_input, c24_input, c24Value_input, c25_input, c25Value_input, c26_input, c26Value_input, c27_input, c27Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_all_campaigns/{date_range}_campaigns_for_all_campaigns_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    metadata = json_file["metadata"]
    data = json_file["data"]
    
    df = pd.DataFrame(data)
    df["vol_start_date"] = metadata["vol_start_date"]
    df["vol_end_date"] = metadata["vol_end_date"]
    df["mgid_start_date"] = metadata["mgid_start_date"]
    df["mgid_end_date"] = metadata["mgid_end_date"]
    df["mpl"] = df["max_lead_cpa"].astype("float64")
    df["mps"] = df["max_sale_cpa"].astype("float64")
    df["mpc"] = df["max_cpc"].astype("float64")
    df["cpc"] = round(df["cost"] / df["clicks"], 3)
    df["epc"] = round(df["revenue"] / df["clicks"], 3)
    df["cpl"] = round(df["cost"] / df["leads"], 3)
    df["epl"] = round(df["revenue"] / df["leads"], 3)
    df["eps"] = round(df["revenue"] / df["sales"], 3)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["cost"] >= float(c2Value_input)
    result2 = df[c2]
    
    c3 = df["profit"] <= -1 * float(c3Value_input)
    result3 = df[c3]
    
    c4 = df["sales"] > 0
    result4 = df[c4]
    
    c5 = df["sales"] == 0
    result5 = df[c5]
    
    ####################
    #need to lower cost or tighten targeting
    
    c6 = df["bid"] >= (df["epc"] + (df["epc"]*float(c6Value_input)/100))
    result6 = df[c6]
    
    c7 = df["cpc"] >= (df["epc"] + (df["epc"]*float(c7Value_input)/100))
    result7 = df[c7]
    
    c8 = df["cpl"] >= (df["epl"] + (df["epl"]*float(c8Value_input)/100))
    result8 = df[c8]
    
    c9 = df["cps"] >= (df["eps"] + (df["eps"]*float(c9Value_input)/100))
    result9 = df[c9]
    
    
    ########################
    # can raise cost or loosen targeting
    
    c10 = df["bid"] <= (df["epc"] - (df["epc"]*float(c10Value_input)/100))
    result10 = df[c10]
    
    c11 = df["cpc"] <= (df["epc"] - (df["epc"]*float(c11Value_input)/100))
    result11 = df[c11]
    
    c12 = df["cpl"] <= (df["epl"] - (df["epl"]*float(c12Value_input)/100))
    result12 = df[c12]
    
    c13 = df["cps"] <= (df["eps"] - (df["eps"]*float(c13Value_input)/100))
    result13 = df[c13]
    
    
    ####################
    # need to lower cost or tighten targeting or raise max per click/lead/sale:
    
    c14 = df["bid"] >= (df["mpc"] + (df["mpc"]*float(c14Value_input)/100))
    result14 = df[c14]
    
    c15 = df["cpc"] >= (df["mpc"] + (df["mpc"]*float(c15Value_input)/100))
    result15 = df[c15]
    
    c16 = ((df["cpl"] != np.inf) & (df["cpl"] >= (df["mpl"] +
        (df["mpl"]*float(c16Value_input)/100)))) | ((df["cost"] >= (df["mpl"] +
            (df["mpl"]*float(c16Value_input)/100))) & (df["leads"] == 0))
    result16 = df[c16]
    
    c17 = ((df["cps"] != np.inf) & (df["cps"] >= (df["mps"] +
        (df["mps"]*float(c17Value_input)/100)))) | ((df["cost"] >= (df["mps"] +
            (df["mps"]*float(c17Value_input)/100))) & (df["sales"] == 0))
    result17 = df[c17]
    
    ####################
    # can raise cost or loosen targeting or lower max per click/lead/sale
    
    c18 = df["bid"] <= (df["mpc"] - (df["mpc"]*float(c17Value_input)/100))
    result18 = df[c18]
    
    c19 = df["cpc"] <= (df["mpc"] - (df["mpc"]*float(c18Value_input)/100))
    result19 = df[c19]
    
    c20 = df["cpl"] <= (df["mpl"] - (df["mpl"]*float(c19Value_input)/100))
    result20 = df[c20]
    
    c21 = df["cps"] <= (df["mps"] - (df["mps"]*float(c20Value_input)/100))
    result21 = df[c21]
    
    ###################
    # need to lower max per click/lead/sale:
    
    c22 = df["mpc"] >= (df["epc"] + (df["epc"]*float(c21Value_input)/100))
    result22 = df[c22]
    
    c23 = df["mpl"] >= (df["epl"] + (df["epl"]*float(c22Value_input)/100))
    result23 = df[c23]
    
    c24 = df["mps"] >= (df["eps"] + (df["eps"]*float(c23Value_input)/100))
    result24 = df[c24]
    
    #################
    # can raise max per click/lead/sale:
    
    c25 = df["mpc"] <= (df["epc"] - (df["epc"]*float(c24Value_input)/100))
    result25 = df[c25]
    
    c26 = df["mpl"] <= (df["epl"] - (df["epl"]*float(c25Value_input)/100))
    result26 = df[c26]
    
    c27 = df["mps"] <= (df["eps"] - (df["eps"]*float(c26Value_input)/100))
    result27 = df[c27]
    
    
    conditions_args = [c1_input, c2_input, c3_input, c4_input, c5_input,
            c6_input, c7_input, c8_input, c9_input, c10_input, c11_input,
            c12_input, c13_input, c14_input, c15_input, c16_input, c17_input,
            c18_input, c19_input, c20_input, c21_input, c22_input, c23_input,
            c24_input, c25_input, c26_input, c27_input]
    
    conditions_dfs = [result1, result2, result3, result4, result5, result6,
            result7, result8, result9, result10, result11, result12, result13,
            result14, result15, result16, result17, result18, result19, result20,
            result21, result22, result23, result24, result25, result26, result27]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["mgid_start_date", "mgid_end_date","vol_start_date", "vol_end_date","mgid_id", "vol_id", "name", "clicks",
                "cost", "imps", "leads", "mpl", "mps", "cpc",
                "epc", "epl",
                "mgid_id", "revenue", "sales","vol_id", "cpl", "eps", "cps", "mpc",
                "profit", "classification"] )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result["sort"] = final_result["name"].str[4:]
    final_result = final_result.sort_values("sort")
    json_final_result = json.dumps(final_result[["mgid_start_date",
        "mgid_end_date","vol_start_date", "vol_end_date", "mgid_id", "vol_id", "name",
        "clicks", "cost", "revenue", "profit", "leads","mpc",
        "mpl","cpl", "epl", "sales", "cps","mps","cpc","eps", "epc", "classification"]].to_dict("records"))
    
    return json_final_result

