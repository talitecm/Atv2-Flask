from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/login')
def login():
    return render_template('login.html')