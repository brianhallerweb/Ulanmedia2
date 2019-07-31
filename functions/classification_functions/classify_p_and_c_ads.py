def classify_p_and_c_ads(ad):
    cvr = ad["cvr"]
    roi = ad["roi"]
    cost = ad["cost"]

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



