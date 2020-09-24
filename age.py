##__author__ = 'jslvtr'
##__Modified__ = 'Geibson'


age = input("Enter age: ")
calc = input('Selecione Segundos, Dias ou Meses:').lower()
user_age = float(age)

def age_program_sec():    
    age_seconds = float(user_age) * 365 * 24 * 60 * 60
    print("Your age in seconds is {}".format(age_seconds))

def age_program_days():    
    age_days = float(user_age) * 365 
    print("Your age in days is {}".format(age_days))

def age_program_months():    
    age_months = float(user_age) *12 
    print("Your age in months is {}".format(age_months)) 


if calc == 's':
    age_program_sec()
elif calc == 'd':
    age_program_days()
elif calc == 'm':
    age_program_months()
else:
    print('O q?!?!?!?!?!') 

