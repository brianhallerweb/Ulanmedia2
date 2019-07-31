def classify_offer_for_all_campaigns(offer):
    profit = offer["profit"]
    conversions = offer["conversions"]
    cost = offer["cost"]
    clicks = offer["clicks"]
    if cost == 0:
        roi = 0
    else:
        roi = profit/cost
    if clicks == 0:
        cvr = 0
    else:
        cvr = conversions/clicks

    if roi > 0.00:
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



