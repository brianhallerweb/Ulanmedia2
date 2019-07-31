# this function is used for classification on campaigns for one p/c widget and
# p widgets for one campaign. 

def classify_campaign_for_one_p_or_c_widget(campaign, p_or_c_widget_total_sales):
    #################
    # define variables
    status = campaign["status"] 
    clicks = campaign["clicks"] 
    cost = campaign["cost"] 
    leads = campaign["leads"] 
    sales = campaign["sales"] 
    revenue = campaign["revenue"] 
    profit = revenue - cost 
    mpl = campaign["mpl"]
    mps = campaign["mps"]
    if clicks == 0:
        cvr = 0
    else:
        cvr = leads / clicks * 100
    if leads == 0:
        lead_cpa = 0
    else:
        lead_cpa = cost / leads
    if sales == 0:
        sale_cpa = 0
    else:
        sale_cpa = cost / sales

    #######################
    #######################
    # return classification
    if status == "inactive":
        return "wait"
    elif sales > 0:
        if (cost/sales) <= mps:
            return "good"
        elif (cost/(sales + 1)) <= mps:
            return "half good"
        elif (cost/(sales + 2)) > mps:
            return "bad"
        elif (cost/(sales + 1)) > mps:
            return "half bad"
    else:
        if leads == 0:
            if clicks < 600:
                return "wait"
            else:
                if p_or_c_widget_total_sales == 0:
                    if cost >= (4 * mpl):
                        return "bad"
                    elif cost >= (2.5 * mpl):
                        if clicks < 1000:
                            return "half bad"
                        else:
                            return "bad"
                    elif cost >= (2 * mpl):
                        return "half bad"
                    else:
                        return "wait"
                else:
                    if cost >= (4 * mpl):
                        return "bad"
                    elif cost >= (3 * mpl):
                        return "half bad"
                    else:
                        return "wait"
        else:
            if lead_cpa >= mpl:
                if clicks < 600:
                    return "wait"
                else:
                    if p_or_c_widget_total_sales == 0:
                        if cost > (4 * mpl):
                            if lead_cpa > (3 * mpl):
                                return "bad"
                            elif lead_cpa > (2 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        elif cost > (3 * mpl):
                            if lead_cpa > (3.5 * mpl):
                                return "bad"
                            elif lead_cpa > (2.5 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        elif cost > (2 * mpl):
                            if lead_cpa > (4 * mpl):
                                return "bad"
                            elif lead_cpa > (3 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        else:
                            return "wait"
                    else:
                        if cost > (5 * mpl):
                            if lead_cpa > (3 * mpl):
                                return "bad"
                            elif lead_cpa > (2 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        elif cost > (4 * mpl):
                            if lead_cpa > (3.5 * mpl):
                                return "bad"
                            elif lead_cpa > (2.5 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        elif cost > (3 * mpl):
                            if lead_cpa > (4 * mpl):
                                return "bad"
                            elif lead_cpa > (3 * mpl):
                                return "half bad"
                            else:
                                return "wait"
                        else:
                            return "wait"
            else:
                if leads >= 3:
                    return "good"
                elif leads == 2:
                    return "half good"
                else:
                    return "wait"


                


