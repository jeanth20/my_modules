from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/create_session')
def create_session():
    # Set session data
    session['username'] = 'JohnDoe'
    session['email'] = 'johndoe@example.com'
    return 'Session created'


@app.route('/check_session')
def check_session():
    # Check session data
    username = session.get('username')
    email = session.get('email')
    if username and email:
        return f"Username: {username}, Email: {email}"
    else:
        return 'Session data not found'


if __name__ == '__main__':
    app.run()
