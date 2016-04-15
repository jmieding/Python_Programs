"""
Python 2.7.10

Euler Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
primes = [2]
total_sum = 2

def is_a_prime(num):
  for i in primes:
    if i > int(num/2):
      primes.append(num)
      return True
    if num % i == 0: 
      return False

for x in xrange(3, 2000000, 2):
  if is_a_prime(x):
    total_sum += x

print total_sum