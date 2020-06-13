import os
from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page>')
def html_page(page):
    return render_template(f'{page}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #saveas_text(data)
            saveas_csv(data)
            return redirect('/thankyou')
        except:
            return "did not save to database"
    else:
        return 'error occured. try again'


def saveas_txt(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\nemail: {email}\nsubject: {subject}\nmessage: {message}\n')


def saveas_csv(data):
    with open('database.csv', mode='a', newline='') as dbase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        csv_writer = csv.writer(dbase, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])