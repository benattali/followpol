from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddf0f203ed214a2d1de14957494c0f5a'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/score')
def score():
    return render_template('score.html', title='Score')

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@cak.com' and form.password.data == '123456':
			flash('Logged in as admin', 'success')
			return redirect(url_for('adminpage'))
		else:
			flash('Login unsuccessful', 'danger')
	return render_template('adminlogin.html', title='Admin Login', form=form)

@app.route('/adminpage')
def adminpage():
	return render_template('adminpage.html', title='Admin Pages')

if __name__ == '__main__':
	app.run(debug=True)