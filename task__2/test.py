import mysql.connector
from datetime import datetime, timedelta



mydb = mysql.connector.connect(
                 host="localhost", 
                 user="root",  
                 passwd="1234", 
                 database="rasa_db") 
mycursor = mydb.cursor() 
sql='SELECT count(*) FROM table3 WHERE entry_date IN (DATE_SUB(CURDATE(), INTERVAL 1 WEEK)) ;'
mycursor.execute(sql) 
table = mycursor.fetchall()
print(type(table[0][0]))


# Import date class from datetime module
  
  
# Returns the current local date

# start = datetime.strptime("20-06-202022", "%d-%m-%Y")
# if d <= start <= today:
#     print ("PASS!")
# print("Today date is: ", today)
# print(d)
