from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'wowza'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def show():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    if len(request.form['name']) < 1:
        flash('Please enter a valid name')
        return redirect('/')
    if len(request.form['comment']) < 1 or len(request.form['comment']) > 120:
        flash('Please enter a valid comment')
        return redirect('/')
    else:
        return render_template('results.html')
app.run(debug=True)
