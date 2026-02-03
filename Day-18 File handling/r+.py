with open ("sample.txt", mode="r+") as fd:
    print(fd.tell())
    print(fd.read())
    print(fd.tell())