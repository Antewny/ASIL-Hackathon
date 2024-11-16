from flask import Blueprint , render_template , request
import datetime
views = Blueprint("views", __name__)

@views.route('Index')
def index():
    return render_template("index.html")

@views.route('Profile')
def profile():
   return render_template("profile.html")

@views.route('Questions')
def Questions():
    data = request.form
    if request.method == 'POST':
        goal = request.form.get("goal")
        time_frame = request.form.get("time_frame")
        character = request.form.get("time")
        time_grab = datetime.now()
        time_submitted = time_grab.strftime('%Y-%m-%d %H:%M:%S')
    #need more info
    return "<h3>Questions</h3>"
