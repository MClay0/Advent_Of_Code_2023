FILE = open('input.txt','r')
lines = FILE.readlines()

calValues = []      #Array to store each lines calibration value

sum = 0
for line in lines:
    chars = [char for char in line]
    firstNum = -1
    secondNum = -1
    for char in chars:
        if char.isdigit() and (firstNum == -1):
            firstNum = int(char)
        elif(char.isdigit()):
            secondNum = int(char)
    if(firstNum == -1 and secondNum == -1):
        calValues.append(0)
    elif(firstNum != -1 and secondNum != -1):
        calValues.append(int(str(firstNum) + str(secondNum)))
    elif(firstNum != -1 and secondNum == -1):
        calValues.append(int(str(firstNum)+str(firstNum)))
        
for val in calValues:
    sum += val
     
print("Sum is " + str(sum))  #53921

