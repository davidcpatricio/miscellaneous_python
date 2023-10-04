# Python Essentials 2 - 2.5.1.8

import sys

anagrams = True

first_text = input("Enter the first text: ")
second_text = input("Enter the second text: ")

if first_text == '' or second_text == '':
    print('An empty string is not an anagram.')
    sys.exit()

# Only letters are considered
first_array = []
for letter in first_text:
    if letter.isalpha():
        first_array.append(letter.lower())  # Case insensitive

second_array = []
for letter in second_text:
    if letter.isalpha():
        second_array.append(letter.lower())

# We presume anagrams contain the same amount of characters
if len(first_array) != len(second_array):
    anagrams = False
else:
    for letter in first_array:
        if letter not in second_array:
            anagrams = False
            break
        else:
            second_array.remove(letter)

if anagrams:
    print("Anagrams")
else:
    print("Not anagrams")
