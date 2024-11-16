from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("login", methods=['GET', 'POST'])
def login():
   if request.method == "POST":   
    username = request.form.get('username')
    password = request.form.get('password')
   return "<h1> login </h1>"

@auth.route("logout")
def logout():
    return "<h1>logout</h1>"

@auth.route("sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password_temp = request.form.get('password')
        password = generate_password_hash(password_temp, method='sha256')
        flash("Accout Successfully created")
        return redirect(url_for('views.Index'))
    return "<h1>sign up</h1>"
