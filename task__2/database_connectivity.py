import mysql.connector
def DataUpdate(Name,Email,Date): 
              mydb = mysql.connector.connect(
                 host="localhost", 
                 user="root",  
                 passwd="1234", 
                 database="rasa_db") 
              mycursor = mydb.cursor() 
              sql='INSERT INTO table3 (name, email,entry_date) VALUES ("{0}","{1}","{2}");'.format(Name,Email,Date)
              mycursor.execute(sql) 
              mydb.commit()
              print("Changes Made")

# if __name__=="__main__":
#    DataUpdate("Pratyush Parida","pratyushparida8@gmail.com")