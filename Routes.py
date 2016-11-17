from flask import Flask, render_template, request, flash, redirect, url_for
from login import LoginForm
from form import SwapForm
from sqlalchemy import create_engine, MetaData, Table


app = Flask(__name__)
engine = create_engine('mysql://root:password@localhost/db', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()
#con.execute('create table Teacher (tid integer(2) primary key,name varchar(20))')
app.config['SECRET_KEY'] = 'SECRET'  # Flask-WTF: Needed for CSRF

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
    name=con.execute('SELECT Fac_Name FROM Faculty WHERE Fac_Name=_username')
    if form.validate_on_submit():  # POST request with valid input?
      # Verify username and passwd
      
      if (form.username.data == name and form.passwd.data == 'xxxx'):
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
    ID=con.execute('SELECT Fac_ID FROM Faculty WHERE Fac_Name=name')
    return render_template("profile.html",name=name,id=ID)


@app.route("/swap", methods=['GET', 'POST'])
def submit():
  forms = SwapForm()
   if request.method == 'POST':
     if form.validate() == False:
      flash('All fields are required.')
      return render_template('swap.html', form=form)
    else:
    Fday = request.forms['FromDay']
    Tday = request.forms['ToDay']
    Fp = request.forms['FromPeriod']
    Tp = request.forms['ToPeriod']
    if form.validate_on_submit():  # POST request with valid input?
      
      if (form.username.data == name and form.passwd.data == 'xxxx'):
         return redirect(url_for('Profile.html',name=_username))
      else:
         # Using Flask's flash to output an error message
         flash(u'Username or password incorrect')
   if request.method == 'GET':
    return render_template('swap.html', form=forms)      
   else:
      return "I think its Some Random HTTPMethod! :P" 



if __name__ == "__main__":
    app.run(debug=True)
