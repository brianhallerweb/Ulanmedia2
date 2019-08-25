import mysql.connector

def create_complete_campaign_sets():
    mydb = mysql.connector.connect(
      host="localhost",
      user="ulan",
      passwd="missoula1",
      database="ulanmedia"
    )
    
    mycursor = mydb.cursor()
    
    sql = "select * from campaign_sets"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    campaign_sets = []
    for row in result:
        campaign_set = {}
        campaign_set['vol_campaign_id'] = row[2]
        campaign_set['mgid_campaign_id'] = row[3]
        campaign_set['campaign_name'] = row[4]
        campaign_set['max_lead_cpa'] = float(row[5])
        campaign_set['max_sale_cpa'] = float(row[6])
        campaign_set['campaign_status'] = row[7]
        campaign_sets.append(campaign_set)

    return campaign_sets



