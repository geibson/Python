#Python3

import re, pyperclip


#TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415)555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d)|(\(\d\d\)))?    #Area code(optional)
(\s|-)                      #First separator
\d\d\d                      #First 3 digits
-                           #Separator
\d\d\d\d                    #last 4 digits
((ext(\.)?\s|x))            #Extension 
(\d{2,5})?                  #extension number
''',re.VERBOSE)

#TODO: Create a regex for email adress
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+     #name part
@                   #@ symbol
[a-zA-Z0-9_.+]+     #domain name part

''',re.VERBOSE) 


#TODO: Get the text from clipboard
text = pyperclip.paste()

#TODO: extract emial or phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for honeNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(allPhoneNumbers)
#print(extractedEmail)
#TODO: Copy the extracted info to the clipboard
results = '\n'.join(allPhoneNumbers) +'\n'+ '\n'.join(extractedEmail)
pyperclip.copy(results)
