import json
import random
import sys
import copy
from shortcuts import short

# todo accent in verb dict
# not all combinations are possible - ex. for imperativus. how to handle it ?
# map different inputs ex. both 'activus' and 'active' should be understood
# todo count remaining words (lowest level) if repeat is not chosen. print score after all
# todo unit tests for counting
# todo use random choise to estimate number of words
# todo during comparison replace multiple white letters with one

# todo method nth level key contains

# in the future use maybe n-dimensional array rather than dictionary 

def equals_modulo_case_and_unicode(str1, str2):
	def replace_unicode(s):
		return s.replace('ā', 'a').replace('ē', 'e').replace('ō', 'o').replace('ū', 'u').replace('ī', 'i')
	return replace_unicode(str1.lower()) == replace_unicode(str2.lower())


args = sys.argv[1:]

conjugations_to_include = []
moods_to_include = []
tenses_to_include = []
voices_to_include = []

if len(args) > 0:
	args_parsed = [x for x in ' '.join(args).split('-') if len(x) > 0]
	# ex. ['c first fourth ', 'm indicativus ', 't praesens ', 'v activus']

	def to_include(letter):
		forms = [x for x in args_parsed if x[0] == letter]
		if len(forms) > 0:
			return forms[0][2:].rstrip().split(' ')
		else:
			return []

	conjugations_to_include = to_include('c')
	moods_to_include = to_include('m')
	tenses_to_include = to_include('t')
	voices_to_include = to_include('v')

file = open("conjugation.json")
con_raw = json.load(file)
file.close()

con = con_raw
con_with_conjugations_removed = {}
if len(conjugations_to_include) > 0:
	for base_word in con_raw.keys():
	    for con_number in con_raw[base_word].keys():
	    	if con_number in conjugations_to_include:
	    		con_with_conjugations_removed[base_word] = con_raw[base_word]
	con = con_with_conjugations_removed

### remove moods not from the list
if len(moods_to_include) > 0:
	con_with_moods_removed = copy.deepcopy(con)
	for base_word in con.keys():
		for con_number in con[base_word].keys():
			for mood in con[base_word][con_number].keys():
				if mood not in moods_to_include:
					del con_with_moods_removed[base_word][con_number][mood]
	con = con_with_moods_removed

### remove tenses not from the list
if len(tenses_to_include) > 0:
	con_with_tenses_removed = copy.deepcopy(con)
	for base_word in con.keys():
		for con_number in con[base_word].keys():
			for mood in con[base_word][con_number].keys():
				for tense in con[base_word][con_number][mood].keys():
					if tense not in tenses_to_include:
						del con_with_tenses_removed[base_word][con_number][mood][tense]
	con = con_with_tenses_removed

### remove voices not from the list
if len(voices_to_include) > 0:
	con_with_voices_removed = copy.deepcopy(con)
	for base_word in con.keys():
		for con_number in con[base_word].keys():
			for mood in con[base_word][con_number].keys():
				for tense in con[base_word][con_number][mood].keys():
					for voice in con[base_word][con_number][mood][tense].keys():
						if voice not in voices_to_include:
							del con_with_voices_removed[base_word][con_number][mood][tense][voice]
	con = con_with_voices_removed


def count_all_entries(d):
	cnt_temp = 0
	for word in list(d.keys()):
	    for conjugation in list(d[word].keys()):
	    	for mood in list(d[word][conjugation].keys()):
	    		for tense in list(d[word][conjugation][mood].keys()):
	    			for voice in list(d[word][conjugation][mood][tense].keys()):
	    				for number in list(d[word][conjugation][mood][tense][voice].keys()):
	    					for person in list(d[word][conjugation][mood][tense][voice][number].keys()):
	    						cnt_temp = cnt_temp + 1
	return cnt_temp


print('there\'s {} words in dict'.format(count_all_entries(con)))

correct_cnt = 0
wrong_cnt = 0
	
while(con != {}):
	base_word = random.choice(list(con.keys()))
	conjugation_number = random.choice(list(con[base_word]))
	mood = random.choice(list(con[base_word][conjugation_number]))
	tense = random.choice(list(con[base_word][conjugation_number][mood].keys()))
	voice = random.choice(list(con[base_word][conjugation_number][mood][tense].keys()))
	number = random.choice(list(con[base_word][conjugation_number][mood][tense][voice].keys()))
	person = random.choice(list(con[base_word][conjugation_number][mood][tense][voice][number].keys()))

	print('{}: {} {} {} {} {} person'.format(base_word, short(mood), short(tense), short(voice), short(number), short(person)))
	answer = input("")
	correct_answer = con[base_word][conjugation_number][mood][tense][voice][number][person]
	if equals_modulo_case_and_unicode(correct_answer, answer):
		correct_cnt = correct_cnt + 1
		if '--repeat' not in args:
			del con[base_word][conjugation_number][mood][tense][voice][number][person]
			if con[base_word][conjugation_number][mood][tense][voice][number] == {}:
				del con[base_word][conjugation_number][mood][tense][voice][number]
				if con[base_word][conjugation_number][mood][tense][voice] == {}:
					del con[base_word][conjugation_number][mood][tense][voice]
					if con[base_word][conjugation_number][mood][tense] == {}:
						del con[base_word][conjugation_number][mood][tense]
						if con[base_word][conjugation_number][mood] == {}:
							del con[base_word][conjugation_number][mood]
							if con[base_word][conjugation_number] == {}:
								del con[base_word][conjugation_number]
								if con[base_word] == {}:
									del con[base_word]

			print("correct ({} left)".format(count_all_entries(con)))
		else:
			print("correct")
	else:
		wrong_cnt = wrong_cnt + 1
		print("wrong. correct answer is {}".format(correct_answer))
	print('')

score = correct_cnt / (correct_cnt + wrong_cnt) * 100
print('dictionary is empty. score is {}%'.format(round(score, 2)))
