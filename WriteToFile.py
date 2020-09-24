import pyperclip
id = 434180
user = 1



new_file=open("C:\\Users\\geibsonl\\Documents\\Test\\email.txt",mode="w",encoding="utf-8")
while user <= 9 :
    
    
    phone = ('415-555-000'+(str(user)))
    new_file.write(phone)
    new_file.write('\n')
    
    email = ('teste'+str(user)+'@mail.com')
    new_file.write(email)
    new_file.write('\n')

    user = user+1
    print(str(user))
    
new_file.close()

file = open("C:\\Users\\geibsonl\\Documents\\Test\\email.txt")
info = file.readlines()
pyperclip.copy(str(info))
