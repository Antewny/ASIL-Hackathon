from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

users = {
    "Katy Lio": {
        "days_kept_up": 1,
        "creature_name": "Fido",
        "creature_level": 1,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 30
    },
    "Bili Bob": {
        "days_kept_up": 1,
        "creature_name": "Armagedon",
        "creature_level": 2,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 60
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    user_logged_in = True
    if request.method == 'POST':
        # Get the selected character from the form
        selected_character = request.form.get('character')
        
        # Handle the selected character (e.g., print it, store it, etc.)
        if selected_character:
            print(f"Selected character: {selected_character}")
        else:
            print("No character selected")

        return render_template('index.html', selected_character=selected_character)
    
    return render_template('index.html', user_logged_in=user_logged_in, selected_character=None)

@app.route("/profile")
def profile():
    username = "Bili Bob"
    user_data = users[username] 

    today = "November 17, 2024"
    checked_in_today = today in user_data['checked_in_days']

    return render_template(
        "profile.html",
        user_logged_in=True,
        username_placeholder=username,
        days_kept_up_placeholder=user_data['days_kept_up'],
        pet_name_placeholder=user_data['creature_name'],
        current_goal_placeholder=user_data['current_goal'],
        pet_level_placeholder=user_data['creature_level'],
        checked_in_days=user_data['checked_in_days'],
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


@app.route('/checkin')
def checkin():
    return render_template('checkin.html',  user_logged_in=True)

if __name__ == '__main__':
    app.run(debug=True)


