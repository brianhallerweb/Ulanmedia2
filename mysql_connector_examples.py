import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="bsh",
  passwd="kensington",
  database="ulanmedia"
)

#############
# show databases
# mycursor = mydb.cursor()
# sql = 'show databases'
# mycursor.execute(sql)
# for db in mycursor:
    # print(db)
# mydb.commit()

########
# insert into table
# mycursor = mydb.cursor()
# sql = "INSERT INTO test(name) VALUES('obie3')"
# mycursor.execute(sql)
# mydb.commit()

############
# query all from table
# mycursor = mydb.cursor()
# sql = "select * from test"
# mycursor.execute(sql)
# result = mycursor.fetchall()
# for db in result:
    # print(db)

############
# query one from table
# mycursor = mydb.cursor()
# sql = "select * from test"
# mycursor.execute(sql)
# result = mycursor.fetchone()
# print(result)

