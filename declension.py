import json
import random
import sys
from shortcuts import short

# todo change distribution during working - ex. base on correct / wrong answers or on what was sampled before 
# todo remove nom singularis
# todo 'x' in feedback / or option remove correct
# todo dativus singularis -> dat sing etc
# todo during comparison replace multiple white letters with one

def equals_modulo_case_and_unicode(str1, str2):
	def replace_unicode(s):
		return s.replace('ā', 'a').replace('ē', 'e').replace('ō', 'o').replace('ū', 'u').replace('ī', 'i')
	return replace_unicode(str1.lower()) == replace_unicode(str2.lower())


def weak_contains(lst, x):
	# ex. declensions_to_include = ['third'] and possible declensions are 'third consonant', 'third vowel' etc.
	return any([s in x for s in lst])


if __name__ == '__main__':
	declensions_to_include = sys.argv[1:]

	file = open("declension.json")
	dec_raw = json.load(file)
	file.close()

	if len(declensions_to_include) == 0:
		dec = dec_raw
	else:
		dec = {base_word: dec_raw[base_word] for base_word in dec_raw.keys() if weak_contains(declensions_to_include, list(dec_raw[base_word].keys())[0])}

	while(len(dec) > 0):
		base_word = random.choice(list(dec.keys()))
		declension_number = random.choice(list(dec[base_word]))
		genre = random.choice(list(dec[base_word][declension_number]))
		number = random.choice(list(dec[base_word][declension_number][genre].keys()))
		case = random.choice(list(dec[base_word][declension_number][genre][number].keys()))

		print('{}: {} {}'.format(base_word, short(case), short(number))) 
		answer = input("")
		correct_answer = dec[base_word][declension_number][genre][number][case]
		if equals_modulo_case_and_unicode(correct_answer, answer):
			print("correct")
			print('')
		else:
			print("wrong. correct answer is {}".format(correct_answer))
			print('')

	# 	feedback = input("")
	# 	if 'x' in feedback:
	# 		del dec[base_word][declension_number][genre][number][case]
	# 		if dec[base_word][declension_number][genre][number] == None:
	# 			del dec[base_word][declension_number][genre][number]
	# 		if dec[base_word][declension_number][genre] == None:
	# 			del dec[base_word][declension_number][genre]
	# 		if dec[base_word][declension_number] == None:
	# 			del dec[base_word][declension_number]
	# 		if dec[base_word] == None:
	# 			del dec[base_word]
	# 		print('')
	# 	if 'c' in feedback:
	# 		print('there are {} words left in current dict'.format(len(dec)))
	# 		print(dec)
	# 		print('')

	print('current dictionary is empty. finishing program')
