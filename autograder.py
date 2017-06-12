import unittest, sys
from graderlib import test_case
import practice as module


"""
Dictionary of allowed question test requests
	Dictionary of functions in practice part
	of this question test
		Function to be tested: list of lists
		which correspond to a test input for
		this function and an expected output
"""
question_inputs = {
	"q1": {
		"min_val": [
			[(1, 2), 1],
			[(0, 0), 0],
			[(-4, -6), -6]
		],
		"max_val": [
			[(1, 2), 2],
			[(0, 0), 0],
			[(-4, -6), -4]
		],
		"a_plus_abs_b": [
			[(1, 2), 3],
			[(-3, -3), 0],
			[(4, -2), 6]
		],
		"weather": [
			[(40,), "cold"],
			[(61,), "warm"],
			[(60,), "warm"],
			[(81,), "hot"],
			[(80,), "hot"]
		],
		"weather_2":[
			[(40, 0.1), "cold and dry"],
			[(45, 0.3), "cold and damp"],
			[(50, 0.5), "cold and rainy"],
			[(60, 0.19), "warm and dry"],
			[(60, 0.2), "warm and humid"],
			[(70, 0.7), "warm and rainy"],
			[(80, 0.1), "hot and arid"],
			[(90, 0.4), "hot and humid"],
			[(100, 0.9), "hot and rainy"]
		]
	},
	"q2": {
		"skip_range": [
			[(0, 10), [0, 2, 4, 6, 8, 10]],
			[(1, 9), [1, 3, 5, 7, 9]],
			[(2, 7), [2, 4, 6]],
			[(3, 6), [3, 5]]
		],
		"skip_by_range": [
			[(0, 100, 10), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]],
			[(5, 27, 6), [5, 11, 17, 23]],
			[(21, 60, 4), [21, 25, 29, 33, 37, 41, 45, 49, 53, 57]],
			[(9, 30, 7), [9, 16, 23, 30]]
		],
		"power_range": [
			[(1, 10, 1), [i for i in range(1, 11)]],
			[(3, 17, 3), [i ** 3 for i in range(3, 18)]],
			[(2, 12, 4), [i ** 4 for i in range(2, 13)]]
		]
	},
	"q3": {
		"difference_sq": [
			[([],), []],
			[([0, 1, 2, 3, 4, 5, 6],), [1, 1, 1, 1, 1, 1]],
			[([1, 4, 9, 16, 25, 36, 49, 64],), [3, 5, 7, 9, 11, 13, 15]],
			[([1, 0, 1, 0, 1, 0],), [-1, 1, -1, 1, -1]],
			[([1, -2, 3, -4, 5, -6, 7, -8],), [-3, 5, -7, 9, -11, 13, -15]]
		],
		"quotient_sq": [
			[([],), []],
			[([1, 1, 1, 1, 1, 1],), [1, 1, 1, 1, 1]],
			[([1, 2, 3, 4, 5, 6],), [2, 1.5, 4 / 3, 1.25, 1.2]],
			[([1, 4, 9, 16, 25, 36],), [4, 2.25, 16 / 9, 25 / 16, 1.44]],
			[([1, 1, 2, 3, 5, 8, 13],), [1, 2, 1.5, 5 / 3, 1.6, 1.625]]
		],
		"factorial": [
			[(1,), 1], [(2,), 2], [(3,), 6], [(4,), 24], [(5,), 120], [(6,), 720]
		],
		"fibonacci": [
			[(0,), 0], [(1,), 1], [(2,), 1], [(3,), 2], [(4,), 3], [(5,), 5],
			[(6,), 8], [(7,), 13], [(8,), 21], [(9,), 34], [(10,), 55]
		],
		"golden_ratio_approx": [
			[(1,), [1]],
			[(2,), [1, 2]],
			[(3,), [1, 2, 1.5]],
			[(4,), [1, 2, 1.5, 5 / 3]],
			[(5,), [1, 2, 1.5, 5 / 3, 1.6]],
			[(6,), [1, 2, 1.5, 5 / 3, 1.6, 1.625]],
			[(10,), [1, 2, 1.5, 5 / 3, 1.6, 1.625, 21 / 13, 34 / 21, 55 / 34, 89 / 55]]
		]
	},
	"q4": {
		"travel": [
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [True, False, False, False]), "Spain"],
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [True, True, False, True]), "Spain"],
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [False, True, False, False]), "Argentina"],
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [False, False, True, False]), "Mexico"],
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [False, False, False, True]), "Guatemala"],
			[(["Spain", "Argentina", "Mexico", "Guatemala"], [False, False, False, False]), None],
		],
		"min_val_2": [
			[([1, 2, 3, 4],), 1],
			[([1, 3, -2, 100, -5],), -5]
		],
		"max_val_2": [
			[([1, 2, 3, 4],), 4],
			[([1, 3, -2, 100, -5],), 100]
		]
	},
	"q5": {
		"zip_up": [
			[([1, 2, 3, 4], [5, 6, 7, 8]), [[1, 5], [2, 6], [3, 7], [4, 8]]],
			[([1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]), [[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]]
		],
		"zip_down": [
			[([[1, 2], [3, 4], [5, 6], [7, 8]],), ([1, 3, 5, 7], [2, 4, 6, 8])],
			[([[0, 0], [1, 1], [2, 2], [3, 3]],), ([0, 1, 2, 3], [0, 1, 2, 3])]
		]
	},
	"q6": {
		"n_zip_up": [
			[([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]),
				[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]],
			[([1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]),
				[[1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0]]]
		],
		"n_zip_down": [
			[([[1, 2, 2], [3, 4, 4], [5, 6, 6], [7, 8, 8]],),
				[[1, 3, 5, 7], [2, 4, 6, 8], [2, 4, 6, 8]]],
			[([[0, 0, 10, 20], [1, 1, 20, 30], [2, 2, 30, 40], [3, 3, 40, 50], [4, 4, 50, 60]],),
				[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [10, 20, 30, 40, 50], [20, 30, 40, 50, 60]]]
		]
	}
}

def run_test(questions):
	for question in questions:
		# test is the instance of our TestCase class with all of our
		# desired question, specified by argv[1], functions to be tested.
		test = test_case(module, question, question_inputs)

		# not test corresponds to a requested question test which
		# doesn't exist
		if not test:
			return

		# adds our TestCase to the global attributes so that unittest
		# will find it when it searches for TestCases to run
		globals()[test.__name__] = test

	# Displays which questions are being tested
	plural = ('s ' if len(questions) > 1 else ' ')
	q_string = ', '.join([questions[i][1:] for i in range(len(questions))])
	print('\nRunning Test' + plural + 'for Question' + plural + q_string)
	print()


	"""
	argv='q' allows the program to use the command line arguments
	as the question input. q is a dummy attribute class of __main__
	so that the unittest will run that as the passed in command
	arguments, then our program can access the actual command args
	without them messing up the unittest! DO NOT make the value for
	argv more than one character: no clue why, but the unittest main
	function tries to split the argv value into single characters so
	unless we have each of those individual characters defined as
	dummy attribute classes of __main__ (which there's no reason to
	do so), so leave argv='q'.
	"""
	unittest.main(argv='q')

def main():
	# Test all questions.
	if len(sys.argv) == 1:
		run_test([question for question in question_inputs])
	# Test one specific question specified
	# by the single argument passed in.
	elif len(sys.argv) == 2:
		run_test([sys.argv[1]])
	# Too many arguments.
	else:
		run_test([sys.argv[i] for i in range(1, len(sys.argv))])

if __name__ == '__main__':
	main()
