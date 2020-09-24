##def div42by(divideBy):
##    try:
##        return 42/divideBy
##    except ZeroDivisionError:
##        print("Erro dividindo por zero")
##        
##print(div42by(2))
##print(div42by(12))
##print(div42by(0))
##print(div42by(1))
##print(div42by(5))


print('quantos gatos: ')
numCats = input()
try:
    if int(numCats) >= 4:
        print('q monte')
    else:
        print('poucos')
except:
    print('Erro')
