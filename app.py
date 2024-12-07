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

@app.route('/gphero4')
def gphero4():
    return render_template('gphero4.html')

@app.route('/phantom4p')
def phantom4p():
    return render_template('phantom4p.html')

@app.route('/batphantom4p')
def batphantom4p():
    return render_template('batphantom4p.html')

@app.route('/awse40mm')
def awse40mm():
    return render_template('awse40mm.html')

@app.route('/gultra47mm')
def gultra47mm():
    return render_template('gultra47mm.html')

@app.route('/gwatch7')
def gwatch7():
    return render_template('gwatch7.html')