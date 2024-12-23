from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Predefined credentials
users_db = {
    "rafayraheel00@gmail.com": "demo123"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username exists and password matches
        if users_db.get(username) == password:
            return redirect(url_for('welcome', username=username))
        else:
            return "Invalid credentials, please try again!"
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        if username in users_db:
            return "Username already taken, please choose another!"
        
        # Add the new user to the database (simulation)
        users_db[username] = password
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/welcome/<username>')
def welcome(username):
    # Render a welcome page template and pass the username
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
