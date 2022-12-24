# random_word.py
# should be run like 'python random_word.py <dict> <start> <end>' where <dict> may be latin or eng or nothing (then latin) and start / end makes a range of words to include (left inclusive, right not)
# if x is typed after seeing translation word will be removed from memory. when dict is empty program will finish
# if c is typed after seeing translation number of words left in dict will be printed
# those letters may be combined

# declension.py
# should be run like 'python declension.py' optionally followed by list of declensions to include ex. 'python declension.py first third mixed'
# possible: first second 'third mixed' 'third consonant' 'third vowel' 'fourth' 'fifth'

# conjugation.py
# ex. python conjugation.py -c first second -m indicativus -t praesens -v activus --repeat
# if no 'to include' is defined than all possibilities are included ex. python conjugation.py -t praesens will use all conjugations and time praesens
# right now to fully work one must set mode to 'indicativus' - because not all combinations ex. imperativus futurum I is possible
# --repeat tells that after successfull answer entry should not be deleted from the memory hence the same question will be asked again some other time

# pronoun.py
# python pronoun.py arg where arg may be one of [is, hic, ille, idem, qui, nullus]
# only first argument will be taken into account

# adjective.py
# ex. python adjective.py -g positivus comparativus -d third -genre femininum neutrum -w acer facilis
# grade(s) must be included in [positivus, comparativus, superlativus], declension in [first, second, third] and genre in [masculinum, femininum, neutrum]
# word must be one of [acer, facilis, sapiens, acerbus]
# no matter if declension will be 'first' or 'second' - acerbus will be included
# default is all possibilities

# count_words_in_dict.sh
# one argument - file name - if none then latin.txt

# find_duplicates_in_dict.sh
# one argument - file name - if none then latin.txt
