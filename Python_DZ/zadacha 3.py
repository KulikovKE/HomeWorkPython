#задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

#*Пример:*

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3


x = float(input('Введите точку по оси x: '))
y = float(input('Введите точку по оси y: '))

if x > 0 and y > 0:
    chetvert = 1
elif x < 0 and y > 0:
    chetvert = 2
elif x < 0 and y < 0:
    chetvert = 3
else:
    chetvert = 4
print(f'Точка находится в {chetvert} четверти плоскости')