# Index
# profile
# registration 

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/registration")
# def registration():
#     return render_template("registration.html")

# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

# if __name__ == '__main__':
#     app.run(debug=True)
    

from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True; 
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route("/profile")
def profile():
    # username = "Iuliana Cherevko"
    # days_kept_up = 10
    # creature_name = "Fido"
    # creature_level = 5
    return render_template("profile.html")#, username=username, days_kept_up=days_kept_up, creature_name=creature_name, creature_level=creature_level)

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    #return something

if __name__ == '__main__':
    app.run(debug=True)