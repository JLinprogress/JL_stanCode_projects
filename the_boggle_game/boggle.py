"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()

	all_w = read_dictionary()
	board = get_the_data_base()
	counter = [0]
	for i in range(1, 5):
		for j in range(1, 5):
			possible = surrounding((i, j), board)
			boggle(possible, board[(i, j)], all_w, [(i, j)], board, counter, [])
	print(f'There are {counter[0]} words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(possible, check, all_word, already_used, board, found_times, found):
	if len(check) >= 4 and check in all_word and check not in found:
		found.append(check)
		print(f'Found "{check}"')
		found_times[0] += 1

		if has_prefix(check, all_word):
			for key in possible:
				val = possible[key]
				if has_prefix(check + val, all_word) and key not in already_used:
					check += val
					already_used.append(key)  # choose
					potential = surrounding(key, board)
					boggle(potential, check, all_word, already_used, board, found_times, found)
					already_used.pop()  # un-choose
					check = check[:len(check) - 1]
		return
	else:
		for key in possible:
			val = possible[key]
			if has_prefix(check + val, all_word) and key not in already_used:
				check += val
				already_used.append(key)		# choose
				potential = surrounding(key, board)
				boggle(potential, check, all_word, already_used, board, found_times, found)
				already_used.pop()				# un-choose
				check = check[:len(check)-1]


def surrounding(location, board):
	(x, y) = location
	possible = {}
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if x+i <= 0 or x+i >= 5 or y+j <= 0 or y+j >= 5 or i == 0 and j == 0:
				pass
			else:
				possible[(x + i, y + j)] = board[(x + i, y + j)]
	return possible


def find_out(poss, all_w):
	for each in poss:
		if each[0] not in all_w:
			pass
		else:
			if each in all_w[each[0]]:
				print(f'Found "{each}"')


def get_the_data_base():
	letters_board = {}
	counter = 0
	while True:
		counter += 1
		row = input('1 row of letters: ')  # (1,1),(2,1),(3,1),(4,1)
		row = row.replace(" ", ",")
		if len(row) != 7:
			print('Illegal input')
			break
		else:
			row = row.replace(",", '')
			for i in range(1, 5):
				letters_board[(i, counter)] = row[i - 1]
		if counter == 4:
			return letters_board


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	all_word = []
	with open(FILE, 'r')as f:
		for word in f:
			word_cleaned = word.strip()
			all_word.append(word_cleaned)
	return all_word


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (dic) The dictionary that stores all the words to be looked for.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for words in dictionary:
		if words.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
