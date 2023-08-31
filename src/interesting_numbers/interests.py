from interesting_numbers.interesting_number import InterestingNumber
import math
import sympy
from itertools import product
import json
import os

#TODO: vampire numbers, search for numbers which make english words

#some utility functions

#https://stackoverflow.com/a/50992575/13870347
def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def digit_to_char(digit):
    assert digit < 37, "base must be between 2 and 37"
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def digits_to_string(digits):
    return "".join([digit_to_char(digit) for digit in digits])

def get_divisors(number):
    prime_factors = sympy.factorint(number)
    #loop over all combinations
    primes = list(prime_factors.keys())
    exponents = [range(prime_factors[prime]+1) for prime in prime_factors]
    divisors = []
    for exponent_signature in product(*exponents):
        divisor = 1
        for i, exponent in enumerate(exponent_signature):
            divisor *= primes[i]**exponent
        divisors.append(divisor)
    return divisors

# def load_words():
#     with open("words_dictionary.json", "r") as file:
#         words = json.load(file)
#     return words


PROJECT_DIR = os.path.dirname(__file__)

def load_words(): #load from words_10k.txt, one line per word
    with open(os.path.join(PROJECT_DIR, 'words_10k.txt'), "r") as file:
        words = file.read().splitlines()
    return words

WORDS = load_words()

# a set of functions to determine whether a number has some interesting property. If so, it returns an appropriate InterestingNumber object.

def is_prime(number):
    if sympy.isprime(number):
        return InterestingNumber(number, str(number), "prime")
    else:
        return None
    
def is_nth_power(number,n):
    root = number**(1/n)
    if root.is_integer():
        return InterestingNumber(number, f"{number} ({int(root)}^{n})", "square")
    else:
        return None
    
def is_square(number):
    return is_nth_power(number,2)

def is_cube(number):
    return is_nth_power(number,3)

def is_triangular(number):
    root = (math.sqrt(8*number+1)-1)/2
    if root.is_integer():
        return InterestingNumber(number, f"{number} ({make_ordinal(int(root))} triangular number)", "triangular")
    else:
        return None
    
def is_fibonacci(number):
    root1 = (math.sqrt(5*number**2+4))
    root2 = (math.sqrt(5*number**2-4))
    if root1.is_integer() or root2.is_integer():
        return InterestingNumber(number, f"{number} (Fibonacci number)", "Fibonacci")
    else:
        return None
    
def is_palindrome(number, base):
    digits = number_to_base(number, base)
    if digits == digits[::-1]:
        return InterestingNumber(number, f"{digits_to_string(digits)} (base {base})", "palindrome", base)
    else:
        return None
    
def is_repdigit(number, base):
    digits = number_to_base(number, base)
    if len(set(digits)) == 1:
        return InterestingNumber(number, f"{digits_to_string(digits)} (base {base})", f"repdigit {digit_to_char(digits[0])}", base)
    else:
        return None
    
def is_consecutive(number, base):
    digits = number_to_base(number, base)
    if digits == list(range(min(digits), max(digits)+1)) or digits == list(range(max(digits), min(digits)-1, -1)):
        return InterestingNumber(number, f"{digits_to_string(digits)} (base {base})", "straight", base)
    else:
        return None
    
def is_perfect_power(number, base):
    assert base >= 2, "base must be at least 2"
    assert number >= 1, "number must be at least 1"
    root = math.log(number,base)
    if root.is_integer():
        return InterestingNumber(number, f"{number} ({base}^{int(root)})", "power of {base}")
    else:
        return None

def is_power_of_two(number):
    return is_perfect_power(number, 2)
    
def is_perfect(number):
    divisors = get_divisors(number)
    if sum(divisors) == 2*number:
        return InterestingNumber(number, f"{number} (perfect number)", "perfect")
    else:
        return None
    
def is_word(number, base):
    digits = number_to_base(number, base)
    #check if any digits are above 36
    if max(digits) > 36:
        return None
    digit_string = digits_to_string(digits)
    word = digit_string.lower().replace("0","o").replace("1","i").replace("5","s")
    if word in WORDS:
        return InterestingNumber(number, f"{digit_string} (base {base})", f"{word}", base)
    else:
        return None