from flask import Flask, render_template, request, flash, redirect, url_for,jsonify
from login import LoginForm
from form import SwapForm
import simplejson
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData, Table
import re

app = Flask(__name__)

engine = create_engine('mysql://root:password@localhost/db', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()
Session = scoped_session(sessionmaker(bind=engine))
dbsession = Session()
#con.execute('create table Teacher (tid integer(2) primary key,name varchar(20))')
app.config['SECRET_KEY'] = 'SECRET'  # Flask-WTF: Needed for CSRF
_username=""
@app.route("/")
def home():
  return render_template('home.html')


@app.route("/about")
def about():
  return render_template('about.html')  

@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if request.method == 'POST':
    _username = request.form['username']
    name=con.execute('SELECT Fac_Name FROM Faculty WHERE Fac_Name=%s',_username)
    if form.validate_on_submit():  # POST request with valid input?
      # Verify username and passwd
      # 
      if (name and form.passwd.data == 'xxxx'):
         return redirect(url_for('index',name=_username))
      else:
         # Using Flask's flash to output an error message
         flash(u'Username or password incorrect')
   if request.method == 'GET':
    return render_template('login.html', form=form)      
   else:
      return "I think its Some Random HTTPMethod! :P" 


@app.route('/profile/<name>')
def index(name):
    array=[]
    arr=[]
    
    for i in con.execute('SELECT Fac_ID FROM Faculty WHERE Fac_Name=%s',name):
      arr.append(i)
    print arr
    ID=arr[0]
    ID=str(ID).strip('(),')
    print ID
    for i in con.execute('SELECT Day,Hour from timetable WHERE Teach_ID in (SELECT Teach_ID from Teaches where Fac_ID=F2))'):
      array.append(i)
    print array 
    a=[] 
    for i in ('SELECT DISTINCT Sec_Id from teaches where Fac_ID=%s',ID):
      a.append(i)
    sql=a[0]
    print sql
    sql=str(ID).strip('(),') 

    return render_template("profile.html",name=name,id=ID,array=array,sql=sql)


@app.route('/profile/<name>/swap', methods=['GET', 'POST'])
def submit(name):
  form = SwapForm()
  print name
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('swap.html', name=name,form=form)
    else:
     Fday = request.form['FromDay']
     Tday = request.form['ToDay']
     Fp = request.form['FromPeriod']
     Tp = request.form['ToPeriod']
      #con.execute('SELECT ')
      #con.execute('UPDATE ')
     return redirect(url_for('index',name=name))#redirect(url_for('Profile.html',name=_username))
    
  if request.method == 'GET':
    return render_template('swap.html',name=name, form=form)      
  else:
      return "I think its Some Random HTTPMethod! :P" 



if __name__ == "__main__":
    app.run(debug=True)
