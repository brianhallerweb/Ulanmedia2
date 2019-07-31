# this function is used for languages for all campaigns and languages for
# one campaign

def classify_language(language):
    clicks = language["clicks"] 
    cost = language["cost"]
    revenue = language["revenue"]
    conversions = language["conversions"]
    profit = language["profit"] 
    if cost == 0:
        roi = 0
    else:
        roi = profit / cost
    if clicks == 0:
        cvr = 0
    else:
        cvr = conversions / clicks 

    ########################
    
    if roi > 0:
        return "good"
    elif cost > 600:
        if cvr > .005:
            return "bad"
        elif cvr > .002:
            return "bad"
        else:
            return "bad"
    elif cost > 300:
        if cvr > .005:
            return "wait"
        elif cvr > .002:
            return "bad"
        else:
            return "bad"
    elif cost > 100:
        if cvr > .005:
            return "wait"
        elif cvr > .002:
            return "wait"
        else:
            return "bad"
    elif cost > 50:
        if cvr > .005:
            return "wait"
        elif cvr > .002:
            return "wait"
        else:
            return "wait"
    else:
        return "wait"
