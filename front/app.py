from flask import Flask, render_template, flash, redirect, request, url_for, session, jsonify, json
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
import os
import requests, datetime
from forms import RegisterForm

app = Flask(__name__)
login = LoginManager(app)
app.config['SECRET_KEY'] = 'DinoTradeTheBest123_secret_key'
# ...
from flask_login import UserMixin

all_user = {}


class User(UserMixin):
    id_t = 0
    username = ""
    age = ""
    ava = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Anonymous.svg"
    birth = ""
    city = ""
    status = ""
    regtime = ""
    country = ""
    sex = ""
    curdial = 0

    def __init__(self, id):
        """Constructor"""
        self.id = id

    def getid(self):
        return self


@login.user_loader
def load_user(user):
    return User.getid(all_user[user])


ip = 'http://192.168.43.33:5000/tests/endpoint'
data_g = {}


@app.route('/main')
def main():
    return render_template('index.html')  # ,data_g=data_g,data=data_i)


@app.route('/register_perm')
def register_perm():
    form = RegisterForm()
    if form.validate_on_submit():
        print(True)
    return render_template('register_perm.html', form=form)


@app.route('/main2')
def main2():
    return render_template('videos.html')  # ,data_g=data_g,data=data_i)


@app.route('/cam2')
def cam2():
    return render_template('cam2.html')  # ,data_g=data_g,data=data_i)


@app.route('/cam3')
def cam3():
    return render_template('cam3.html')  # ,data_g=data_g,data=data_i)


@app.route('/passes')
def passes():
    return render_template('passes.html')  # ,data_g=data_g,data=data_i)


@app.route('/passes2')
def passes2():
    return render_template('passes2.html')  # ,data_g=data_g,data=data_i)


@app.route('/notifications')
def notifications():
    return render_template('notifications.html')  # ,data_g=data_g,data=data_i)


@app.route('/notifications2')
def notifications2():
    return render_template('notifications2.html')  # ,data_g=data_g,data=data_i)


@app.route('/settings')
def settings():
    return render_template('settings.html')  # ,data_g=data_g,data=data_i)


@app.route('/settings2')
def settings2():
    return render_template('settings2.html')  # ,data_g=data_g,data=data_i)


@app.route('/videos')
def videos():
    return render_template('videos.html')  # ,data_g=data_g,data=data_i)


@app.route('/')
def home():
    return redirect(url_for("main2"))


@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if current_user.is_authenticated:
        return redirect(url_for("main2"))

    if request.form:
        return redirect(url_for("main2"))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
