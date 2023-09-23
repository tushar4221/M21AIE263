from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (in-memory storage)
users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            users.append({'username': username, 'password': password})
            return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
