email = 'x@gmail.com'
password = 1234
if email == 'x@gmail.com' and password == 1234 :
    print('welcome')
elif email == 'x@gmail.com' and password != 1234 :
    print('invalid password')
elif  email != 'x@gmail.com' and password == 1234 :
    print('invalid email')
else:
    print('invalid email and password')
