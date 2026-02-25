from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/me')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'IvanDude' and password == 'Usagi':
            return render_template('index.html')
        else:
            return render_template('login.html')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)