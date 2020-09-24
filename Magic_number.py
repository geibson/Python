import random
cont = False
ma_magic = random.randint(1,10)
print('Vamos jogar um jogo? ')
while cont == False:    
    for tents in range(1,6):
        user_magic = int(input("DIgite um numero entre 1 e 10: "))
        if ma_magic == user_magic:
            print('Acerto Miseravi!!')
            cont = True
            break
        elif ma_magic > user_magic:
            print('Muito Baixo')
        elif ma_magic < user_magic:
            print('Muito Alto')
    break
if cont == False:
    print('ERRRROOOOUUUUU '+ str(tents)+ ' vezes, o número era '+ str(ma_magic))
print (tents)
