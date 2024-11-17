from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/')
def index():
    user_logged_in = True; 
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route("/profile")
def profile():
    username = "Iuliana Cherevko"
    days_kept_up = 10
    creature_name = "Fido"
    creature_level = 5
    return render_template(
        "profile.html",
        username_placeholder=username,
        days_kept_up_placeholder=days_kept_up,
        pet_name_placeholder=creature_name,
        pet_level_placeholder=creature_level
)

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    #return something

@app.route('/check_in', methods=['POST'])
def check_in():
    goal_followed = request.form.get('goal-followed')
    bad_habit = request.form.get('bad-habit')
    journal_entry = request.form.get('journal')

    # Example processing logic
    print(f"Goal followed: {goal_followed}")
    print(f"Bad habit avoided: {bad_habit}")
    print(f"Journal entry: {journal_entry}")

    # Redirect back to the profile page after check-in
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)


