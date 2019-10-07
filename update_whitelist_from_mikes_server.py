from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys
import mysql.connector
from ulanmedia2_config.config import *

def update_whitelist_from_mikes_server():
    try:
        res = requests.get("https://ulanmedia.brianhaller.net/api/readwhitelist")
        res.raise_for_status()
        widgets = res.json()

        mydb = mysql.connector.connect(
        host="localhost",
        user= mysql_user,
        passwd= mysql_password,
        database="ulanmedia"
        )

        mycursor = mydb.cursor()

        for widget in widgets:
            sql = f"INSERT INTO colorlist(widget_id, color) values('{widget}', 'white');"
            mycursor.execute(sql)
            mydb.commit()

    except requests.exceptions.RequestException as e:
            print("Failed to update_whitelist_from_mikes_server")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_whitelist_from_mikes_server() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

update_whitelist_from_mikes_server()
