from functions.misc.send_email import send_email
from datetime import datetime
import sys
import requests
import json
import os

def update_good_widgets_file():
    try:
        res = requests.get("http://ulanmedia.com/mgid/goodpwidgets.txt")
        res.raise_for_status()
        widgets = res.text.split("\n")
        good_widgets = []
        for widget in widgets:
            if widget != "":
                good_widgets.append(widget.replace("\r", ""))

        with open(f"{os.environ.get('ULANMEDIAAPP')}/curated_lists/good_widgets/good_widgets.json", "w") as file:
           json.dump(good_widgets, file)
    except requests.exceptions.RequestException as e:
            print("Failed to update good widgets file")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_good widgets_file() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

