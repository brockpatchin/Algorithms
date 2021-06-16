def addBinary(a, b):

    #Inititalzing a bunch of stuff (the list that is then converted into the string output (s), the output string, the carry variable, the length)
    s = []
    output = ""
    carry = 0

    ph = len(a) - len(b)
    if ph < 0:
        ph *= -1

    new = ""

    if ph != 0:
        for i in range(ph):
            new += "0"

        if len(a) < len(b):
            new += a
            a = new
        else:
            new += b
            b = new

        print(a)
        print(b)

    length = len(a) #or length b since they are now the same


    #for loop that goes backwards
    for i in range(length):

        #If the lengths between the 2 binary values, we just assign the value of each of the digits normally. 
        print("This is the value of a: " + str(a))    
        print("This is the value of a: " + str(b))
        tempA = int(a[length - i - 1])
        print(tempA)
        tempB = int(b[length - i - 1])
        print(tempB)

        #initializes the sum that we will be obtaining for each digit sum to the sum of the 2 digits plus the carry (basic addition)
        sum = tempA + tempB + carry 

        #this checks to see if there is a carry or not (this specific conditional is the case where there is no carry)
        if sum == 1 or sum == 0:
            s.insert(0, str(sum))
            print(str(length - i - 1) + " " + str(sum) + " sum is not greater than 1")
            carry = 0
        else:
            s.insert(0, str(sum % 2))
            print(str(length - i - 1) + " " + str(sum) + " sum is greater than 1")
            carry = 1
    if carry == 1:
        s.insert(0, 1)
    for z in s:
            output += str(z)
    return output




print(addBinary('1', '111'))
