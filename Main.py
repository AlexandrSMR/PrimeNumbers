def initial_filling(file):
	file.close()
	file = open('PrimeNumbers.txt', 'w+')
	file.write('1\n2\n3\n5\n7\n')


JUMP_ARRAY = [0, 6, 4, 2, 4, 2, 4, 6]

primeNumbers = []

fileNumbers = open('PrimeNumbers.txt', 'r+')
for number in fileNumbers:
	primeNumbers.append(int(number))

if len(primeNumbers) < 5:
	initial_filling(fileNumbers)
	primeNumbers = [7]
else:
	primeNumbers.pop(0)
	primeNumbers.pop(0)
	primeNumbers.pop(0)
	primeNumbers.pop(0)

print(primeNumbers)

fileNumbers.write(str(7))

fileNumbers.close()
