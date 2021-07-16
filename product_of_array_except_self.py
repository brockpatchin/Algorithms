def productExceptSelf(nums):
        # Creates 3 lists, 2 of which are filled with len(nums) amount of 1's and the other is filled with 0's instead
        before = [1]*len(nums)
        after = [1]*len(nums)
        output = [0]*len(nums)
        
        # This places the numerical value of each product up to a certain point from the LEFT
        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        
        # This places the numerical value of each product up to a certain point from the RIGHT
        for a in range(len(nums) - 2, -1, -1):
            after[a] = after[a + 1] * nums[a + 1]
        
        # This places the values together
        for b in range(len(nums)):
            output[b] = after[b] * before[b]
        # This returns the output
        print(after)
        print(before)
        return output

# Testing #

print(productExceptSelf([1,2,3,4])) # Supposed to be [24, 12, 8, 6]