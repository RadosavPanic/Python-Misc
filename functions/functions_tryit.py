# Functions, Lambda, Arguments (required, keyword, default)
# REQUIRED Arguments
def fn_required(arg1):
    """Required argument as arg1"""
    print(arg1)
    return


fn_required("This is required argument function")
# fn1()  # error missing positional argument

# KEYWORD Arguments


def fn_keyword(name, age):
    """Keyword argument function."""
    print(f"Name: {name}, age: {age}")
    return


fn_keyword(age=31, name="john")  # Name: john, age: 31
fn_keyword(age=20, name="")  # Name: , age: 20

# DEFAULT Arguments


def fn_default(name, job="Programmer"):
    """Default argument function."""
    print(f"Employee: {name}, job: {job}")
    return


fn_default("Mark")  # Employee: Mark, job: Programmer
fn_default("Dan", "Data Analyst")  # Employee: Dan, job: Data Analyst


# VARIABLE-LENGTH Arguments

def fn_var_length(*args_tuple):
    """Function with arbitrary number of arguments which forms a tuple."""
    for args in args_tuple:
        print(args, end=" ")
    return


fn_var_length(100, 540, 'f', ['docs', 'test'])  # 100 540 f ['docs', 'test']

# LAMBDA (Anonymous) Functions

sumTwo = lambda arg1, arg2: arg1 + arg2

print(f"\nSum two: {sumTwo(50, 130)}")




