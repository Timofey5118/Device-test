types = int(input("1 - low, 2 - medium, 3 - hard: "))

if types == 1:

	while True:	

		n = int(input("Вход: "))

		print("Формула: n**n**2")

		number = n**n**2

		colvo=(len(str(number)))

		print("Выход:",number)

		print("Кол-во символов:",colvo)

elif types == 2:

	while True:	

		n = int(input("Вход: "))

		print("Формула: n**n**4")

		number = n**n**4

		colvo=(len(str(number)))

		print("Выход:",number)

		print("Кол-во символов:",colvo)

elif types == 3:

	while True:	

		n = int(input("Вход: "))

		print("Формула: n**n**16")

		number = n**n**16

		colvo=(len(str(number)))

		print("Выход:",number)

		print("Кол-во символов:",colvo)
