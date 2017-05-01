from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'wow'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def survey():
    print 'Thanks!'
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('results.html')

@app.route('/', methods=['GET'])
def button():
    return redirect('/')
app.run(debug=True)
