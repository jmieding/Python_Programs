"""
Python 2.7.10

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest Palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product():
  largest = 0
  for num1 in xrange(999, 0, -1):
    for num2 in xrange(999, 0, -1):
      if str(num1 * num2) == str(num1 * num2)[::-1] and num1 * num2 > largest:
          largest = num1 * num2
  return largest

print largest_palindrome_product()