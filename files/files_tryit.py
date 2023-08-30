# FILE I/O, Modules

# ----INPUT----

"""
jobInput = input("Enter your current job title: ")
print(jobInput)  # Software Engineer (received input result)

strI = input("Insert equation: ")
listI = eval(strI)  # inserted: [x*5 for x in range(2,10,2)]
print(listI)  # received: [10, 20, 30, 40]
"""

# ----WRITE----

"""
fd = open('file1.txt', 'a+')
fd.write("Python is great!\n")

print(f"File name: {fd.name}\nFile Stream closed: {fd.closed}\nFile mode:{fd.mode}")

fd.close()
"""

# ----READ & OFFSET CHANGE----

"""
fd2 = open('file1.txt', 'r')
textRead = fd2.read(10)
print(textRead)  # Python is

print(fd2.tell())  # offset (current position in file)

fd2.seek(2)  
# changes to position, seek(offset [,from]) -> from defines from where offset starts, 0=start, 1=cur_pos, 2=endOfFile
textRead = fd2.read(10)
print(textRead)  # thon is gr

fd2.close()
"""
