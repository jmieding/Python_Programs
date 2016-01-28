"""
Python 2.7.10

Euler Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from itertools import combinations, ifilter

def pythagorean_triplet():
  sums = list(combinations(xrange(3, 500), 3))
  sums_1000 = ifilter(lambda combo: combo[0] + combo[1] + combo[2] == 1000, sums)
  triplet = (0, 0, 0)
  for combo in sums_1000:
    if combo[0]**2 + combo[1]**2 == combo[2]**2:
      triplet = combo
      break
  triplet_product = triplet[0] * triplet[1] * triplet[2]
  return triplet, triplet_product
      
print pythagorean_triplet()
