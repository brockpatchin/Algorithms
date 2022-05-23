# Coin Change gives an array cointaining the denominations of coins present and a numerical amount that needs to be made with the denominations provided. The goal is to minimize the amount of coins used (DP)
# The methodology for this question is to use a bottom up approach (common approach for DP questions where you create a recursive solution that solves for the entire problem and apply that from the bottom up)
# The recursive solution involves iterating through all of the coin denominations and solving (Opt(n) = Opt(n - denom value) + 1) where Opt(n) indicates the optimal value for n being the amount and the right 
# side of the equation involves finding the optimal value for the remaining n - denom value amount of money (for example, you need 25 cents and you use a nickel so the n - denom value would be 25 - 5 = 20).
# We add 1 because we added a coin (in the previous example, we added a nickel so our total number of coins increases by 1)

# Altogether, applying this approach bottom up achieves the optimal value. 


def coinChange(coins, amount):
    # if our amount is 0, just return 0 because we do not need to use any coins to achieve the requested amount
	if amount == 0:
		return 0
    # initialize our list for bottom up with the value of 0 (this is done to avoid index out of range errors if the amount = 1)
	values = [0]
    # iterate beginning at 1 to amount + 1 (bottom up)
	for i in range(1, amount + 1):
        # initalize temp to a large value so that we can properly find the minimum
		temp = 1000000
        # iterate through all of the denominations
		for z in coins:
            # if the amount - the denom value is greater than 0 (this means that we can use one of those coins) Example, if your amount is 5, you can not use a quarter
			if (i - z) >= 0:
                # this checks to make sure that no index out of range exceptions prop up
				if len(values) > i-z:
                    # if the value after we take out one of the coins is equivalent to -1 (this means we can't make this value) then don't change temp value
					if values[i-z] == -1:
						temp = temp
                    # else, apply recursive logic (Opt(n) = Opt(n - denom value) + 1)
					else:
						temp = min(temp, values[i - z] + 1)
        # Adds value of -1 if we can not make that value (one of the criterion for questions)
		if temp == 1000000:
			temp = -1
        # adds value to end of list (filling values with all of our previous values which follows the bottom up approach)
		values.append(temp)
    # returns the final value (this will be the top value since we are moving bottom up)
	return values[-1]

# Test Cases #
print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
# End of Test Cases #