import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repeat = 3

print('este programa marca o tempo, digite a palavra PROGRAMACAO '+str(repeat)+' .')
input('Aperte enter para começar')



while vez <= repeat:
    inicio = t.thread_time()
    input('digite a palavra: ')
    fim = t.thread_time()
    tempo = round(fim - inicio)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+'X'
    legenda.append(vezstr)
    vez += 1


plt.xticks(vezes,legenda)
plt.plot(vezes,tempos)
plt.show()

