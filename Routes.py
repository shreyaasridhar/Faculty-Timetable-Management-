from flask import Flask, render_template, request, flash, redirect, url_for
from login import LoginForm
#from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine, MetaData, Table


app = Flask(__name__)
engine = create_engine('mysql://root:password@localhost/test', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()
#con.execute('create table Teacher (tid integer(2) primary key,name varchar(20))')
app.config['SECRET_KEY'] = 'SECRET'  # Flask-WTF: Needed for CSRF

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if request.method == 'POST':
    _username = request.form['username']
    if form.validate_on_submit():  # POST request with valid input?
      # Verify username and passwd
      
      if (form.username.data == 'Peter' and form.passwd.data == 'xxxx'):
         return redirect(url_for('index',name=_username))
      else:
         # Using Flask's flash to output an error message
         flash(u'Username or password incorrect')
   if request.method == 'GET':
    return render_template('login.html', form=form)      
   else:
      return "I think its Some Random HTTPMethod! :P" 


'''
@app.route('/submit', methods=['POST'])
def submit():
    # Read the HTTP POST request parameter from request.form
    _username = request.form['username']

    if _username:
        return redirect(url_for('index',_username=_username))
    else:
        return 'Please go back and enter your name...'
'''

@app.route('/profile/<name>')
def index(name):
    return render_template("profile.html",name=name)


if __name__ == "__main__":
    app.run(debug=True)
