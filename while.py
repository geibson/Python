repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    

    while valid_preco == False:
        preco = input('Digite o preco: ')
        try:
            preco = float(preco)
            if preco <= 0:
                print('preço maior q zero')
            else:
                valid_preco = True
        except:
            print("formato invalido, somente numeros e ponto '.'.")
            

        
    fatura.append([produto,preco])
    total += preco
    valid_preco = False
    repetir =  input('Deseja comprar mais alguma coisa? S ou N ')
    
    
for i in fatura:
    print(i[0],'-',i[1])
print('O total é ',total)



##for i in range(0,10):
##    print(10-i)

##compras = ['arroz','carne','feijao','massa'],['carne','frango','peixe'],['leite','yougurt']
##
##for i in compras:
##    for item in i:
##        print(item)
##
##

##
##cores = {'verde':'green','preto':'black','azul':'blue'}
##
##for i in cores:
##    print(i,':',cores[i])



##
##vendas = [1000,450,300,920,600]
##
##total = 0
##for i in vendas:
##    total += i
##    print(total)
##


##compras = ['arroz','carne','feijao','massa']
##nome = 'joaquim'
##
##for i in nome:
##    print(i)

##x=0
##pessoas = []
##while x <4:
##    nome = input('qual o seu nome')
#### evitar nome joaoa adicionado a lista
##    if nome == 'joao':
##        break
##    pessoas.append(nome)
##    x += 1
##print (pessoas)
