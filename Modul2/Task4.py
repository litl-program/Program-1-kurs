#------=====================Задача 4 (6/10)=======================------
#Шахматный король ходит по горизонтали, вертикали и диагонали, но только на #1 клетку. Даны две различные клетки шахматной доски, определите, может ли #король попасть с первой клетки на вторую одним ходом.
#
#Формат ввода
#Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер #столбца и номер строки сначала для первой клетки, потом для второй клетки.
#
#Формат вывода
#Программа должна вывести YES, если из первой клетки ходом короля можно #попасть во вторую или NO в противном случае.

x1=int(input('Введіть число 1:'))
x2=int(input('Введіть число 2:'))
x3=int(input('Введіть число 3:'))
x4=int(input('Введіть число 4:'))

if x1 == x3+1 or x1 == x3-1 or x1 == x3:
  if x2 == x4+1 or x2 == x4-1 or x2 == x4:
	  print("Yes")
  else:
    print("No")	