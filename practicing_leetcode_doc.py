def maxProfit(prices):
	output = 0
	cMax = 0
	length = len(prices)
		
		
	for i in range(1, length):
		cMax = max(0, cMax + prices[i] - prices[i - 1])
		output = max(cMax, output)

		print('###########')
		print(i)
		print(cMax)
		print(output)
		print('###########')

				
	return output
			

# Testing #

print(maxProfit([7,1,5,3,6,4])) # should be 5
