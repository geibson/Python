i = 0
 
new_file=open("C:\\Users\\geibsonl\\Documents\\Test\\sql2.txt",mode="w",encoding="utf-8")

my_file=open("C:\\Users\\geibsonl\\Documents\\Test\\Conexoes.xml","r")
for line in my_file:
    new_file.write(line)


    ##print(line)
my_file.close()
new_file.close()
