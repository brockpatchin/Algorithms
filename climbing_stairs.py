def climb_stairs(n):
	
	#initializes the first 2 elements of the fibonacci sequence
	fibArray = [1, 1]
        
    # ensures that there are no out of bounds exceptions
    if n == 1:
        return 1
    else:
    	#iterates all the way up to n
        for i in range(n):
        	#adds each fibo number all the way up to n, to the fibo array
            fibArray.append(fibArray[i] + fibArray[i+1])
            
    #when the iteration has concluded, this returns the fibo number in question
    return fibArray[len(fibArray) - 2]


    #Notes#

    #Altogether, this algorithm should have time complexity and space complexity of O(N) due to the fact that the algorithm iterates through the entirety of n
    #and also fills the fiboArray with n elements

  	#The algorithm can be more optimized using some other methods to get a time complexity of O(log(n)), but this method was the one that I could come up with
  	
