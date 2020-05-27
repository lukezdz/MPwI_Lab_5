from Calculator import Calculator

if __name__ == "__main__":
	filename = "100liczb_modified.txt"

	numbersFile = open(filename)
	lines = numbersFile.readlines()
	numbers = []

	for line in lines:
		numbers.append(float(line.rstrip().replace(",", ".")))

	print()	
	print("Average: ")
	average = Calculator.average(numbers)
	print(average)

	print()
	print("Weighted average:")
	weightedAverage = Calculator.weightedAverage(numbers)
	print(weightedAverage)

	print()
	print("Normal moment:")
	normalMomentOne = Calculator.normalMoment(numbers, 1)
	normalMomentTwo = Calculator.normalMoment(numbers, 2)
	print('First: {0}, Second: {1}'.format(normalMomentOne, normalMomentTwo))

	print()
	print("Central moment:")
	centralMomentOne = Calculator.centralMoment(numbers, 1, average)
	centralMomentTwo = Calculator.centralMoment(numbers, 2, average)
	print('First: {0}, Second: {1}'.format(centralMomentOne, centralMomentTwo))
