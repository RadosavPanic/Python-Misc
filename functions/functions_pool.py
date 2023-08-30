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


def removeListElements(list1, list2):
    """Function for removal of elements from given list2 in list1."""
    result = list(filter(lambda x: x not in list2, list1))
    return result


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print(removeListElements(list1, list2))  # [1, 3, 5, 7, 9, 10]

# Variable Scopes
Money = 2000


def AddMoney():
    """Receives a global variable from outside that can be manipulated."""
    global Money
    Money += 1


print(Money)  # 2000
AddMoney()
print(Money)  # 2001




