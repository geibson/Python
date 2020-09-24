import random

print('Rolar dados de multiplas faces')

i = 1
total = []
val_face = False
tipos = [4,6,8,10,12,15,20,100]

while val_face == False:
    faces = int(input('Digite as faces do dado, 4, 6, 8, 10, 12, 15, 20, 100: '))
    if faces not in tipos:
        print('Não e um número de faces valido')
        print(faces)
    else:
        val_faces = True
        break
        
repeat = int(input('Digite quantos dados a ser rolados: '))

while i <= repeat:
    num=random.randint(1,faces)
    total.append(num)
    i += 1
print(total)


