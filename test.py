import sys

# python <..> -c <conjugation numbers> -m <moods> -t <tenses> -v <voices>

args = sys.argv[1:]

# ex ['-c', 'first', 'fourth', '-m', 'indicativus', '-t', 'praesens', '-v', 'activus']

if len(args) > 0:
	args_parsed = [x for x in ' '.join(args).split('-') if len(x) > 0]
	# ex. ['c first fourth ', 'm indicativus ', 't praesens ', 'v activus']

	def to_include(letter):
		forms = [x for x in args_parsed if x[0] == letter]
		if len(forms) > 0:
			return forms[0][2:].rstrip().split(' ')
		else:
			return []

	print(to_include('c'))
	print(to_include('m'))
	print(to_include('t'))
	print(to_include('v'))
