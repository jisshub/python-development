# python files write method

# a  - append in to  file
# w - write/overwrite the contents
with open("./contents.txt", "a") as fw:
    # fw.write("overwritten the contents_ver2")
    fw.write("\noverwritten the contents_ver2")
    fw.write("\noverwritten the contents_ver2")

    with open("./contents.txt", "r") as fw:
        print(fw.read(), end="")
