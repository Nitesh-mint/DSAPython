import math
"""
Using stack to store the remainder. 
"""
from stack import Stack 

def DecimalToBinary(number: int):
    """
    A function that converts the given Decimal number to binary

    Args:
        number: The number that is need to be converted to binary.
    Return: The Decimal value of the number. 
    """
    try:
        if number > 0:
            stack = Stack()
            # divide gardai ouput rakhdai
            dividend = number
            
            # divide until the dividend is 2
            while dividend > 2:
                stack.push(math.floor(dividend % 2))
                dividend = dividend / 2
            stack.push(1)
            # finally add 1 to the stack as 2 is the dividend and 2 / 2 is 0 and remainder is 1.FIGURE is EASY TO Understand
            stack.printStack()
        else:
            raise ValueError("The number must be greater than 0")
    except ValueError as e:
        print(e)

DecimalToBinary(818)
