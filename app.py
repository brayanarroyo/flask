from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')
    
@app.route('/obtener_csv',methods=['POST'])
def csv():
    name_csv = request.form['nombre']
    global df
    df = pd.read_csv(name_csv) 
    global titulos
    titulos = list(df)
    return redirect(url_for('graficar'))

@app.route('/graficar')
def graficar():
    return render_template('graficar.html', tables=[df.to_html(classes='data')], titles=titulos )

@app.route('/graficar/seleccion',methods=['POST'])
def graficar_seleccion():
    columna = request.form['columna']
    tipo = request.form['tipo']
    if(tipo == 'Puntos'):
        print('1')
    if(tipo == 'Lineas'):
        print('2')
    if(tipo == 'Pastel'):
        print('3')
    if(tipo == 'Barras'):
        print('4')

    return redirect(url_for('mostrar'))

@app.route('/mostrar')
def mostrar():
    return render_template('mostrar.html', imagen="https://d2ci88w16yaf6n.cloudfront.net/p/assets/animations/hurricane_1e8e060c71635d9c72b776820991d419.png" )

if __name__ == "__main__":
    app.run(debug=True)