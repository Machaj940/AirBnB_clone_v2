#!/usr/bin/python3
'''script that starts a Flask web app'''


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    ''' return Hello HBNB! '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' return HBNB '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_text(text):
    ''' return HBNB '''
    return "C %s" % text.replace(r'_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_text_default(text="is cool"):
    ''' return HBNB '''
    return "Python %s" % text.replace(r'_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' return HBNB '''
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' return HBNB '''
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    ''' return HBNB '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
