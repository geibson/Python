'''


*********************
*                   *
*                   *
*                   *
*                   *
*                   *
*                   *
*********************


'''

def boxPrint(symbol,width,heigth):
    if len(symbol) !=1:
        raise Exception('"symbol" precisa ter tamamanho 1')

    print (str(symbol) + str(width))

    for i in range(height - 2):
        print(str(symbol) + (' ' * str(width - 2)+ str(symbol))
              
    print (str(symbol) * str(width))

boxPrint('*',15,5)
boxPrint('O',10,20)
