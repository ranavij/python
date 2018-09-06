import re as r

#Q1
email = input("enter the email that needs to be verified: ")
matcher = r.finditer('^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', email)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('given email is correct')
else:
    print('email is not correct')


#Q2

pno = input('enter the phone number as "country code" followed by "-" and then the "phone number": ')
matcher = r.finditer('^[+][9][1][-][6-9][\d]{9}', pno)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('phone number is AN INDIAN PHONE NUMBER')
else:
    print('phone number is NOT AN INDIAN PHONE NUMBER')

