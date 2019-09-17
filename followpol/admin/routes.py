from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from followpol import db
from followpol.models import User
from followpol.admin.forms import LoginForm

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

@admin.route('/adminpage')
@login_required
def adminpage():
	return render_template('adminpage.html', title='Admin Pages')
