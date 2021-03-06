from app import myobj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import request, redirect, render_template, flash

class SubmitForm(FlaskForm):
	city_name = StringField('city_name')
	submit = SubmitField('submit')

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route('/', methods = ['GET', 'POST'])
def home():
	form = SubmitForm()
	if request.method == "POST":
        	flash(format(form.city_name.data))
	return render_template('home.html', name=name, city_names=city_names, form=form)
