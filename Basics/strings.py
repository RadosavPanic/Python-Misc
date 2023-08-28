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
str1 = 'string example'

print(str1[:6].capitalize() + str1[6:11].upper() + str1[11:].lower())  # String EXAMple
print(str1.count("e", 0, 14))  # 2 (counts occurence of specified str)
print(str1.center(16, '&'))  # &string example& (center string width, with both paddings)

print(str1.startswith('stri'), str1.endswith('plea'))  # True False
print(str1.find('ex', 3))  # 7 (returns index, -1 for not found)
print(len(str1), str1.__len__())  # 14 (__len__ is internal command)


