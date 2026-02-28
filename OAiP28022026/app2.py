from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<a>/<op>/<b>/')
def index2(a,b,op):
    a = float(a)
    b = float(b)

    return render_template('index2.html', a=a, b=b, op=op)

if __name__ == '__main__':
    app.run(debug=True)