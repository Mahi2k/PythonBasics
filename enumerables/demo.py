prt = print

#enumerables examples
list = [1,32,5,72,9,"vicky",True]
tuple = (1,2,3,4,5)
set = {1,2,3,4,5,3}
dictionary = {
    1:"value",
    "key1":5,
    2:"hello there"
}

# for i in range(len(list)):
#     if(i%2 == 0):
#         prt(list[i])

#prt(list,tuple,set,dictionary)

# prt(len(set),set);

def getEvenValues(numberList):
    returnList = []
    for i in range(len(numberList)):
        if (int(numberList[i])%2==0):
            returnList.append(int(numberList[i]))
    return returnList

num=input("Enter numbers seperated by space: ") # Ask user to input the numbers 

if (len(num) < 1): # if input is not given then take default values
    num = "99 88 66 45 3393 92 2 10 66"
numberList = num.split()

myList = getEvenValues(numberList)
prt("Final output: ", myList)