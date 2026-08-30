from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Funcionando"

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)