import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("password contain 3 special character")
        print("password contain 1 capital letter")
        print("password contain 6 lower letter")
        print("password contain 1 number")
        print("Strong Password Good to go")
        break
  
if flag ==-1:
    print("Not a Valid Password")
