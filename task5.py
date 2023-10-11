import random

def RandomArray(x = int(input("Введіть найбільше число яке може бути в массиві "))):
    arr = []
    while( len(arr) != x):
        n = random.randint(1,x)
        if(arr.count(n) == 0):
            arr.append(n)
    return arr
print(RandomArray())        
 
    
