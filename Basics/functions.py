# Functions, Lambda, Arguments (required, keyword, default)

def convertTextDashed(str):
    """Converts and returns text spaces to dashed symbols for a passed string argument."""  # function_docstring
    replacedString = str.replace(' ', '-')
    return replacedString


str1 = "Python is a popular programming language"
str2 = convertTextDashed(str1)
print(str2)  # Python-is-a-popular-programming-language


def appendItems(listToUpdate, items):
    """Appends individual item or a list to an existing list passed as an argument."""
    return listToUpdate.append(items)


list1 = [1, 2, 3]
appendItems(list1, [16, 22, 5])
print(list1)  # [1, 2, 3, [16, 22, 5]]


def flatList(listToFlat):
    """Iterates through elements as well as iterating through list types to attain individual values.
    Returns flatted list."""
    flattedList = []
    for element in listToFlat:
        if type(element) is list:  # loop through list element to get individual values
            for item in element:
                flattedList.append(item)
        else:
            flattedList.append(element)
    return flattedList


list_flatted = flatList(list1)  # list1 = [1, 2, 3, [16, 22, 5]]
print(list_flatted)  # [1, 2, 3, 16, 22, 5]



