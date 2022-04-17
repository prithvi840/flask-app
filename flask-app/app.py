from dotenv import load_dotenv
load_dotenv()

from flask import (
    Flask, render_template, session, request, redirect, url_for
)
from user import User
from common import Database, SendEmail, SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY


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
    else:
        return redirect(url_for('register_template'))

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
    with SendEmail():
            SendEmail.signup_email(session['email'])

    return render_template('profile.html', email=session['email'])


@app.route('/registered')
def registered_email_template():
    return render_template("registered_users.html")


@app.route('/auth/registered', methods=['POST'])
def send_mail_to_registered():
    emails = Database.find(collection="users", query={})
    with SendEmail():
        SendEmail.send_emails(emails, 'Discount offers')

    return "Emails sent successfully"


@app.route('/unregistered')
def unregistered_email_template():
    return render_template("unregistered_users.html")


@app.route('/auth/unregistered', methods=['POST'])
def send_mail_to_unregistered():
    emails = Database.find(collection="unregister", query={"email": {}})
    with SendEmail():
        SendEmail.send_emails(emails, 'Promotional Offers')

    return "Email sent successfully!!!"


if __name__ == '__main__':
    app.run(debug=True)
