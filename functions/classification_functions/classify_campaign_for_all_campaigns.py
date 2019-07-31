def classify_campaign_for_all_campaigns(campaign):
    cost = campaign["cost"]
    revenue = campaign["revenue"]
    profit = revenue - cost
    sales = campaign["sales"]
    leads = campaign["leads"]
    mps = campaign["max_sale_cpa"]
    mpl = campaign["max_lead_cpa"]
    if sales > 0:
        cps = cost / sales
        eps = profit / sales
    else:
        cps = None 
        eps = 0
    if leads > 0:
        cpl = cost / leads
        epl = profit / leads
    else:
        cpl = None 
        epl = 0
    if profit > 0:
        return "good"
    elif sales > 0:
        if cost > (2 * mps):
            if cps > (2 * eps):
                return "bad"
            elif cps > (1 * eps):
                return "wait"
            else:
                return "good"
        else:
            if cps > (1 * eps):
                return "wait"
            else:
                return "good"
    elif leads > 0:
        if cost > (2 * mps):
            return "bad"
        elif cost > (1 * mps):
            if cpl > (2 * mpl):
                return "bad"
            elif cpl > (1 * mpl):
                return "wait"
            else:
                return "good"
        elif cost > (10 * mpl):
            if cpl > (3 * mpl):
                return "bad"
            elif cpl > (1 * mpl):
                return "wait"
            else:
                return "good"
        elif cost > (3 * mpl):
            if cpl > (5 * mpl):
                return "bad"
            elif cpl > (1 * mpl):
                return "wait"
            else:
                return "good"
        else:
            return "wait"
    elif cost > (5 * mpl):
        return "bad"
    else:
        return "wait"




