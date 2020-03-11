# python files write method

# a  - append in to  file
# w - write/overwrite the contents
with open("./contents.txt", "a") as fw:
    # fw.write("overwritten the contents_ver2")
    fw.write("\noverwritten the contents_ver2")
    fw.write("\noverwritten the contents_ver2")

    with open("./contents.txt", "r") as fw:
        print(fw.read(), end="")


# creating a new file and writing to it
with open("./extra_files/hello.txt", "w") as fe:
    fe.write("writing to a new file")

with open("./extra_files/hello.txt", "r") as fe:
    cont = fe.read()
    print(cont, end="")
