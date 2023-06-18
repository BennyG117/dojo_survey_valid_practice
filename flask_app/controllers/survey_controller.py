from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.survey_model import User



# Home Route
@app.route('/')
def survey_home():
    return render_template("input.html")

# route for the button press to take us to receipt page
@app.route('/receipt/<int:id>')
def show_results(id):
    #info we received from db is now stored in dojo
    dojo=User.get_one({'id':id})
    #apples connects this to html, dojo connects this route to the class method
    return render_template('receipt.html', apples=dojo)

# route to validate submitted data
@app.route('/process', methods = ['POST'])
def process_submit():
    if not User.validate_dojo(request.form):
        return redirect('/')
    # insert form into becoming the user
    dojos = User.save_submission(request.form)

    return redirect(f'/receipt/{dojos}')

