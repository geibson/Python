cores = {'red':'vermelho','blue':'azul','green':'verde'}
cor = input('Digite uma cor: ').lower()
color = cores.get(cor,'Cor não existe')
print (color)

