from functools import reduce
import operator

res = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(res)  # 24

seq1 = ["Testing", "shows", "the", "presence", "not", "the", "absence", "of", "bugs"]
reducedSeq = reduce(lambda x, y: x + y + " ", seq1)
print(reducedSeq)  # Testingshows the presence not the absence of bugs

print(reduce(operator.add, seq1))  # Testingshowsthepresencenottheabsenceofbugs



