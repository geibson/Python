idade = int(input('Digite a sua idade: '))
sexo = input('sexo m ou f: ').lower()
cidade = input('digite a cidade: ').lower()

if cidade == 'rio' or cidade == 'sp':
    if sexo == 'm':
        if idade < 18:
            print ('Homem menor de idade da região')
        else: print('Homem maior de idade da região')

    elif sexo == 'f':
        if idade < 18:
            print ('Mulher menor de idade da região')
        else: print('Mulher maior de idade da região')

    else: print('erro na entrada de dados')
else:
    print ('não e da regiao sudeste')
