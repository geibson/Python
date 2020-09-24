meses = ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')
nasc =  input('Digite a data de nascimento DD-MM-AAAA: ')
indice = int(nasc[3:5])-1
mes = meses[indice]

print ('seu aniversario e mes: ', mes)
