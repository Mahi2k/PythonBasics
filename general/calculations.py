show = print #for printing the output on terminal

firstnum = 45
secondNum = 90.56
thirdString = "vicky"

show("sum", firstnum + secondNum)
show("difference", firstnum - secondNum)
show("divide", firstnum / secondNum)
show("mod", firstnum % secondNum)

show("casting1", int(secondNum) + firstnum)
show("casting2", str(secondNum) + thirdString)
show("casting2", str(int(secondNum)) + thirdString)

#input sunction always takes it as a string
input1 = input("Enter first number:")
input2 = input("Enter second number:")

sum = input1 + input2
show("inputs sum:",sum)