# Assertions, try-except-else, try-finally, raise, throw

# ----ASSERTIONS----

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(450)))
# print(KelvinToFahrenheit(-5))  # throws an AssertionError (raise-if-not)

# ----TRY-EXCEPT-ELSE----

"""
try:
    fd = open('file1.txt', 'r')
    fd.write('Python test\n')
except IOError:
    print("Error: can\'t find file or write data")
else:
    print("Data written to the file successfully")
    fd.close()
"""  # throws an IOError because file is open in read mode, no permission to write data


# ----TRY-FINALLY----

"""
try:
    fd2 = open('file1.txt', 'r')
    try:
        fd2.write('Test py string')
    finally:
        print("Going to close the file")
        fd2.close()
except IOError:
    print("Error: can\'t find or read data")
"""  # same as above, but file stream is closed as finally block is always executed

# ----EXCEPT WITH PARAMETER----

"""
def convertFloatToInteger(val):
    try:
        return int(val)
    except ValueError as Argument:
        print(f"Argument doesn't contain number! Try again.\n--> {Argument}")


floatingNum = 4.5
integerNum = convertFloatToInteger(floatingNum)
print(integerNum)  # 4
convertFloatToInteger("randtext")  # invalid literal for int() with base 10: 'randtext'
"""
# ----USER-GENERATED EXCEPTIONS----

"""
def game_progress(level):
    if level < 1:
        raise NameError("Invalid level!")
    print(f"Game progress: Level {level}")
    return


try:
    print("Game start...")
    game_progress(0)  # will throw a NameError from the function
except NameError as ne:
    print(f"An error occured with fetching game data.\n---> {ne}")
else:
    print("Level loaded successfully")
"""

# ----INHERITANCE OF BUILT-IN EXCEPTION CLASSES----


class NetworkError(RuntimeError):
    def __int__(self, args):
        self.args = args

try:
    raise NetworkError(['first issue', 'second issue', 'third issue'])
except NetworkError as e:
    print(f"Network issue: ---> {e.args}")

