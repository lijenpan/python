import collections

def find_duplicate_in_list(a):
	"""Return a distinct duplicate values in a list.

	>>> find_duplicate_in_list([1,2,3,2,1,5,6,5,5,5])
	[1, 2, 5]

	>>> find_duplicate_in_list([1,1,1])
	[1]

	>>> find_duplicate_in_list([1,2,3])
	[]
	"""

	return [x for x, y in collections.Counter(a).items() if y > 1]

if __name__ == '__main__':
	import doctest
	doctest.testmod()