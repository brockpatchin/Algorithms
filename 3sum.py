def threeSum(nums):

    # initalizes 2 variables (length and result) in which length is the length of the array and result is the list that will eventually be outputted.
    length = len(nums)
    result = []

    # if the length is less than 3, there is obviously not a sum of 3 numbers in the array that add up to 0 so return empty array.
    if length < 3:
        return result
    # sort array
    nums.sort()
    # iterate length times
    for i in range(length):
        # remvoes duplicate edge cases (since array is sorted, values that are equal will be next to each other so this removes the possibilty of duplicates)
        if i != 0 and nums[i] == nums[i-1]:
            continue
        # initializes variable named target to the negative of our current value (this will give us the value needed to sum to 0 since nums[i] + (-nums[i]) = 0)
        target = nums[i]*-1
        # creates 2 pointers (l and r standing for left and right) to have a start and end point to iterate through
        l, r = i+1, length-1
        # while left is still left and right is still right
        while l<r:
            # if we have our target
            if nums[l]+nums[r] == target:
                # append the 3 value to the result
                result.append([nums[i], nums[l], nums[r]])
                # increase left by 1
                l += 1
                # removes possible duplicates (similar logic as above)
                while l<r and nums[l] == nums[l-1]:
                    # continues to move forward through all duplicates
                    l = l+1
            # if our sum is less than target (move left closer increasing sum since list is sorted)
            elif nums[l] + nums[r] < target:
                l = l+1
            # else, move right closer to the middle (moving right to the left decreases sum)
            else:
                r = r-1
    # returns result
    return result 

# Testing #

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([]))
print(threeSum([0]))
