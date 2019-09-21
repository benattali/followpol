from flask import Blueprint, render_template, flash, url_for
from followpol.main.forms import TwitterHandleForm
import csv
import pygal

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


        pie_chart = pygal.Pie()
        pie_chart.title = 'Browser usage in February 2012 (in %)'
        pie_chart.add('IE', 19.5)
        pie_chart.add('Firefox', 36.6)
        pie_chart.add('Chrome', 36.3)
        pie_chart.add('Safari', 4.5)
        pie_chart.add('Opera', 2.3)
        pie_chart.render()
        chart = pie_chart.render_data_uri()

        return render_template('score.html', twitter_handle=twitter_handle, csv_data=csv_data, chart=chart)
    return render_template('home.html', form=form)

@main.route('/score')
def score():
    return render_template('score.html', title='Score')
