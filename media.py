repetir = 's'
validan = False
validaf = False

while repetir == 's':
    nome = input('Digite o nome: ')
    while validan == False:
        nota1 = input('digite nota 1: ')
        nota2 = input('digite nota 2: ')
        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
            if nota1<0 or nota2<0:
                print('Notas tem que ser maiores ou iguais a 0' )
            if nota1 > 10 or nota2 > 10:
                print('Notas tem que ser maiores ou iguais a 10' )
            else: validan = True
        except:
            print('Quem sabe?!?!?!')

    while validaf == False:         
        faltas = input('Total de faltas: \n')
        try:
            faltas = int(faltas)
            
            if faltas<0 or faltas>20:
                print('Faltas tem que ser ficar entre 0 e 20' )
            
            else: validaf = True
        except:
            print('Quem sabe?!?!?!')
            
    
        assid = int(20-faltas)/20
        media = (nota1 + nota2)/2
        if media >= 6 and assid >= 0.7:
            resultado = 'Aprovado'
        elif media < 6 and assid < 0.7:
            resultado = 'Reprovado media e faltas'
        elif media < 6:
            resultado = 'reprovado por media'
        elif assid < 0.7:
            resultado = 'reprovado por falta'
        else:
            print ('erro')
          

    print('Nome: ',nome)
    print('Media: ',media)
    print('Assiduidade: ', str(assid*100)+'%')
    print ('Resultado: ',resultado)
    validan = False
    validaf = False 
    repetir = input('Continuar? S ou N')
