# Task: Given an integral number, determine if it's a square number. (7 kyu)
import math

def is_square(n):
    if n > -1:
        result = math.sqrt(n).is_integer()
        return result
    else: 
        return False    
