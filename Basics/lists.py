# Lists, Tuples

list1 = ['dog', 'cat', 'computer', 1973, 1991, 12.5]

print(len(list1))  # 6
print(list1[1:4])  # ['cat', 'computer', 1973] (end param not included)
print(list1[-2])  # 1991 (backwards)

# Concat and Repeat
print([1, 2] + [3, 4])  # [1, 2, 3, 4] (concat)
print(['PI'] * 3)  # ['PI', 'PI', 'PI']

# Membership
print(1991 in list1)  # True
print(15 not in list1)  # True

# Methods
list1 = [10, 4, 16, 61]
print(max(list1), min(list1))  # 61 4

list1 = [123, 'abc']

list1.append(2001)  # [123, 'abc', 2001]

list1.append(123)
print(list1. count(123))  # 2 (counts occurence)

list1.extend(['sec1', 'sec2'])
print(list1)  # [123, 'abc', 2001, 123, 'sec1', 'sec2']

print(list1.index('abc'))  # 1

list1.remove(123); print(list1)  # ['abc', 2001, 123, 'sec1', 'sec2']
list1.insert(2, 'bag'); print(list1)  # ['abc', 2001, 'bag', 123, 'sec1', 'sec2']

print(list1.pop(), list1.pop(2))  # sec2 123

list1 = [1, 2, 3]; list1.reverse(); print(list1)  # [3, 2, 1]

list1 = ['xyz', 'abc', 'xyz']; list1.sort(); print(list1)  # ['abc', 'xyz', 'xyz']

# Tuples (READ-ONLY lists)
tuple1 = (12, 15)

# tuple1[1] = 50 (not possible)

tuple2 = tuple1 + (13, 11); print(tuple2)  # (12, 15, 13, 11) (concat can be done)


