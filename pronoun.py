import json
import random
import sys
from shortcuts import short

file = open("pronoun.json")
pronouns_raw = json.load(file)
file.close()

to_include = sys.argv[1:]
if len(to_include) == 0:
	to_include = ['is', 'hic', 'ille', 'idem', 'qui', 'nullus']


def only_selected_pronouns(to_include_list):
	pronouns = {}
	for k in pronouns_raw.keys():
		if k in to_include_list:
			pronouns[k] = pronouns_raw[k]
	return pronouns


def count_all_entries(d):
	cnt_temp = 0
	for base_word in list(d.keys()):
		for genre in list(d[base_word].keys()):
			for number in list(d[base_word][genre].keys()):
				for case in list(d[base_word][genre][number].keys()):
					cnt_temp = cnt_temp + 1
	return cnt_temp

pronouns = only_selected_pronouns(to_include)

cnt = count_all_entries(pronouns)
cnt_correct = 0
cnt_wrong = 0

while(len(pronouns) > 0):
	base_word = random.choice(list(pronouns.keys()))
	genre = random.choice(list(pronouns[base_word].keys()))
	number = random.choice(list(pronouns[base_word][genre].keys()))
	case = random.choice(list(pronouns[base_word][genre][number].keys()))

	print('{} {} {} {}'.format(short(base_word), short(genre), short(case), short(number)))
	answer = input("")
	correct_answer = pronouns[base_word][genre][number][case]

	if answer == correct_answer:
		del pronouns[base_word][genre][number][case]
		if pronouns[base_word][genre][number] == {}:
			del pronouns[base_word][genre][number]
			if pronouns[base_word][genre] == {}:
				del pronouns[base_word][genre]
				if pronouns[base_word] == {}:
					del pronouns[base_word]
		print('correct (left {})'.format(count_all_entries(pronouns)))
		cnt_correct = cnt_correct + 1
	else:
		print('wrong. correct answer is \'{}\''.format(correct_answer))
		cnt_wrong = cnt_wrong + 1
	print('')

score = cnt_correct / (cnt_correct + cnt_wrong) * 100
print('current dict is empty. score: {}%'.format(round(score, 2)))