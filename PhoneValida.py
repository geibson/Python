re.compile('''
(\d\d\d-)  #area code
(\(\d\d\d\) )       # slash
\d\d\d  #
-
\d\d\d\d    #last 4 digits
\sx\d{2,4} # extension''',re.IGNORECASE|re.DOTALL|re.VERBOSE)


import re

message = 'call me 415-555-1011 tomorrow, or at 514-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))

##mo = phoneNumRegex.search(message)
##print(mo.group())



##def isPhoneNumber(text):
##    if len(text) != 12:
##        return False
##    for i in range(0,3):
##        if not(text[i].isdecimal()):
##            return False
##        if text[3] != '-':
##            return False
##    for i in range(4,7):
##        return False
##        if text[7] != '-':
##            return False
##    for i in range(8,12):
##        if not text[i].isdecimal():
##            return False
####print(isPhoneNumber(str(425-555-1011)))
##
##
##message = 'call me 415-555-1011 tomorrow, or at 514-555-9999'
##
##foundNumber = False
##for i in range(len(message)):
##    chunk = message[i:i+12]
##    if isPhoneNumber(chunk):
##        print('Phone number found '+chunk)
##        foundNumber = True
##if not foundNumber:
##    print('Could not found a phone number')
