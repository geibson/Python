#nota1 = float(input('digite nota1: '))
#nota2 = float(input('digite nota2: '))
#peso1 = int(input('digite peso1: '))
#peso2 = int(input('digite peso2: '))
#media = (nota1 * peso1 + nota2*peso2) /10
#print 'O resultado e ',media
#if media > 6:
#    print 'aprovado'
#else: print 'reprovado'
#print 'fim'

meses = ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')
data_nasc = input('Digite a data de nascimento DD/MM/AAAA: ')
print data_nasc
mes = data_nasc[2:4]
masani = meses[mes-1]
print 'seu aniversario e mes: ' + masani
