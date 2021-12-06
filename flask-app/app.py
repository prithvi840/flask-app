import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request
from user import User
from common.database import Database
import common.send_email as send_email

load_dotenv(os.path.join(os.getcwd(), '.env'))

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def index():
    return render_template("info.html")


@app.route('/login')
def login_page():
    return render_template("login.html")


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
        send_email.send_email(session['email'])

    else:
        session['email'] = None

    return render_template('profile.html', email=session['email'])


@app.route('/register')
def register_template():
    return render_template("register.html")


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)
    session['email'] = email

    return render_template('profile.html', email=session['email'])


@app.route('/registered')
def registered_email_template():
    return render_template("registered_users.html")


@app.route('/auth/registered', methods=['POST'])
def send_mail_to_registered():
    emails = Database.find(collection="users", query={})
    send_email.send_emails_registered(emails, "Greetings")

    return "Emails sent successfully"


@app.route('/unregistered')
def unregistered_email_template():
    return render_template("unregistered_users.html")


@app.route('/auth/unregistered', methods=['POST'])
def send_mail_to_unregistered():
    emails = Database.find(collection="unregister", query={"email": {}})
    send_email.send_emails_registered(emails, "Promotional offers")

    return "Email sent successfully!!!"


if __name__ == '__main__':
    app.run(debug=True)
