"""
Python 2.7.10

Euler Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1-10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1-20?
"""

def smallest_multiple():
  x = 0
  final = 0
  while x < 10:
    x = 0
    final += 20 
    """
    Count by the largest possible number to minimize times the
    loop needs to execute.
    """
    for num in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
      """
        Any number that is evenly divisible by 20, will also be evenly divisible
        by 1, 2, 4, 5, & 10. 18: divisible by 3, 6, & 9. 16 & 14 are 
        divisble by 8 & 7 respectively.

        Using xrange()/range() is more conventional, but the hard coded tuple
        saves about 5 seconds on execution time.
      """
      if final % num == 0:
        x += 1
  return final

print smallest_multiple()