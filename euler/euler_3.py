"""
Python 2.7.10

Euler Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

primes = [2]

def is_prime(factor):
  print "factor is {}" .format(factor)
  for i in xrange(3, (factor / 2) + 1, 2):
    for prime in primes:
      if i % prime == 0:
        return False
    else:
      primes.append(i)
  return True

def greatest_prime_factor(number):
# get all factors >= 10000
  factors = []
  count = 2
  while number/count >= 10000:
    if number % count == 0:
      factors.append(number/count)
    count += 1
  print factors

# check factors for primes
  for factor in factors:
    if is_prime(factor) == True:
      return factor
  else:
# generate primes < 10000
    print "No prime factors greater than 10000"
    for i in xrange(3, 10000, 2):
      for prime in primes:
        if i % prime == 0:
          break
      else:
        primes.append(i)
# check primes for factors:
    for prime in primes[::-1]:
      if number % prime == 0:
        return prime


# print greatest_prime_factor(25)
# print greatest_prime_factor(99)
# print greatest_prime_factor(58)
# print greatest_prime_factor(54321)
print greatest_prime_factor(600851475143)