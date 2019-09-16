from flask import render_template, url_for, flash, redirect, request
from followpol import app, db
from followpol.forms import LoginForm
from followpol.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/score')
def score():
    return render_template('score.html', title='Score')

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
	if current_user.is_authenticated:
		return redirect(url_for('adminpage'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and form.password.data == user.password:
			login_user(user, remember=form.remember.data)
			return redirect(url_for('adminpage'))
		else:
			flash('Login unsuccessful. Please check your email and password.', 'danger')
	return render_template('adminlogin.html', title='Admin Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/adminpage')
@login_required
def adminpage():
	return render_template('adminpage.html', title='Admin Pages')
