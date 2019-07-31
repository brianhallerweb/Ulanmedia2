from functions.misc.send_email import send_email
from datetime import datetime
import sys
import requests
import json
import os

def update_widget_domains_file():
    try:
        res = requests.get("http://ulanmedia.com/mgid/widgetdomains.txt")
        res.raise_for_status()
        res = res.text.split("\n")
        widget_domains = []
        for widget_domain in res:
            widget_domains.append(widget_domain.replace("\r", ""))


        widget_domain_lookup = {}

        for widget_domain in widget_domains:
            if len(widget_domain) > 0:
                widget_id = widget_domain.split(",")[0]
                domain = widget_domain.split(",")[1]
                if widget_id in widget_domain_lookup:
                    widget_domain_lookup[widget_id].append(domain)
                else:
                    widget_domain_lookup[widget_id] = [domain]


        with open(f"{os.environ.get('ULANMEDIAAPP')}/curated_lists/widget_domains/widget_domains.json", "w") as file:
           json.dump(widget_domain_lookup, file)

    except requests.exceptions.RequestException as e:
            print("Failed to update widget domains file")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_widget_domains_file() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()


