#LOOPING STATEMENT:1)for-loop &2)While-loop
#1.For-Loop:for iteratable in iterator:
#EX:
'''
for num in [1,2,5,7,8]:
    print(num)
'''
'''
for i in "codegnan":
    print(i)
'''
#Check which one is +ve or -ve in a list of numbers
'''
lst=[2,4,-3,5,-6,-7,9]
for num in lst:
    if num>=0:
        print(num,"is positive")
    else:
        print(num,"is negative")
print("program done")
'''
#List of number is which one is Even or Odd
'''
lst=[2,5,6,7,8,11,9]
for num in lst:
    if num%2==0:
        print(num,"Even")
    else:
        print(num,"odd")
print("Program Done!")

'''
#Range(Start,End,step)-(OR)-(Start,Stop,Skip)
'''
for i in range(10):
    print(i)
'''
'''
for i in range(2,10):
    print(i)
'''
'''
for i in range(5,15,3):
    print(i)
'''
#Print 1 to 20 number using range functions.
'''
for num in range(1,21,1):
    print(num)
'''
#print even number in b/w 0-20 using range fn
'''
for num in  range(0,21,2):
    print(num,end=" ")
'''
#Odd number b/w 0-20 using range fn
'''
for num in range(1,21,2):
    print(num,end=" ")
'''
#set
for i in{2,3,5,7,5,3,40}:
    print(i)









