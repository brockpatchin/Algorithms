def pickingNumbers(a):
	
	#sorts the inputted array
	a.sort()

	#initializes the variable output
	output = 0

	#iterates through the array all the way to the 2nd to the last element
	for i in range(len(a) - 1):
		#initializes the variable start to the value of i for each iteration in the for loop
		start = i
		#initializes the variable tempMax which will be used to check each subarrays output
		tempMax = 0
		#checks to see if the first 2 elements in the subarray in question meet the initial condition
		if abs(a[start] - a[start + 1]) <= 1:
			#if so, minHold and maxHold are both initialized
			minHold = min(a[start], a[start + 1])
			maxHold = max(a[start], a[start + 1])
			#tempMax also increases value by 2 as we now have 2 elements in our subarray
			tempMax += 2
			#initializes a checker variable to True
			x = True
			#while this variable stays true and the start pointer does not reach the end of the list
			while x == True and start != len(a) - 2:
				#start increments value by one
				start += 1
				#this new element is checked to see if it can be put in the array
				if abs(a[start + 1] - minHold) <= 1 and abs(a[start + 1] - maxHold) <= 1:
					#if so, the length increase
					tempMax += 1 
				#if not, the checker variable becomes false
				else:
					x = False

		#the ending value of tempMax is checked to see if it is a newMax and if it is, the output is changed to that value
		if tempMax > output:
			output = tempMax

	#the program ends with returning the maximum of all of the subarray sizes
	return output

# Complexities #
# Time Complexity is O(n) + (time complexity from while loop which changes) so we will say O(n/2)
# Space Complexity is O(1) I think

print(pickingNumbers([4, 6, 5, 3, 3, 1]))