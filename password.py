password.py

import re
p= input("Input your password :")
p2 = input("Input your password again :")
x = True

while p != p2:
    print("The passwords don't match up.")
    password = input("Please enter your new password: ")
    password2 = input("Please enter your new password again: ")
    break

while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@!]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("This is a strong Password")
        x=False
        break

if x:
    print("your password must contain a lowercase,uppercase,number and either $#@!")