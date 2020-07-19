# try:
#    fh = open("testfile", "w")
#    try:
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print("Going to close the file")
#       fh.close()
# except IOError:
#    print("Error: can\'t find file or read data")
# x=-1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print(sys.exc_info())
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)