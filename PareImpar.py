cont = 'n'
while cont != 's':
    def divisible(num1, num2):
            return num1 % num2 == 0
            

    def user_even():
        number = input("Digite um numero: ")
        int_number = int(number)
        if divisible(int_number,2):
            print("its even")
        else: 
            print("Its odd")

    user_even()
cont = input("Continuar? s ou n")
