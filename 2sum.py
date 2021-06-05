# Find a subsequence of length 2 in an array in which the sum of the subsequence is equal to the target

def twoSum(nums, target):
        
        #Initializes an empty dictionary
        dictionary = {}
        
        #iterates through the entirety of the array
        for i in range(len(nums)):
            #sets the second number to the target - the current element (a + b = c  ===  c - a = b)
            j = target - nums[i]
            #conditional to check if j is in the dictionary already
            if(j in dictionary.keys()):
                #if it is we set a variable to the index value of the current element
                jIndex = nums.index(j)
                #we then check to see if the current index is equal to the other number's index
                if(i != jIndex):
                    #if it isn't, we return the answer! 
                    return [i, jIndex]
            #we update the dictionary with the value of the current index's value and the index itself    
            dictionary.update({nums[i]: i})

# Testing #

print(twoSum([2,7,11,15], 9))
                    