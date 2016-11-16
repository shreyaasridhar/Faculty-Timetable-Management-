from flask import Flask, render_template, request, flash, redirect, url_for
# from forms.login_form import login_form
# from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine, MetaData, Table

app = Flask(__name__)
engine = create_engine('mysql://root:password@localhost/test', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()
app = Flask(__name__)


@app.route("/")
@app.route("/login")
def contact():
    return render_template("ftms.html")


@app.route('/submit', methods=['POST'])
def submit():
    # Read the HTTP POST request parameter from request.form
    _username = request.form['username']


@app.route('/profile/<name>')
def index():
    return render_template("ftms2.html", name=, id='25')


if __name__ == "__main__":
    app.run(debug=True)
