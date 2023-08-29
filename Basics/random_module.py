import random

print(random.choice([1, 5, 9, 12]))  # 5 (random choice)
print(random.randrange(100, 200, 2))  # 134 (start, end, step)
print(random.random())  # 0.8552123630896281 (random number between 0 and 1)

random.seed(10)
print(random.random())  # 0.5714025946899135 (random number with seed of 10)

randomList = [5, 20, 10, 13]
random.shuffle(randomList)
print(randomList)  # [10, 5, 20, 13]

print(random.uniform(32, 60))  # 37.77075049990605 (random float number)
