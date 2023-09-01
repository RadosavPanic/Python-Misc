# Regular Expressions

import re

sentence1 = "These kinds of things are very interesting"

# re.match

matchObj = re.match(r'(.*) are (.*?) .*', sentence1, re.M | re.I)

if matchObj:
    print(matchObj.group())  # These kinds of things are very interesting
    print(matchObj.group(1))  # These kinds of things
    print(matchObj.group(2))  # very
else:
    print('No matching!')

# re.search

sentence2 = "Cats are smarter than dogs"

match = re.match(r'dogs', sentence2, re.M | re.I)

if match:
    print(match.group())
else:
    print("No match!")

search = re.search(r'dogs', sentence2, re.M | re.I)

if search:
    print(search.group())
else:
    print("Nothing found in search!")

# re.sub (substitution of matches)

phone = "2004-959-559 # this is a number"
number = re.sub(r"#.*$", "", phone)  # remove python comments
print(number)
number = re.sub(r"\D", "", phone)  # remove everything other than digits
print(number)




