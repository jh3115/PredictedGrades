from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

GRADES = [
    "A1", "A2",
    "B1", "B2", "B3",
    "C1", "C2", "C3",
    "D1", "D2", "D3"
]


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['Name']
    subject = request.form['myList']
    name = text.upper()
    grade = choice(GRADES)
    return f"Congratulations {name} you received an {grade} for {subject}"


if __name__ == '__main__':
    app.run(debug=True)
