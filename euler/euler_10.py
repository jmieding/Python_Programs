"""
Python 2.7.10

Euler Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def summation_of_primes():
  primes_to_two_million = [x for x in xrange(3, 2000001, 2) if x % 3 != 0 and x % 5 != 0 and x % 7 !=0]
  final_sum = sum(primes_to_two_million)
  return final_sum

print summation_of_primes()