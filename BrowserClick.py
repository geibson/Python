from selenium import webdriver
count = 1

browser = webdriver.Chrome()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
linkElem = browser.find_element_by_id('login-signin')
type(linkElem)
linkElem.click()
print('Nada ainda')
while count < 100:
    passwordElem = browser.find_element_by_id('login-passwd')
    passwordElem.send_keys('12345')
    passwordElem.submit()
    count += 1
    print(count)
print('Nada ainda')


##
##from selenium import webdriver
##browser = webdriver.Chrome()
##browser.get('http://inventwithpython.com')
##linkElem = browser.find_element_by_link_text('Donate')
##type(linkElem)
##linkElem.click() # follows the "Donate" link
##


