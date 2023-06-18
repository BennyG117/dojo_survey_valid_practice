from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.survey_model import Dojo



#! incomplete routes
@app.route('/')
def main_page():
    return render_template("index.html")


#! incomplete routes
@app.route('/process', methods = ['POST'])
def submit_data():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    print(request.form)
    return redirect('/result')

#! incomplete routes
@app.route('/result')
def show_results():
    return render_template('indexR.html')