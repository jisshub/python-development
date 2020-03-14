# files in python

myFile = open("./iterators.py", "r")
for line in myFile.read():
    print(line)

myFile.close()

# using context managers - with statements
with open("iterators.py", "r") as file1:
    print(file1.read())

#     no need to close the manually it automatically close the files
# also close the file if exceptions r thrown
# file1.close()
# throw the error,
try:
    print(file1.read())
except Exception as e:
    print(e.args)
finally:
    print("Exc")
