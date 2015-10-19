""""
Python 2.7.10

Puzzle: Return the number of vowels in a given string.

"""

print "\nThis program counts how many vowels are in some text."

text = raw_input("\nInsert your text here: \n")

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0

for letter in text:
	if letter in vowels:
		vowel_count += 1

print "\nNumber of vowels: %d" % (vowel_count)