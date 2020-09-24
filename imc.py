import Func as f
print ('Vamos calcular o IMC')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o Sexo, M ou F: ').upper()
    if sexo == 'M' or sexo == 'F':
        valid_sexo = True
    else:
        print('Sexo invalido \n')
        

valid_peso = False
while valid_peso == False:
    peso = input('Digite o Peso: ')
    try:
        peso = float(peso)
        if peso < 0 and peso > 200:
            print('Peso Invalido')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso invalido, use so .')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura: ')
    try:
        altura = float(altura)
        if altura <= 0 and altura > 300:
            print('altura Invalido')
        else:
            valid_altura = True
            print('\n')
    except:
        print('altura invalido, use so .')        



v_imc = str(f.imc(peso,altura))
c_imc = f.class_imc(sexo,peso,altura)

print('O seu IMC é: ',v_imc[0:5])
print('A sua classificação é: ',c_imc)
