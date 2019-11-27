from random import randint
n = int(input("Please choose the array size: "))

Array = [0] * n
print(Array)
for i in range(0,n):
    x = randint(0,n)
    Array[i] = x

print(Array)
