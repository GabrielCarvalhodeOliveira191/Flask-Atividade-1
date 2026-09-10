from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('exercicio1.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    ano_nascimento = request.form['ano_nascimento']
    idade = 2026 - int(ano_nascimento)

    return render_template('exercicio1.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)