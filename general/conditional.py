show = print

#Calculator as an example taking operations to be done from user

num1 = 30
num2 = 20

if num1 > num2:
    show(False)
else:
    show(True)
    
show("Check:", num2>num1)

choice = input('your choice Y/N: ')
if (choice == 'Y'):
    show(True)
elif (choice == '5'):
    show("Wrong")
else:
    show(False)
    
'''
# Number of operators
+, -, *, /
|, ==, 
'''