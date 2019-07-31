import requests
from datetime import datetime, timedelta

# this is an example of a function that will break up a long date range
# into 30 day chunks, do separate requests for each chunk, and then 
# aggregate everything back into one dictionary
def example(token, campaign_id, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    agreggated_data = {} 
    while (end - start).days >= 30:
        temp_start = (end - timedelta(30)).strftime("%Y-%m-%d")
        temp_end = end.strftime("%Y-%m-%d")
        print(f"request from {temp_start} to {temp_end}")
        url = "url"
        response = requests.get(url).json()
        for data in response:
            if data in widget_data:
                # update aggregated_data
            else: 
                # write to aggregated_data
        end = datetime.strptime(temp_start, "%Y-%m-%d").date()
    if (end - start).days > 0:
        print(f"request from {start} to {end}")
        url = "url"
        response = requests.get(url).json()
        for data in response:
            if data in widget_data:
                # update aggregated_data
            else: 
                # write to aggregated_data
    return widget_data 

