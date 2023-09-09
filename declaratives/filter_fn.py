# filter(

list1 = list(range(-5, 5))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list2 = list(filter(lambda x: x < 0, list1))
print(list2)  # [-5, -4, -3, -2, -1]

list3 = ["str", "two", "strThree", "four"]
list4 = list(filter(lambda x: x == "str", list3))
print(list4)  # ['str']
