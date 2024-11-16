from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("login", methods= ['GET' , 'POST'])
def login():
    return "<h1> login </h1>"

@auth.route("logout")
def login():
    return "<h1>logout</h1>"

@auth.route("sign-up" , methods= ['GET' , 'POST'])
def sign_up():
    return "<h1>sign up</h1>"
