def maxProfit(prices):
    # initalizes the variables (cMax, oMax, length) all to their values. cMax stands for current max and oMax stands for output max
    cMax = 0
    oMax = 0
    length = len(prices)
    
    # iterates through the list starting at index 1
    for i in range(1, length):
        # utilizes Kadanes
        # checks to see which is larger, 0 or cMax + difference between selling the day after buying
        cMax = max(0, cMax - prices[i - 1] + prices[i])
        # checks to see which is larger, oMax or cMax
        oMax = max(cMax, oMax)
    # returns the answer
    return oMax

    # simple implentation of Kadane's with some different logic. Look at maximum subarray to see a similar solution    