# python files
with open("./contents.txt", "r") as file:
    # print(file.read())

    # readingeach line at a time
    # use end attribute to remove unwanted lines
    # f_cont = file.readline()
    # print(f_cont, end="")
    # f_cont = file.readline()
    # print(f_cont, end="")

    # iterating over contents
    # for eachLine in file:
    #     print(eachLine, end="")
    #     print(len(eachLine))

    # reading cntents based on length
    f_cont = file.read(10)
    print(f_cont, end="")
    # here v read the first 10 characters in the file

