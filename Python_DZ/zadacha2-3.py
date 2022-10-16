'''Задача 3. Реализуйте алгоритм перемешивания списка. 
Список размерностью 10 задается случайными целыми числами, 
выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
'''

n = int(input('Введите число N ')) 

import random
spisokRandom=[]
listResult=[]

for i in range(n):
    spisokRandom.append(random.randint(-100,100))
print(spisokRandom)

listResult = sorted(spisokRandom, key=lambda A: random.random())
print(listResult)

