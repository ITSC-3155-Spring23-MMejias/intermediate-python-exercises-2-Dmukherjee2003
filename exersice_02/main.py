import time as t
def fibbonacci(num):
    if num == 0: 
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibbonacci(num -1) + fibbonacci(num -2)
   


print(fibbonacci(34))
#print(t.)