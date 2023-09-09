# map(function, sequence)

items = [1, 2, 3, 4, 5]


def squareX(x):
    return x ** 2


squaredList = list(map(squareX, items))
print(squaredList)  # [1, 4, 9, 16, 25]

instantSquaredList = list(map(lambda x: x**2, items))
print(instantSquaredList)  # [1, 4, 9, 16, 25]

# list of functions using in a sequence


def square(x):
    return x**2


def cube(x):
    return x**3


funcs = [square, cube]

resultList = []
for number in range(6):
    value = list(map(lambda x: x(number), funcs))
    resultList.append(value)

print(resultList)  # [[0, 0], [1, 1], [4, 8], [9, 27], [16, 64], [25, 125]]

squaredResultsList = list(map(pow, [2, 3, 4], [10, 11, 12]))
print(squaredResultsList)  # [1024, 177147, 16777216]

# making tuples

list1, list2 = [1, 2, 3], [1, 4, 9]
def totuple(*x): return x


newTuple = list(map(totuple, list1, list2))
print(newTuple)  # [(1, 1), (2, 4), (3, 9)]
