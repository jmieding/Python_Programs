"""
Python 2.7.10

Euler Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_3_and_5():
  total = 0
  for num in xrange(1000):
    if num % 3 == 0 or num % 5 == 0:
      total += num
  return total

print sum_multiples_3_and_5()