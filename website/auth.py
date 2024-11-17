from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("sign-in", methods=['GET', 'POST'])
def sign_in():
   if request.method == "POST":
    username = request.form.get('username')
    password = request.form.get('password')
    #user = User.query.filter_by(email=email).first()
   return "<h1> login </h1>"

@auth.route("logout")
def logout():
    return "<h1>logout</h1>"

@auth.route('Registration', methods = ['GET', 'POST'])
def registration():
    #data = request.form
    if request.method == 'POST':
        habit = request.form.get("question1")
        name = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        #time_frame = request.form.get("time_frame")
        #character = request.form.get("character1")
        #time_grab = datetime.now()
        #   time_submitted = time_grab.strftime('%Y-%m-%d %H:%M:%S')
 

        #new_user = User(name=name , password=password, #need character and time maybe
           #             email = email,habit=habit)
        print(habit,name,password,email) 
        #db.session.add(new_user)
        #db.session.commit()
        #print(new_user.name)
        return redirect(url_for('views.index'))
    return render_template("registration.html")