"""
Python 2.7.10

Euler Problem 7: 10001st Prime

What is the 10,001st prime number?
"""
from math import sqrt

def prime(n):
  number = 3 
  # all primes after 2 are odd, so starting with 3 allows us to step by 2
  # to step by two and only skip evaluating even numbers.
  prime_counter = 2 
  # 3 is the second prime (2, 3)
  while prime_counter < n:
    number += 2
    for num in xrange(2, int(sqrt(number)) + 1):
      if number % num == 0:
        break
    else:
      prime_counter += 1
      print number
  return number

# print prime(5)
# print prime(10)
print prime(10001)