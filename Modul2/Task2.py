#------=====================Задача 2 (2/10)=======================------
#Даны три целых числа. Найдите наибольшее из них (программа должна вывести #ровно одно целое число).
#
#Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для #решения этой задачи?

x1=int(input('Введіть число 1:'))
x2=int(input('Введіть число 2:'))
x3=int(input('Введіть число 3:'))
if x1 > x2 and x1 > x3:
  print(x1)
elif x2 > x1 and x2 > x3:
  print(x2)
else:
  print(x3)	