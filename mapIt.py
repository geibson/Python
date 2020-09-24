import webbrowser, sys, pyperclip

sys.argv #['mapIt.py','2080','Ary Tarrago', 'Avenida']
#address = ''

# check if command line arguments are passed
if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)

