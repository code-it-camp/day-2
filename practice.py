# ------------------------------------------------------------------------- #
#																			#
# Question 1																#
# ------------------------------------------------------------------------- #
def min_val(a, b):
	"""
	Implementation of min for two values.

	Args:
		a: number
		b: number

	Returns:
		the lesser of the two arguments
	"""
	# FIXME
	if ________:
		return ________
	else:
		return ________

def max_val(a, b):
	"""
	Implementation of max for two values.

	Args:
		a: number
		b: number

	Returns:
		the greater of the two arguments
	"""
	# FIXME
	if ________:
		return ________
	else:
		return ________

def a_plus_abs_b(a, b):
	"""
	a + |b| but NO calls to abs

	Args:
		a: number
		b: number

	Returns:
		a + |b|
	"""
	# FIXME
	if ________:
		return ________
	else:
		________

def weather(temp):
	"""
	For temperatures less than 60 return "cold", between 60 and 80 return
	"warm", and greater than 80 return "hot"

	Args:
		temp: number, represents temperature

	Returns:
		a description of the weather based off temperature
	"""
	# FIXME
	if ________:
		return ________
	elif ________:
		return ________
	else:
		return ________

def weather_2(temp, hum):
	"""
	For temperatures less than 60 return "cold", between 60 and 80 return
	"warm", and greater than 80 return "hot".
	For humidities in the range 0 up to 0.2 return "dry" if "cold" or "warm"
	and "arid" if "hot", in the range 0.2 to 0.5 return "damp" if "cold" and
	"humid" if "warm" or "hot", and greater than 0.5 return "rainy".

	Args:
		temp: number representing temperature
		hum: number representing humidity, ranged from 0 to 1

	Returns:
		a single string describing the weather following the format of
		"hot and dry"
	"""
	assert hum >= 0 and hum < 1
	# FIXME
	________

# ------------------------------------------------------------------------- #
#																			#
# Question 2																#
# ------------------------------------------------------------------------- #
def skip_range(start, end):
	"""
	Creates a list of integers from start to end with every other integer
	skipped. So if start is even, creates a list of evens up to end and vice
	versa if start is odd. Do not assume that start and even have the same
	parity (i.e. they are both odd or both even).

	Args:
		start: number
		end: number

	Returns:
		a list of every other integer from start going to end or up to the
		previous integer
	"""
	# FIXME
	________

def skip_by_range(start, end, n):
	"""
	Similar to skip_range except that we are now skiping by the specified
	number of integers.

	Args:
		start: number
		end: number
		n: number, amount of integers to skip from number to number in the range
		(i.e. n = 0 is every integer from start to end and n = 1 results in
		an equivalent range to skip_range)

	Returns:
		a list of integers
	"""
	# FIXME
	________

def power_range(start, end, n):
	"""
	Creates a list of numbers from start to end with each item in the list
	being the its value to the power of n.
	(i.e. power_range(1, 4, 2) returns [1, 4, 9, 16])

	Args:
		start: number
		end: number
		n: number, exponent each item is being raised to

	Returns:
		a list of integers
	"""
	# FIXME
	________

# ------------------------------------------------------------------------- #
#																			#
# Question 3																#
# ------------------------------------------------------------------------- #
def difference(lst):
	"""
	Creates a list of the differences of each item in the list, with
	the first item remaining unchanged. A difference would look like
	this: (i.e. b_i = a_i - a_(i-1))
		[1, 4, 9, 16, 25] --> [1, 3, 5, 7, 9]
		[1, 8, 27, 64, 125] --> [1, 7, 19, 61]

	Args:
		lst: a list of numbers

	Returns:
		a list of numbers
	"""
	# FIXME
	________

def factorial(n):
	"""
	Produces the nth factorial or (n!).
	n! is defined as n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
	0! is defined as 1

	Args:
		n: a non-negative integer

	Returns:
		n!, a number
	"""
	# FIXME
	product = ________
	for ________ in ________:
		________
	return ________

