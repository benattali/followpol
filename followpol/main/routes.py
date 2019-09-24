from flask import Blueprint, render_template, flash, url_for
from followpol.main.forms import TwitterHandleForm
import csv
import pygal

main = Blueprint('main', __name__)

def pieChart(form_data):
    following = {}
    for index, fol in enumerate(form_data):
        if index == 0:
            continue
        elif fol[14] in following:
            following[fol[14]] += 1
        else:
            following[fol[14]] = 1

    pie_chart = pygal.Pie()
    pie_chart.title = 'How many people do they follow?'
    for item in following.items():
        pie_chart.add(item[0], item[1])
    pie_chart.render()
    chart = pie_chart.render_data_uri()

    return chart

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

        chart = pieChart(csv_data)

        return render_template('score.html', twitter_handle=twitter_handle, csv_data=csv_data, chart=chart)
    return render_template('home.html', form=form)

@main.route('/score')
def score():
    return render_template('score.html', title='Score')
