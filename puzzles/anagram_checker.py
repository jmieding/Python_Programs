"""
Python 2.7.10

Puzzle: Given a string as an argument, write a function that returns
True if the string is an anagram, and False otherwise.
"""
from itertools import permutations

def anagram_checker(word):
  all_combos_of_word = permutations(word, len(word))
  for combo in all_combos_of_word:
    if combo == combo[::-1]:
      return True
    else:
      pass
  return False

print anagram_checker('civic')
print anagram_checker('cciiv')
print anagram_checker('cat')
print anagram_checker('cta')