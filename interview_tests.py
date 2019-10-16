#!/usr/bin/env python
"""
A compilation of some of the test questions I have recently come across.
"""
import requests
from itertools import combinations, product


# Gets largest number
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


# Checks whether a word is a palindrome
class Palindrome:
    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        if word == word[::-1]:
            return True
        return False


# Checks whether a year is a leap one
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif not year % 100 == 0:
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


# Reversing the bytes in a binary file
def bytes_reverser(file_name):
    my_file = open(file_name, 'rb')
    inside_file = my_file.read()

    file_data = bytearray(inside_file)
    return file_data.reverse()


# Get items in a list that are not sorted
def correct_order(input_list):
    sorted_list = sorted(input_list)
    unsorted_items = 0

    for i in range(len(input_list)):
        if input_list[i] != sorted_list[i]:
            unsorted_items+=1

    return unsorted_items


def my_func(x):
    return x % 2 != 0


my_list = [
            7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 20,
            21, 0, 22, 27, 28, 30, 32, 33, 38, 40, 43,
            44, 46
        ]

print(list(filter(my_func, range(1, 6+1))))


def split_string(s):
    n = 0
    count = 0
    for i in range(len(s)):
        print(s[i:3])
        n +=1


# Get possible palindromes you can get from substrings
def count_palindrome(s):
    my_string = [s[i:j] for i, j in combinations(range(len(s) + 1), r=2)]
    count = 0

    for l in my_string:
        if l == l[::-1]:
            count +=1

    return count


# Complete the function below.
def getNumberOfMovies(substr):
    """
    Endpoint: "https://jsonmock.hackerrank.com/api/movies/search/?Title=substr"
    """
    URL = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(
        substr)
    response = requests.get(url=URL)
    data = response.json()
    return len(data)


arrival = [1, 3, 3, 5, 7]
duration = [2, 2, 1, 2, 1]

def maxEvents(arrival, duration):
    # Write your code here
    items = [arrival, duration]
    response = list(product(*items))
    for i in response:
        print(sum(i))
    return (len(response))


a_list = [-2, 1, 3, -4, 5]


def number_checker(items):
    for i in range(len(items)):
        possibilities = list(combinations(items, i+1))
        print(possibilities)


def solution_a(A):
    # write your code in Python 3.6
    integers_list = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9]

    my_list = set(A)
    a_list = list(set(integers_list).difference(my_list))
    return a_list


# Get numbers in a list that are even and their index is odd
A = [1, 3, 6, 4, 1, 2, 15, 100]
mang = [i for i in A if i%2 == 0 and A.index(i) % 2 != 0]


# Get compound words
EnglishWords = [
            "water", "big", "apple", "watch",
            "banana", "york", "amsterdam", "orange",
            "macintosh", "bottle", "book"
            ]

my_words = [
            "paris", "applewatch", "ipod", "amsterdam",
            "bigbook", "orange", "waterbottle"
            ]


def get_compound_words(source_words, input_words):
    result = []

    for i in input_words:
        for n in source_words:
            if i.startswith(n) and i != n:
                result.append(i)
    return result


# Get tallest candle
def candle_count(candles):
    tallest_candle = max(candles)
    result = candles.count(tallest_candle)
    return result


candles = [3, 2, 1, 6, 2, 1]


def camel_case_count(word):
    count = 0
    for i in word:
        if i.isupper():
            count += 1

    if word[0].islower():
        count += 1
    return count


def get_number_frequency(numbers):
    my_list = [i for i in numbers if numbers.count(i) > 1]
    res = []

    for i in my_list:
        tup = (i, numbers.count(i))
        res.append(tup)

    return dict(res)


numbers = [1,2,3,4,6,6,7,8,9,5,2,6,1,8]


def sum_array_integers(items):
    draft = [sum(i) for i in combinations(items, 4)]
    result = {'min': min(draft), 'max': max(draft)}
    return result


def spell_numbers(num):
    num_str = str(num)
    integer_count = len(num_str)
    place_values = {3: 'hundred', 4: 'thousand', 7: 'million', 10: 'billion'}
    int_dict = {1: 'one', 2: 'two', 3: 'three'}


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    print(count)
    maxOccurence = 1
    index = -1
    for i in range(N):
        print(i, end='')
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]


B = [1, 2, 3, 3, 1, 3, 1]

sample_data = [
    {"id": 123, "price": 270},
    {'id': 55, 'price': 145},
    {'id': 17, 'price': 70},
    {'id': 18, 'price': 500},
    {'id': 27, 'price': 130},
    {'id': 102, 'price': 230}
    ]

{18: 17, 27: 22}


def my_iter(items):
    result = [item.get('price') for item in items]
    output = []

    for i in range(1, len(items)):
        my_price = items[i].get('price')
        more_pop = result[:i]
        min_price = min(more_pop)

        if my_price > min_price:
            temp = (items[i].get('id'), items[more_pop.index(min_price)].get('id'))
            output.append(temp)

    return dict(output)
