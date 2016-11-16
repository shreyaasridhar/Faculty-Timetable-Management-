from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


@app.route("/")
def home():
    return render_template('ftms.html')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/test'


if __name__ == '__main__':
    app.run(debug=True)

