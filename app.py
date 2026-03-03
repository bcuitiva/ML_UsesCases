from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/Almonacid')
def UseCase():
    return render_template('UseCase_Almonacid.html')