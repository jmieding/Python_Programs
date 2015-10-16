"""
This is a homework assignment from Google's Python course. https://developers.google.com/edu/python/?hl=en
This program uses python 2.7.10 to sort and return all words in a user-provided text file. 

This program requires importing the prettytable module to display the results.
You can install the prettytable module with with the command: 'easy_install prettytable'
"""

import re
from prettytable import PrettyTable

display = PrettyTable(["Word", "Times in File"])
text_file = open(raw_input("What file do you want to analyze? "))
words_in_file = re.findall(r'\w+\'\w+|\'\w+|\w+\'|\w+\-\w+|\w+', text_file.read())
table = {} # will store each word and the number of times it appears in the file as key, value pair.

for word in words_in_file:
  word = word.lower()
  if word in table:
	table[word] += 1
  else:
	table[word] = 1

# Sort Words by Frequency
def count_words_frequency():
  words_sorted = sorted(table.items(), key=lambda tup: tup[1], reverse = True)
  for tup in words_sorted:
    display.add_row([tup[0], tup[1]])
  print display
		
# Sort Words Alphabetically
def count_words_alphabet():
  for word in sorted(table.keys()):
    display.add_row([word, table[word]])
  print display
  
count_words_frequency()
# count_words_alphabet()