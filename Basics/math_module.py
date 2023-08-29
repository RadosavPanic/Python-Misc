import math

print(abs(-45), math.fabs(-45))  # 45 45.0
print(max(50, 12, 70), min(5, 2, 4))  # 45 70 2
print(pow(5, 3), math.pow(5, 3))  # 125 125.0
print(round(12.567, 1))  # 12.6

print(math.ceil(5.2), math.floor(5.2))  # 6 5
print(math.exp(5))  # 148.4131591025766 (e^x)
print(math.log2(10), math.log10(10), math.log(10, 5))  # 3.3219280948873626 1.0 1.4306765580733933
print(math.modf(95.6))  # (0.5999999999999943, 95.0)
