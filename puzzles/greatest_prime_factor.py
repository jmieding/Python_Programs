"""
Python 2.7.10

Puzzle: Given a number, write a function to find the greatest prime factor
for that number.
"""

def greatest_prime_factor(number):
  range_minimized = number/2 
  """can't use sqrt, greatest prime factor can be > sqrt of number."""
  if range_minimized % 2 == 0:       
    range_minimized += 1 # allows program to count only odd numbers
  
  primes = [2, 3, 5, 7]
  for i in xrange(9, range_minimized + 1, 2):
    for prime in primes:
      if i % prime == 0:
        break
    else:
      primes.append(i)

  factors = []
  for prime in primes: # only counts odd numbers
    if number % prime == 0:
        factors.append(prime)
  if factors:
    return max(factors)
  else:
    print "no factors"

print greatest_prime_factor(25)
print greatest_prime_factor(99)
print greatest_prime_factor(58)
print greatest_prime_factor(54321)
print greatest_prime_factor(75143)
