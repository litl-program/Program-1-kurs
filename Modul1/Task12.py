#------====================Задача 12 (2/10)#======================------
#Пирожок в столовой стоит A рублей и B копеек. Определите, #сколько рублей и копеек нужно заплатить за N пирожков.
#>*Программа получает на вход три числа: A, B, N — целые, #неотрицательные, не превышают 10000.
A = int(input("Рублі--)"))
B = int(input("Копійки--)"))
N = int(input("Кількість пиріжків--)"))
chek =N * (A + (B / 100))
if chek > 10000:
	print("Убав апетит")
else:
	print("Загальна вартість", float(chek))	
