from declension import equals_modulo_case_and_unicode, weak_contains


def test_equals_modulo_case_and_unicode():
	assert equals_modulo_case_and_unicode('maneō', 'maneo')
	assert equals_modulo_case_and_unicode('flōreō', 'Floreo')
	assert equals_modulo_case_and_unicode('parātus', 'pAratus')
	assert equals_modulo_case_and_unicode('rīsī', 'RISI')
	assert equals_modulo_case_and_unicode('prōfūi', 'profui')
	assert equals_modulo_case_and_unicode('dēnique', 'deNiQue')


def test_weak_contains():
	assert weak_contains(['third'], 'third consonant')
	assert weak_contains(['second', 'third'], 'third consonant')
	assert weak_contains(['third'], 'third')
	assert not weak_contains(['second'], 'third')
	