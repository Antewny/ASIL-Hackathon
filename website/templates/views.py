from flask import Blueprint , render_template

views = Blueprint("views", __name__)

@views.route('Index')
def index():
    return "<h1>index</h1>"

@views.route('Profile')
def profile():
   return "<h2>Profile</h2>"

@views.route('Questions')
def Questions():
    return "<h3>Questions</h3>"
