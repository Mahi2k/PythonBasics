disp = print

#noOflines=int(input("Enter Number of lines: "))
#character=input("Enter character to print: ")

noOflines = 5
character = "*"
i=0
for i in range(0,noOflines+1):
    j=0
    for j in range(0,i): 
        disp(character,end=" ")
    disp()
    
disp("------------------")
for i in range(1,noOflines+1):
    for j in range(noOflines-i):
        disp(" ",end=" ")
    for k in range(2 * i -1):
        disp(character,end=" ")
    disp()


disp("------------------")

exit = "n"
matarPaneer = 330
methiMatar = 220
chickenTikka = 450
tax=15
sum=0
while (exit!="y"):
    disp("1. Matar Panner = 330")
    disp("2. Methi Matar Malai = 220")
    disp("3. Chiken Tikka = 450")
    item = int(input("Choose items to order?"))
    if(item == 1):
        sum = sum + 330
    if(item == 2):
        sum = sum + 220
    if(item == 3):
        sum = sum + 450
    exit = input("Exit y/n")

disp("Total bill",sum)