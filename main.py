from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/')
def index():
    return render_template('index.html', user_logged_in=True)

@app.route("/profile")
def profile():
    username = "Iuliana Cherevko"
    days_kept_up = 10
    creature_name = "Fido"
    creature_level = 5
    checked_in_days = ["November 16, 2024"]  # Array of checked-in dates
    current_goal_placeholder = 10

    # Some code to check whether user checked-in today or not for some features at profile.html
    today = "November 17, 2024"  # this is actually working - try out different dates
    checked_in_today = today in checked_in_days

    return render_template(
        "profile.html",
        user_logged_in=True,
        username_placeholder=username,
        days_kept_up_placeholder=days_kept_up,
        pet_name_placeholder=creature_name,
        current_goal_placeholder=current_goal_placeholder,
        pet_level_placeholder=creature_level, 
        checked_in_days=checked_in_days,
        checked_in_today=checked_in_today,
    )

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    #return something

@app.route('/check-in', methods=['POST'])
def check_in():
    bad_habit = request.form.get('bad-habit')
    journal = request.form.get('journal')
    checked_in_days = ["November 16, 2024"]
    return redirect(url_for('profile', checked_in_days=checked_in_days))

if __name__ == '__main__':
    app.run(debug=True)


