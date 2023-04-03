import numpy as np

# Defining the functions that calls the result numbers informations
def evenOdd(calc):
    if calc % 2 == 0:
        return "\n this is an even number."
    else:
        return "\n this is an odd number."

def isPrime(x):
    if x < 2:
        return "\n this is a composite number."
    elif x == 2:
        return "\n this is a prime number."  
    for n in np.arange(2, x):
        if x % n == 0:
            return "\n this is a composite number."
    return "\n this is a prime number."

def divisible(x):
    divisors = []
    for nums in np.arange(1, 501):
        if x % nums == 0:
            divisors.append(nums)
        
    return f"\ndivisible by {divisors}"