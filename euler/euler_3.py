"""
Python 2.7.10

Euler Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Note: The program takes a Looooooong time to execute.

def greatest_prime_factor(number):

  range_minimized = (number / 2) + 1

  primes = [2, 3, 5, 7] # all other non-primes can be divided by these
  for i in xrange(9, range_minimized, 2):
    for prime in primes:
      if i % prime == 0:
        break
    else:
      primes.append(i)

  factor = None
  for prime in primes:
    if number % prime == 0:
      factor = prime
  if factor:
    return factor
  else:
    return number, "is a prime number!"


# print greatest_prime_factor(25)
# print greatest_prime_factor(99)
# print greatest_prime_factor(58)
# print greatest_prime_factor(54321)
# print greatest_prime_factor(600851475143)