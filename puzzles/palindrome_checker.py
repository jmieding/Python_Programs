"""
Python 2.7.10

Puzzle: Given a string as an argument, write a function that returns
True if the string is palindrome, and False otherwise.
"""
from itertools import permutations

def palindrome_checker(word):
  all_combos_of_word = permutations(word, len(word))
  for combo in all_combos_of_word:
    if combo == combo[::-1]:
      return True
    else:
      pass
  return False

print palindrome_checker('civic')
print palindrome_checker('cciiv')
print palindrome_checker('cat')
print palindrome_checker('cta')