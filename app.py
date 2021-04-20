from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='somekey'

@app.route('/')
def index():
    if 'mensaje' not in session:
        session['mensaje']=""
    if 'numero' not in session:
        session['numero']=random.randint(1,101)
    if 'color'not in session:
        session['color']=None
    return render_template("index.html", mensaje = session['mensaje'],block_color= session['color'])

@app.route('/adivina', methods=['POST'])
def guess():
    valor = int(request.form['numero'])
    if valor == session['numero']:
        session['mensaje']= "You win!"
        session['color'] = "blue"
    if valor > session['numero']:
        session['mensaje']= "Too High"
        session['color'] = "red"
    elif valor < session['numero']:
        session['mensaje']="Too Low"
        session['color'] = "red"
    return redirect('/')

@app.route('/reset')
def reset():
    session['numero']
    session.pop("numero")
    session.pop("mensaje")
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)