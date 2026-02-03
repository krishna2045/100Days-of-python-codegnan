'''file=open("demo1.txt",mode="w")
c=file.write("welcome to codegnan")
file.close()'''
#using append mode over come the write mode issue
file=open("demo1.txt",mode="a")
c=file.write("  welcome to python programming")
file.close()