def fibonnaci(n):
	"""
	Produces the nth number in the Fibonacci sequence. Rather than giving a
	shorthanded explanation I suggest checking out this link for a good
	description of the Fibonacci numbers: https://en.wikipedia.org/wiki/Fibonacci_number
	For our purposes, assume that fibonacci(0) = 0 and fibonacci(1) = 1.

	Args:
		n: the index of the desired Fibonacci number

	Returns:
		the nth Fibonacci number
	"""
	# FIXME
	a, b = ________, ________
	while ________:
		________
	return ________

def golden_ratio_approx(n):
	"""
	Produces a list of approximations for the golden ratio. We'll consider the
	nth approximation of the golden ratio to be the (n+1)th Fibonacci number
	divided by the nth Fibonacci number. We want a list of all the approximations
	from i = 0 up to i = n.
	(i.e. golden_ratio_approx(4) returns [1, 2, 3 / 2, 5 / 3, 8 / 5])

	Args:
		n: number, want this many + 1 approximations of golden ratio

	Returns:
		a list of numbers (should be n + 1 long)
	"""
	# FIXME
	________

# ------------------------------------------------------------------------- #
#																			#
# Question 4																#
# ------------------------------------------------------------------------- #
def travel(destinations, interested):
	"""
	Determines the first place in the provided list of possible destinations
	that the user wants to go to based off the provided list of interests.
	An item in interested corresponds to the users interest in the
	destination in destinations at the same index as the item in interested.
	If not interested in any of the destinations, don't return anything.

	Args:
		destinations: list of strings
		interested: list of booleans

	Returns:
		string, the first destination user is interested in, otherwise None
	"""
	# FIXME
	for ________ in ________:
		if ________:
			return ________

def min_val(lst):
	"""
	Fully implements the min function for a list of functions. You may use your
	previous implementation of min_val or max_val but you may not use the
	built-in min or max functions!

	Args:
		lst: a list of numbers

	Returns:
		the lowest valued number in the provided list
	"""
	# FIXME
	________

def max_val(lst):
	"""
	Fully implements the max function for a list of functions. You may use your
	previous implementation of min_val or max_val but you may not use the
	built-in min or max functions!

	Args:
		lst: a list of numbers

	Returns:
		the highest valued number in the provided list
	"""
	# FIXME
	________

# ------------------------------------------------------------------------- #
#																			#
# Question 5																#
# ------------------------------------------------------------------------- #
def zip_up(lst1, lst2):
	"""
	Implements the zip function, which refers to the process of making
	a list of lists with each inner list cotaining the items from lst1 and
	lst2 at the index of this inner list.
	For example: zip_up([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]) returns
		[[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]].
	Assume that ls1 and lst2 have the same lengths.

	Args:
		lst1: a list
		lst2: a list

	Returns:
		a zipped up list of lists
	"""
	assert len(lst1) == len(lst2)

	# FIXME
	________

def zip_down(lst):
	"""
	Unzips a list of lists.
	For example: zip_down([[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]])
		returns two lists: [1, 2, 3, 4, 5] and [10, 20, 30, 40, 50].
	You can assume that each list with in the list only has two items.

	Args:
		lst: a list of lists

	Returns:
		two unzipped lists
	"""
	for lst_item in lst:
		assert isinstance(lst_item, list)
		assert len(lst_item) == 2

	# FIXME
	________

# ------------------------------------------------------------------------- #
#																			#
# Question 6: Extra Problems												#
# ------------------------------------------------------------------------- #
def n_zip_up(*lsts):
	"""
	Zips up all the lists passed in as lsts. If lsts only contains two lists,
	this function has the same effect as zip_up. Once again, assume that all
	lists in lst have the same length.

	Args:
		lst: a list of lists to be zipped

	Returns:
		a zipped up list of lists
	"""
	for lst in lsts:
		assert len(lst) == len(lsts[0])

	# FIXME
	________

def n_zip_down(lst):
	"""
	Zips down all the lists contained in lst. If there are only two values
	in each list inside of the passed in list, this function will have the
	same effect as zip_down.

	Args:
		lst: a list of lists, with each list item containing the same number
		of items as the other lists

	Returns:
		a list of unzipped lists; this list will contain n lists if there
		were n values in each zipped list
	"""
	# FIXME
	________
