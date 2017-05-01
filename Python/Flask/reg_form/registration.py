from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'jy5iu#fjlkj!'
@app.route('/')
def index():
    return render_template('index.html', methods=['GET'])

@app.route('/register', methods=['POST'])
def reg():
    session['email'] = request.form['email']
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']
    password = session['password']

# email validation
    if len(session['email']) < 1:
        flash('Email cannot be blank')
    elif not EMAIL_REGEX.match(session['email']):
        flash('Please enter a valid email')
#first name validation
    elif not re.match(r'^[A-z][A-z|\.|\s]+$',session['fname']):
        flash('first name cannot contain numbers or symbols')
#last name validation
    if not re.search(r'^[A-z][A-z|\.|\s]+$',session['lname']):
        flash('last name cannot contain numbers or symbols')
        #password validation
    elif len(password) < 8:
        flash('Password must be more than 8 characters')
    elif password != session['confirm']:
        flash('Passwords do not match. Try again')
    else:
        flash('Thanks for submitting your information.')
    return redirect('/')
app.run(debug=True)
