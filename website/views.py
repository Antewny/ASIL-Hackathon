from flask import Blueprint , render_template , request, Flask, redirect, url_for, flash
from datetime import datetime
from . import db
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash


app = Flask(__name__)
views = Blueprint("views", __name__)

@views.route('Index')
def index():
    return render_template("index.html")

@views.route('Profile', methods = ['GET','POST'])
def profile():
   return render_template("profile.html")

@views.route('Check-in', methods= ['GET', 'POST'])
def check_in():
    if request.method == 'POST':
        return render_template("checkin.html")
    return render_template('checkin.html')