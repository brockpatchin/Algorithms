def maxProduct(nums):
    
    # Initializes 3 variables (final, tempMin, tempMax) all to 0
    final = 0
    tempMin = 0
    tempMax = 0
    
    # handles the edge case of length being 1
    if len(nums) == 1:
        return nums[-1]
    
    # iterates through the entirety of the given array
    for i in nums:
        # holds the value for the previous tempMax
        temp = tempMax
        # sets the tempMax to the maximum of the current element, current element * tempMax, current element * tempMin
        tempMax = max(i, i * tempMax, i * tempMin)
        # sets the tempMin to the minimum of the current element, currenet element * tempMin, current element * previous tempMax
        tempMin = min(i, i * tempMin, i * temp)
        # final is max between tempMax and final
        final = max(final, tempMax)
    # returns answer
    return final

    # Extra Notes
    # Very similar to Kadane's, we just need to now take the negative values into account.
    # O(n) time, O(1) space

# Testing #

print(maxProduct([2,3,-2,4])) # should be 6
        
    