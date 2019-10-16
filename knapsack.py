import collections
from itertools import combinations

items = [4, 5, 12, 7, 3, 6]

max_weight = 18
knapsack = 7
largest_sum = 0

for i in range(len(items)):
	possibilities = list(combinations(items, i+1))
	sum_possibilities = [sum(tup) for tup in possibilities]
	max_value = max(sum_possibilities)

	if max_value > largest_sum:
		largest_sum = max_value
	


result = list(combinations(items, 4))
sum_possibilities = [sum(tup) for tup in result]


tw  = 100
items = {'a': 12, 'b': 15, 'c': 20, 'd': 30, 'e': 100}
def get_max_value(items):
	return mv

def knapsack1(all_items, tw):
	res = max(all_items)
	if res == tw:
		return res




items_weight = {'a': 12, 'b': 15, 'c': 20, 'd': 30, 'e': 16}
weight_list = [item for item in items_weight.values()]
weight_keys = [item for item in items_weight.keys()]

items_value = {'a': 1, 'b': 2, 'c': 4, 'd': 3, 'e': 1}
value_list = [item for item in items_value.values()]

max_weight = 58

Items = collections.namedtuple('Items', 'weight value')


def get_max_weight(weight_list, max_weight):
	largest_sum = 0

	for i, item in enumerate(weight_list, 1):
		possible_combinations = list(combinations(weight_list, i))
		sum_possibilities = [sum(tup) for tup in possible_combinations]

		if max(sum_possibilities) <= max_weight:
			acceptable_total = max(sum_possibilities)

		print(acceptable_total, 'here')

		if acceptable_total > largest_sum:
			largest_sum = acceptable_total
			possibilities = sum_possibilities

		for i in range(len(possible_combinations)):
			print(possible_combinations[i])
			print(sum(possible_combinations[i]))
	
	return largest_sum, possibilities


def knapsack(weight_list, max_weight, items_value):
	largest_possible_weight = get_max_weight(weight_list, max_weight)

	for i, item in enumerate(weight_list):
		pass
	pass

print(get_max_weight(weight_list, max_weight))




