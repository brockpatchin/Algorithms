#Meant for finding max subarray value

def max_sub_array(nums):

	#initializes the values of the output max and the pointer to the current max to nums[0]
	cMax, output = nums[0]
	

	#iterates through the entirety of the list starting at the 2nd element
	for i in range(1, len(nums)):

		#sets the current max to the larger of the active element and the old current max + the active element
		cMax = max(nums[i], cMax + nums[i])

		#sets the output max to the larger of the current max and the original output max
		output = max(output, cMax)

	#returns the final max
	return output

#Testing#

a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1]
c = [5,4,-1,7,8]

print(max_sub_array(a))
print(max_sub_array(b))
print(max_sub_array(c))


# Logic behind the algorithm
# The first thing that is done is the current max and the eventual output are set to the first value in the list
# From here, we iterate through the entirety of the list starting at the second element in which 2 things are checked for.
# The first thing that is checked is what is the maximum value between the current element (nums[i]) and the current max + nums[i] (current element in the list)
# This is done to find the largest sum of all of the possible contiguos subarrays. 
# From here, the output is changed to be the output between the current max and the original max
# After this completes, the remaining value held in the variable "output" is the largest sum in the array


