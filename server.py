from flask import Flask, render_template, redirect
import os
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

year = dt.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html",year=year)


@app.route('/twitter')
def twitter():
    return redirect(location=os.environ.get('TWITTER_URL'), code=302)


@app.route('/facebook')
def facebook():
    return redirect(location=os.environ.get('FACEBOOK_URL'), code=302)


@app.route('/linkedin')
def linkedin():
    return redirect(location=os.environ.get('LINKEDIN_URL'), code=302)


@app.route('/email')
def email():
    return redirect(location=os.environ.get('EMAIL_ID'), code=302)


@app.route('/github')
def github():
    return redirect(location=os.environ.get('GITHUB_URL'), code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
