def pickingNumbers(a):
	a.sort()
	output = 0

	for i in range(len(a) - 1):
		start = i
		tempMax = 0
		if abs(a[start] - a[start + 1]) <= 1:
			minHold = min(a[start], a[start + 1])
			maxHold = max(a[start], a[start + 1])
			tempMax += 2
			x = True
			while x == True and start != len(a) - 2:
				start += 1
				if abs(a[start + 1] - minHold) <= 1 and abs(a[start + 1] - maxHold) <= 1:
					tempMax += 1 
				else:
					x = False

		if tempMax > output:
			output = tempMax

	return output


print(pickingNumbers([4, 6, 5, 3, 3, 1]))