# Decorators, Operators Overlap, Data Protection (Encapsulation)

# ----OPERATORS OVERLAP----

# __init__, __del__,
# __str__ (printable string representation) __repr__ (string representation, str contains it), __cmp__ (object compare)

class PrintText:
    def __str__(self): return 'foo'


print(str(PrintText()))  # foo
print(repr(PrintText()))  # <__main__.PrintText object at 0x0000017FF5B5EFD0>


class PrintText2:
    def __repr__(self): return 'foo'


print(repr(PrintText2()))  # foo
print(str(PrintText2()))  # foo

# ----OVERLAP EXAMPLE 2----


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(4, 10)
v2 = Vector(6, -4)
print(v1 + v2)  # Vector(10, 6) --> str is implicitly presented by print, while add is with '+'

# ----DATA PROTECTION (ENCAPSULATION)----


class Counter:
    """Simple counter with ticking function."""
    __count = 0

    def tick(self):
        self.__count += 1
        print(self.__count)


counter = Counter()
counter.tick()  # 1
counter.tick()  # 2
# print(counter.__count)  # AttributeError not finding attribute, cannot access private property


