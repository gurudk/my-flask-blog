from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, Form, validators

import random


SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)


class SimpleForm(FlaskForm):
    example = RadioField('Label', choices=[('value', 'description'), ('value_two', 'whatever')])


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    form = SimpleForm()
    delay_days = str(random.randint(1, 100))
    delay_payoff = str(random.randint(1, 100000))

    form.example.choices = [('value', '(0, 100)'), ('value_two', '('+delay_days+','+delay_payoff+')')]

    if form.validate_on_submit():
        print(form.example.data)
    else:
        print(form.errors)
    return render_template('example.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

