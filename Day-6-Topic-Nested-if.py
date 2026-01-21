#Nested-if
#Check +Even,-Even and +Odd,-Odd
'''
num=int(input("enter a number:"))
if num%2==0:
    if num>-1:
        print("+ve Even")
    else:
        print("-ve Even")
else:
    if num>-1:
        print("+ve Odd")
    else:
        print("-ve Odd")
'''
#Check positive number and Even/Odd

'''
num=int(input("enter a number:"))
if num>0:
    if num%2==0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Number is Zero or Negative")
'''
#Student Pass with Distinction
'''
marks=int(input("Enter a number:"))
if marks>=35:
    if marks>=75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")

'''
