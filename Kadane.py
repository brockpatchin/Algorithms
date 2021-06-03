#Meant for finding max subarray value

def max_sub_array(nums):

	#initializes the values of the output max and the pointer to the current max to nums[0]
	output = nums[0]
	cMax = nums[0]

	#iterates through the entirety of the list starting at the 2nd element
	for i in range(1, len(nums)):

		#sets the current max to the larger of the active element and the old current max + the active element
		cMax = max(nums[i], cMax + nums[i])

		#sets the output max to the larger of the current max and the original output max
		output = max(output, cMax)

	#returns the final max
	return output

## TESTING ##

a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1]
c = [5,4,-1,7,8]

print(max_sub_array(a))
print(max_sub_array(b))
print(max_sub_array(c))




