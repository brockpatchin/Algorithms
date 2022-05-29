# Point of Question is to check if a string containing only -- '(', ')', '[', ']', '{', and '}' -- has only valid parentheses
# Complexities:
# Time = O(n) -- iterates through entire string only once in which for loop is filled with primitive operations
# Space = O(n) -- usage of Stack


def isValid(s):
    # initalizes Stack
    Stack = []
    # begins iteration through string
    for n in s:
        # if the character is an opeining parntheses, bracket, curly brace
        if n == '(' or n == '{' or n == '[':
            # add it to the stack
            Stack.append(n)
        # if not
        else:
            # check to make sure that there are characters currently on the stack (if not, we are adding a closing symbol first therefore we automatically know it is not valid)
            if len(Stack) == 0:
                return False
            # characters are on the stack
            else:
                # utilizes ascii values to check to see if it is a closing version of the symbol
                if abs(ord(n) - ord(Stack[-1])) > 3:
                    # if it is not valid, return False
                    return False
                # else
                else:
                    # remove the symbol that we just matched up off the top of the stack
                    Stack.pop()
    # after iteration is completed, we need the stack to be empty for the string to be considered valid
    if len(Stack) == 0:
        return True
    else:
        return False

# Test Cases #
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
# End of Test Cases #