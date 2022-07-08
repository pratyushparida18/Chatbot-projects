from sre_constants import SUCCESS
from ssl import HAS_TLSv1_1
from flask import Flask, render_template, request, redirect
import mysql.connector


app = Flask(__name__)
mydb = mysql.connector.connect(
                 host="localhost", 
                 user="root",  
                 passwd="1234", 
                 database="rasa_db") 
mycursor = mydb.cursor() 

@app.route('/')
def login():
    return render_template("login.html")



@app.route('/form_login',methods=['POST'])
def check1():
    
    if request.method == 'POST':
      name1=request.form['username']
      pwd=request.form['password']
      sql="select name,password from table2"
      mycursor.execute(sql) 
      table = mycursor.fetchall()
      if table==[]:
        return 'No users found!'
      a = (name1,pwd)
      if a in table:
        return redirect('/users')
      # for user in table:
      #   if user[0]==name1:
      #     if user[2]==pwd:
      #       return redirect('/users')
      #     else:
      #       return render_template('login.html',info='Invalid Password')
      else:
        return render_template('login.html',info='Invalid Credentials')
    else:
      return redirect('/login')
    



@app.route('/signup',methods=['POST','GET'])
def check2():
    if request.method == 'POST':
      name=request.form['username']
      email=request.form['mail']
      pwd=request.form['password']
      pwd2=request.form['password_2']
      if pwd!=pwd2:
        return render_template('signup.html',info='Password is not matching')
      else:
        sql='INSERT INTO table2 (name, email, password) VALUES ("{0}","{1}", "{2}");'.format(name,email,pwd2) 
        mycursor.execute(sql) 
        mydb.commit()
        return render_template('login.html')
    return render_template('signup.html')

@app.route('/forgot_password',methods=['POST','GET'])
def check3():
    if request.method == 'POST':
      email=request.form['email']
      pwd=request.form['password']
      pwd2=request.form['password2']
      if pwd!=pwd2:
        return render_template('forgot_password.html',info='Password is not matching')
      else:
        # sql='INSERT INTO table2 (name, email, password) VALUES ("{0}","{1}", "{2}");'.format(name,email,pwd2)  
        sql='UPDATE table2 SET password="{0}" WHERE email="{1}";'.format(pwd,email)
        mycursor.execute(sql) 
        mydb.commit()
        return render_template('login.html')
    return render_template('forgot_password.html')


@app.route('/statistics')
def stats():
  sql2='SELECT count(*) FROM table3 ;'
  mycursor.execute(sql2) 
  table2 = mycursor.fetchall()
  
  sql3='SELECT count(*) FROM table3 WHERE entry_date = CURDATE() ;'
  mycursor.execute(sql3) 
  table3 = mycursor.fetchall()

  sql4='select count(*) from table3 where week(entry_date)=week(now());'
  mycursor.execute(sql4) 
  table4 = mycursor.fetchall()

  sql5='select count(*) from table3 where MONTH(entry_date)=MONTH(now());'
  mycursor.execute(sql5) 
  table5 = mycursor.fetchall()
  return render_template('statistics.html',userDetails2=table2[0][0],userDetails3=table3[0][0],userDetails4=table4[0][0],userDetails5=table5[0][0])

@app.route('/users')
def DataUpdate(): 
              
              sql="select name,email from table3;"
              mycursor.execute(sql) 
              table = mycursor.fetchall()
              
              sql2='SELECT count(*) FROM table3 ;'
              mycursor.execute(sql2) 
              table2 = mycursor.fetchall()
              
              sql3='SELECT count(*) FROM table3 WHERE entry_date = CURDATE() ;'
              mycursor.execute(sql3) 
              table3 = mycursor.fetchall()

              sql4='select count(*) from table3 where week(entry_date)=week(now());'
              mycursor.execute(sql4) 
              table4 = mycursor.fetchall()

              sql5='select count(*) from table3 where MONTH(entry_date)=MONTH(now());'
              mycursor.execute(sql5) 
              table5 = mycursor.fetchall()
              return render_template('users2.html',userDetails=table,userDetails2=table2[0][0],userDetails3=table3[0][0],userDetails4=table4[0][0],userDetails5=table5[0][0])



if __name__ == '__main__':
    app.run(debug=True)
