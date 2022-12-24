shortcuts = {
		'indicativus': 'ind',
		'praesens': 'praes',
		'imperfectum': 'imperf',
		'perfectum': 'perf',
		'futurum I': 'fut I',
		'futurum_I': 'fut I',
		'futurum II': 'fut II',
		'futurum_II': 'fut II',
		'plusquamperfectum': 'plusquamperf',
		'activus': 'act',
		'passivus': 'pass',
		'singularis': 'sing',
		'pluralis': 'pl',
		'first': '1',
		'second': '2',
		'third': '3',
		'nominativus': 'nom',
		'genetivus': 'gen',
		'dativus': 'dat',
		'accusativus': 'acc',
		'ablativus': 'abl',
		'vocativus': 'voc',
		'masculinum': 'masc',
		'femininum': 'fem',
		'neutrum': 'neutr',
		'positivus': 'pos',
		'comparativus': 'comp',
		'superlativus': 'sup'
	}


def short(key):
	return shortcuts.get(key, key)