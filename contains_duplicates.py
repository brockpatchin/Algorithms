def containsDuplicate(nums):
    
    # Initializes a set named s
    s = set()
    
    # iterates through the entirety of the provided list
    for i in range(len(nums)):
        # checks to see if a number is in s
        if nums[i] in s:
            # if it is, return True because this means that there is a duplicate
            return True
        # adds the element if the above condition is not true
        s.add(nums[i])
    # returns false if the return true conditional was not triggered during the entirety of the loop
    return False


# Altogether, this question is pretty much exactly like 2 sum. 

