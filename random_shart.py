def search(nums, target):
    length = len(nums)
    if nums[length - 1] == target:
        return length - 1
    if nums[0] == target:
        return 0
    
    
    lp = 0
    rp = length - 1
    
    while lp <= rp or abs(rp - lp) == 2:
        mp = int(lp + (rp - lp) / 2)
        
        if nums[mp + 1] == target:
            return mp + 1
        if nums[mp] == target:
            return mp
        
        if nums[lp] < target:
            lp = mp + 1
        else:
            rp = mp + 1

        print(lp, rp)
    return -1

search([4,5,6,7,0,1,2], 3)

