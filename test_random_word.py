from random_word import parse_dict

lines_all = None
lines_three_words = ['lepidus, a, um [adj]', '1. uroczy, zachwycający', '2. dowcipny, wykwintny', 'acerbus, a, um [adj]', '1. kwaśny, cierpki, gorzki', '2. zgrzytliwy', '3. (o stylu) chropowaty, surowy', '4. niedojrzały, nieukończony', '5. przedwczesny', 'profugus, a, um [adj]', '1. uciekający, wygnany']
lines_one_word = ['lepidus, a, um [adj]', '1. uroczy, zachwycający', '2. dowcipny, wykwintny']


def test_parsing_correct_number_of_words_default_start_end():
	assert len(parse_dict(lines_three_words)) == 3


def test_parsing_correct_number_of_words_default_start_specified_end():
	assert len(parse_dict(lines_three_words, end=3)) == 2
	assert len(parse_dict(lines_three_words, end=4)) == 3
	assert len(parse_dict(lines_three_words, end=10)) == 3


def test_parsing_correct_number_of_words_default_end_specified_start():
	assert len(parse_dict(lines_three_words, start=1)) == 3
	assert len(parse_dict(lines_three_words, start=2)) == 2
	assert len(parse_dict(lines_three_words, start=3)) == 1
	assert len(parse_dict(lines_three_words, start=4)) == 0


def test_parsing_correct_number_of_words_specified_start_end():
	assert len(parse_dict(lines_three_words, start=1, end=2)) == 1
	assert len(parse_dict(lines_three_words, start=1, end=3)) == 2
	assert len(parse_dict(lines_three_words, start=1, end=10)) == 2


def test_parsing_one_liner_is_correct():
	assert parse_dict(lines_one_word, 1, 2) == {'lepidus, a, um [adj]': ['1. uroczy, zachwycający', '2. dowcipny, wykwintny']}


def test_keys_are_latin_words():
	pass


def test_values_are_translations():
	pass