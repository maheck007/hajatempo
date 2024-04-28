from flask import Flask, request, render_template

app = Flask(__name__)

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso (em kg) e altura (em metros) fornecidos.
    """
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em categorias: Magrelo, Tripa Seca ou Fofinho.
    """
    if imc < 18.5:
        return "Magrelo"
    elif 18.5 <= imc < 25:
        return "Tripa Seca"
    else:
        return "Tá gordo meu filho"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    return render_template('resultado.html', imc=imc, classificacao=classificacao)

if __name__ == '__main__':
    app.run(debug=True)



