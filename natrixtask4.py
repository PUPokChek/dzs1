import numpy as np
from random import randint
on =[1,-1]
n = int(input('Введите число n > 2 = '))
if n<=2:n = 0;
if n<2:print ('Error, please write n > 2')
mas = np.ones((n,n))
for i in range(n):
    for j in range(n):
        mas[j,i] = on[randint(0,1)]
    print(mas)
sum = 0 
for j in range(n):
    for k in range(n):
        if(j-1)>= 0:
            sum += mas[j,k] * mas[j-1,k]
    for j in range(n):
        if(k-1)>= 0:
            sum += mas[j,k] * mas[j,k-1]
sum
