def intToRoman(num):
    romanDict = [
                [1000, 'M'], 
                [900, 'CM'], 
                [500, 'D'], 
                [400, 'CD'], 
                [100, 'C'], 
                [90, 'XC'], 
                [50, 'L'], 
                [40, 'XL'], 
                [10, 'X'], 
                [9, 'IX'], 
                [5, 'V'], 
                [4, 'IV'], 
                [1, 'I']
        ]
        counter = 0
        
        output = ''
        
        while num != 0:
            if (num >= romanDict[counter][0]):
                while(num >= romanDict[counter][0]):
                    num -= romanDict[counter][0]
                    output += romanDict[counter][1]
                
            counter += 1
                
        return output