from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/login")
def login():
    return render_template("ftms.html")


@app.route('/profile/<name>')
def index(name):
    return render_template("ftms2.html",name=name,id='25')


if __name__ == "__main__":
    app.run(debug=True)
