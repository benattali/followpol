from flask import Blueprint, render_template, flash, url_for
from followpol.main.forms import TwitterHandleForm
import csv

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = TwitterHandleForm()
    if form.validate_on_submit():
        twitter_handle = form.handle.data
        flash(f'Results for {form.handle.data}...', 'success')

        csv_data = []
        with open('followpol/data_files/twitter_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                csv_data.append(line)

        return render_template('score.html', twitter_handle=twitter_handle, csv_data=csv_data)
    return render_template('home.html', form=form)

@main.route('/score')
def score():
    return render_template('score.html', title='Score')
