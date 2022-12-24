import sys
import re
import json
import copy
import random
from shortcuts import short


def args_dict(args):
	args_separated = re.findall('-[a-z]+ [a-z, ]*', args)
	d = {}
	for arg in args_separated:
		key_and_val = re.split(' ', arg, maxsplit=1)
		key = key_and_val[0][1:] # remove '-' from the beginning
		values_merged = key_and_val[1].rstrip()
		value_list = re.split(' *', values_merged) # ex. 'positivus  comparativus' -> ['positivus', 'comparativus']
		d[key] = value_list
	return d


args = {}
command_line_args_merged = ' '.join(sys.argv[1:])
if len(command_line_args_merged) > 0:
	args = args_dict(command_line_args_merged)

file = open('adjective.json')
adjectives_all = json.load(file)
file.close()


def remove_words_other_than(adj_dict, w_list):
	adj_with_words_removed = copy.deepcopy(adj_dict)
	for word in adj_dict.keys():
		first_word = re.split(',', word)[0]	# 'acerbus, acerba, acerbum' -> 'acerbus'
		if not any([x == first_word for x in w_list]):	# because acer is in acerbus
			del adj_with_words_removed[word]

	return adj_with_words_removed


def remove_declensions_other_than(adj_dict, dec_list):
	adj_with_declensions_removed = copy.deepcopy(adj_dict)
	for word in adj_dict.keys():
		for declension_number in adj_dict[word].keys():
			if not any([x in declension_number for x in dec_list]):
				del adj_with_declensions_removed[word][declension_number]
				if adj_with_declensions_removed[word] == {}:
					del adj_with_declensions_removed[word]

	return adj_with_declensions_removed


def remove_genres_other_than(adj_dict, genre_list):
	adj_with_genres_removed = copy.deepcopy(adj_dict)
	for word in adj_dict.keys():
		for declension_number in adj_dict[word].keys():
			for genre in adj_dict[word][declension_number].keys():
				if genre not in genre_list:
					del adj_with_genres_removed[word][declension_number][genre]
					if adj_with_genres_removed[word][declension_number] == {}:
						del adj_with_genres_removed[word][declension_number]
						if adj_with_genres_removed[word] == {}:
							del adj_with_genres_removed[word]

	return adj_with_genres_removed


def remove_grades_other_than(adj_dict, grades_list):
	adj_with_grades_removed = copy.deepcopy(adj_dict)
	for word in adj_dict.keys():
		for declension_number in adj_dict[word].keys():
			for genre in adj_dict[word][declension_number].keys():
				for grade in adj_dict[word][declension_number][genre].keys():
					if grade not in grades_list:
						del adj_with_grades_removed[word][declension_number][genre][grade]
						if adj_with_grades_removed[word][declension_number][genre] == {}:
							del adj_with_grades_removed[word][declension_number][genre]
							if adj_with_grades_removed[word][declension_number] == {}:
								del adj_with_grades_removed[word][declension_number]
								if adj_with_grades_removed[word] == {}:
									del adj_with_grades_removed[word]

	return adj_with_grades_removed


adj_with_words_removed = remove_words_other_than(adjectives_all, w_list=args.get('w', ['acer', 'facilis', 'sapiens', 'acerbus']))
adj_with_declensions_removed = remove_declensions_other_than(adj_with_words_removed, dec_list=args.get('d', ['first', 'second', 'third']))
adj_with_genres_removed = remove_genres_other_than(adj_with_declensions_removed, genre_list=args.get('genre', ['masculinum', 'femininum', 'neutrum']))
adj_final = remove_grades_other_than(adj_with_genres_removed, grades_list=args.get('g', ['positivus', 'comparativus', 'superlativus']))


def count_all_entries(d):
	cnt_temp = 0
	for word in list(d.keys()):
		for declension in list(d[word].keys()):
			for genre in list(d[word][declension].keys()):
				for grade in list(d[word][declension][genre].keys()):
					for number in list(d[word][declension][genre][grade].keys()):
						for case in list(d[word][declension][genre][grade][number].keys()):
							cnt_temp = cnt_temp + 1
	return cnt_temp


print('there\'s {} entries in dict'.format(count_all_entries(adj_final)))

correct_cnt = 0
wrong_cnt = 0

while(adj_final != {}):
	word = random.choice(list(adj_final.keys()))
	declension = random.choice(list(adj_final[word]))
	genre = random.choice(list(adj_final[word][declension]))
	grade = random.choice(list(adj_final[word][declension][genre].keys()))
	number = random.choice(list(adj_final[word][declension][genre][grade].keys()))
	case = random.choice(list(adj_final[word][declension][genre][grade][number].keys()))

	print('{}: {} {} {} {}'.format(word, short(genre), short(grade), short(case), short(number)))
	answer = input("")
	correct_answer = adj_final[word][declension][genre][grade][number][case]

	if answer == correct_answer:
		correct_cnt = correct_cnt + 1
		del adj_final[word][declension][genre][grade][number][case]
		if adj_final[word][declension][genre][grade][number] == {}:
			del adj_final[word][declension][genre][grade][number]
			if adj_final[word][declension][genre][grade] == {}:
				del adj_final[word][declension][genre][grade]
				if adj_final[word][declension][genre] == {}:
					del adj_final[word][declension][genre]
					if adj_final[word][declension] == {}:
						del adj_final[word][declension]
						if adj_final[word] == {}:
							del adj_final[word]

		print("correct ({} left)".format(count_all_entries(adj_final)))

	else:
		wrong_cnt = wrong_cnt + 1
		print("wrong. correct answer is {}".format(correct_answer))
	print('')

score = correct_cnt / (correct_cnt + wrong_cnt) * 100
print('dictionary is empty. score is {}%'.format(round(score, 2)))