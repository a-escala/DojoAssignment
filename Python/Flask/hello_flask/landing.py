from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/ninjas')
@app.route('/dojos/new')

def index():
    return render_template('index.html')
app.run(debug=True)
