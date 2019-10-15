def addValue(value, lst):
	lst.append(int(value))
	return lst


def prom(lista):
	addedValues = 0
	prom = 0
	for value in lista:
		addedValues = addedValues + value
	prom = addedValues / len(lista)
	return prom

def main():
	running = True
	while running:
		slst = []
		nValues = int(input("cuantos valores se van a promediar? "))
		for i in range(0, nValues):
			print("---------------------------")
			lst = addValue(input("valor " + str(i + 1) + " a promediar: "), lst)
			print("---------------------------")
		print(prom(lst))
		resp = 0
		while running == True:
			resp = input("seguir promediando? ")
			if resp == "si" or resp == "s" :
				running = True
				break
			elif resp == "no" or resp == "n" :
				running = False

main()