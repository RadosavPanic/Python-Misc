# Strings | Formatting, Methods

word = 'PythonFunCoding'

# SLICE (:) Operator
print(word[0])  # P
print(word[1:5])  # ytho (start, end not included)
print(word[:7])  # PythonF (slice end)
print(word[7:])  # unCoding (slice start)

# REPEAT and CONCAT
print('ML' * 2)  # MLML
print('ML' + ' & ' + 'DS')  # ML & DS

# FORMATTING
print('%s %s' % ('one', 'two'))  # one two
print('{} {}'.format('good', 'interpolation'))  # good interpolation
print('{1} {0}'.format('one', 'two'))  # two one (placement reversed)

print('%10s' % 'testing')  # ___testing (10 spaces reserved blank as prefix)
print('%-10s' % 'testing')  # testing___ (10 spaces with blank as sufix)
print('{:>10}'.format('testing'))  # ___testing
print('{:10}'.format('testing'))  # testing___
print('{:&>10}'.format('testing'))  # &&&testing
print('{:&<10}'.format('testing'))  # testing&&&

# MULTILINE
statement = """This is a long multiline
string where escape we characters\t like tab or newline\nworks"""

print(statement)

print(r'C:\\Program')  # C:\\Program, \r \R are raw string (no escape chars)
print('C:\\Program')  # C:\Program

# METHODS
str1 = 'python web DEV'

print(len(str1), str1.__len__())  # 14 (__len__ is internal command)
print(str1.count("e", 0, 14))  # 2 (counts occurence of specified str)

print(str1[:6].capitalize() + str1[6:11].upper() + str1[11:].lower())  # Python WEB dev
print('This'.swapcase(), 'isSOMEstring'.swapcase())  # tHIS ISsomeSTRING
print('string noncap'.title())  # String Noncap

print('string example'.center(16, '&'))  # &string example& (center string width, with both paddings)

print('string'.startswith('stri'), str1.endswith('ingl'))  # True False
print('string example'.find('ex', 3))  # 7 (returns index, -1 for not found)
print('that is is is'.rindex('is', 0))  # 11 (highest index)
print('that is is is'.index('is', 0))  # 5 (lowest index)

print("=".join(("a", "b", "c")))  # a=b=c
print("1 2 3".split(), "4 5 6".split(' ', 1))  # ['1','2','3'] ['4','5 6'] (max split integer as second arg)
print("1\n2\n\n3".splitlines())  # ['1','2','','3']
print('this is is'.replace('is', 'was'))  # thwas was was
print('this is is'.replace('is', 'was', 2))  # thwas was is

print("  firstOne".lstrip(), "88secondOne".lstrip('8'))  # firstOne, secondOne (can be empty or chars)
print('third99'.rstrip('99'))  # third
print('555string555'.strip('555'))  # string

print('example'.ljust(10, '-'), 'sec'.rjust(5, '&'))  # example--- &&sec
print('screen'.zfill(10))  # 0000screen (fills remaining with zeros from start)

print(max('really'), min('really'))  # y a
print('one ' + 'sec\tstr', 'one ' + 'sec\tstr'.expandtabs(0))  # onesec	str | one secstr (change tab length, def is 8)

print('th2'.isalnum(), 'th2'.isalpha())  # True False
print('12'.isdigit(), 'r12'.isnumeric(), '12'.isdecimal())  # True False True
print(' '.isspace())  # True
print('tt'.islower(), 'tt'.isupper(), 'Tt Tt'.istitle())  # True False True

# Fast String Format
job = 'Teacher'
print(f"Hello {job}")  # Hello Teacher

