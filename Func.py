def imc(peso,altura):
    imc = peso/(altura*altura)
    return imc

def class_imc(sexo,peso,altura):
    valor_imc = imc(peso,altura)

    if sexo == 'M':
        if valor_imc <= 20.7:
            return "Abaixo do peso"
        elif valor_imc > 20.7 and valor_imc <= 26.4:
            return "Peso normal."
        elif valor_imc > 26.4 and valor_imc <= 27.8:
            return "Pouco acima do peso"
        elif valor_imc > 27.8 and valor_imc <= 31.1:
            return "Acima do peso"
        elif valor_imc > 31.1:
            return "Obeso. IMC"
        else:
            return "Erro de calculo"

    if sexo == 'F':
        if valor_imc <= 19.1:
            return"Abaixo do peso."
        elif valor_imc > 19.1 and valor_imc <= 25.8:
            return"Peso normal."
        elif valor_imc > 25.8 and valor_imc <= 27.3:
            return"Pouco acima do peso."
        elif valor_imc > 27.3 and valor_imc <= 32.3:
            return"Acima do peso. IMC."
        elif valor_imc > 32.3:
            return "Obeso."
        else:
            return "Erro de calculo"
