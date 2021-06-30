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


# Altogether, Kadanes is a DP algorithm that takes advantage of the logic surrounding subarrays.
# Assume that we have the array [5, 4, -1, 7, 8]
# We start both the cMax and output at the first element (5). This is because this is the first possible subarray and is the max so far
# We then compare the set cMax to either the second element or the combination of the first and the second element. This is seen on the 13th line. 
# This is done because if the first element was negative, there is no benefit in starting the subarray sum there. 
# This logic is applied throughout and is how the actual max sub array is found. 


