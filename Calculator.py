class Calculator:
	@staticmethod
	def average(numbers: list) -> int:
		sum = 0
		for i in range(0, len(numbers)):
			sum += numbers[i]
		return sum / len(numbers)

	@staticmethod
	def weightedAverage(numbers: list):
		weights = []
		for i in range(0, len(numbers)):
			weights.append(numbers.count(numbers[i]))
		sum = 0
		for i in range(0, len(numbers)):
			sum += numbers[i] * weights[i]
		return sum / len(numbers)

	@staticmethod
	def normalMoment(numbers: list, power: int):
		sum = 0
		for i in range(0, len(numbers)):
			sum += numbers[i] ** power
		return sum / len(numbers)

	@staticmethod
	def centralMoment(numbers: list, power: int, average: int = None):
		sum = 0
		if average == None:
			average = Calculator.average(numbers)

		for i in range(0, len(numbers)):
			sum += (numbers[i] - average) ** power
		return sum / len(numbers)
