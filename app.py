from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('start.html')

@app.route('/FirstPage')
def firstPage():
    return render_template('index.html')

@app.route('/useCases')
def useCases():
    return render_template('useCases.html')

@app.route('/Almonacid')
def UseCase1():
    return render_template('useCase_Almonacid.html')

@app.route('/Mendez')
def UseCase2():
    return render_template('useCase_Mendez.html')

@app.route('/Cuitiva')
def UseCase3():
    return render_template('useCase_Cuitiva.html')

@app.route('/Group')
def UseCase4():
    return render_template('useCase_Group.html')