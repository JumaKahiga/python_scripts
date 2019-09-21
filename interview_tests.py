#!/usr/bin/env python
"""
A compilation of some of the test questions I have recently come across.
"""


def find_max(nums):
    # Gets largest number
	max_num = float("-inf")
	for num in nums:
		if num > max_num:
			max_num = num
	return max_num


class Palindrome:
    # Checks whether a word is a palindrome
  @staticmethod
  def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
    	return True
    return False


def is_leap(year):
    # Checks whether a year is a leap one
    leap = False
    
    if year%4 == 0:
        if year%100 == 0 and year%400 == 0:
            leap = True
        elif not year%100 == 0:
        	leap = True
    return leap


# Minion Game I coded from a Hacker Rank test
vowels = 'AEIOU'
word = 'BANANA'

stuart_marks = 0
kevin_marks = 0

for i in range(len(word)):
	if word[i] in vowels:
		kevin_marks = kevin_marks + len(word) - (i+1) + 1
	else:
		stuart_marks = stuart_marks + len(word) - (i+1) + 1

print('Stuart Marks: ', stuart_marks, 'Kevin Marks: ', kevin_marks)
