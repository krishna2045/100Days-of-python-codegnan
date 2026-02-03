with open ("file.txt", mode="w+") as fd:
    print(fd.tell())
    c=fd.write("hello world")
    print(fd.read())
    print(fd.tell())