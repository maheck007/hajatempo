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
        return "Fofinho"

def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    print("---------------------------------------------")
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Você é classificado como: {classificacao}")

if __name__ == "__main__":
    main()
