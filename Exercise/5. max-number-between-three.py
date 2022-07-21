num1 = 10
num2 = 5
num3 = 2

if(num1 > num2):
    if(num1 > num3):
        print("num1 is maximum")
    else:
        print("num3 is maximum")

elif(num2 > num1): #or only else: instead of elif:
    if(num2 > num3):
        print("num2 is maximum")
    else:
        print("num3 is maximum")