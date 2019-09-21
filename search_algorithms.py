#!/usr/bin/env python
"""
Basic implementation of common search algorithms using Python.
"""

from statistics import median, median_low, median_high


def linear_search(items, item):
	for i in range(len(items)):
		if items[i] == item:
			return '{} found at index {}'.format(item, i)
		else:
			return '{} not found'.format(item)


def linear_search_2(item, items):
	# A more Pythonic way of implementing this algorithm
	try:
		result = items.index(item)
	except ValueError:
		return '{} not found'.format(item)

	return '{} found at index {}'.format(item, result)


def binary_search(items, item):
	items.sort()
	response = 'Item {} not found'.format(item)
	found = False

	while items and not found:
		print('Searching for {}'.format(item))
		list_size = len(items)
		if (list_size%2) == 0:
			mid = items.index(median_low(items))
		else:
			mid = items.index(median(items))

		if item == items[mid]:
			found = True
			response = 'Item {} found'.format(item)
		else:
			if item > items[mid]:
				new_list = [i for i in items if items.index(i) > mid]
			else:
				new_list = [i for i in items if items.index(i) <= mid]
			items = new_list

	return response
