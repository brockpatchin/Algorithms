
#Meant to find all subsequences length 3 of an array in which the sum of the subseqeucne is 0
def three_sum(nums):

    #sorts the array
    nums.sort()
    #initializes the length of the array to N and the output to an empty list
    N, output = len(nums), []

    #iterates through length of array
    for i in range(N):
        #conditional to check that the current element is equal to the next element. 
        # If this is true, we continue
        if nums[i] == nums[i-1]:
            continue
        #sets target value to the negative value of the current element
        target = nums[i]*-1
        #initializes 2 variables (s and e) to the values of currentindex++ and last index respectively
        s,e = i+1, N-1
        #from here, we iterate through as long as s is less than e
        while s < e:
            # we check to see if we have hit our target or not
            if nums[s]+nums[e] == target:
                #if we have, we put this subsequence of 3 into the array
                output.append([nums[i], nums[s], nums[e]])
                #we also increment the value of s
                s = s+1
                # we continue to increase the value of s as long as the element at s is equivalent to the element before it.
                while s<e and nums[s] == nums[s-1]:
                    s = s+1
            #if the above conditional is not meant, we continue to check new values of s
            elif nums[s] + nums[e] < target:
                s = s+1
            #if neither of those worked, we start to change the values of e
            else:
                e = e-1
    return output

#Testing#

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([]))
print(three_sum([0]))

