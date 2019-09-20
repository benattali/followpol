import os
from flask import Blueprint, render_template, url_for, flash, redirect, current_app
from flask_login import login_user, current_user, logout_user, login_required
from followpol import db
from followpol.models import User
from followpol.admin.forms import LoginForm, UploadCSV
import csv

admin = Blueprint('admin', __name__)

@admin.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
	if current_user.is_authenticated:
		return redirect(url_for('admin.adminpage'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and form.password.data == user.password:
			login_user(user, remember=form.remember.data)
			return redirect(url_for('admin.adminpage'))
		else:
			flash('Login unsuccessful. Please check your email and password.', 'danger')
	return render_template('adminlogin.html', title='Admin Login', form=form)

@admin.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))

def save_csv(form_csv):
	_, f_ext = os.path.splitext(form_csv.filename)
	csv_fn = "twitter_data" + f_ext
	csv_path = os.path.join(current_app.root_path, 'data_files', csv_fn)

	previous_csv = []
	with open('followpol/data_files/twitter_data.csv', 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		for line in csv_reader:
			previous_csv.append(line)

	form_csv.save(csv_path)

	return csv_fn

@admin.route('/adminpage', methods=['GET', 'POST'])
@login_required
def adminpage():
	form = UploadCSV()
	if form.validate_on_submit():
		if form.csv.data:
			csv_file = save_csv(form.csv.data)
			flash('The file was successfully uploaded', 'info')
	else:
		flash('Looks like this file is not in a CSV format', 'danger')
	return render_template('adminpage.html', title='Admin Pages', form=form)
