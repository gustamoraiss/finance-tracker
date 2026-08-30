from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Funcionando"

@app.route('/adicionar', methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':

        valor = request.form['valor']
        tipo = request.form['tipo']
        categoria = request.form['categoria']
        data = request.form['data']
        descricao = request.form['descricao']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO transacoes(
        valor,
        tipo,
        categoria,
        data,
        descricao)
        VALUES (?,?,?,?,?)
        ''', (valor, tipo, categoria, data, descricao))
        conn.commit()

        conn.close()

        return redirect(url_for('index'))

    return render_template('adicionar.html')

@app.route('/listar', methods=['GET'])
def listar():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM transacoes''')
    transacoes = cursor.fetchall()

    conn.close()

    return render_template('listar.html', transacoes=transacoes)

if __name__ == '__main__':
    app.run(debug=True)