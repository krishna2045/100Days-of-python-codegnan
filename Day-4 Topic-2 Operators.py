#OPERATORS:
#Arithmetic operator:+,-,*,/,%,//,**
#Simple-Calculator program:
# a=10
# b=20
# addition=a+b
# subraction=b-a
# multiplication=a*b
# division=b/a
# floordivision=b//a
# modules=b%a
# exponent=b**a
# print("sum of two numbers:",addition)
# print("sub of two numbers:",subraction)
# print("multiple of two numbers:",multiplication)
# print("divisible of two numbers:",division)
# print("floordivision of two numbers:",floordivision)
# print("modules of two numbers:",modules)
# print("exponent:",exponent)

# 2.Comparison/Relational Operators:==,!=,>,<,>=,<=
# a=10
# b=18
# print(a==b)  #False
# print(a!=b)  #True
# print(a>b)   #False
# print(a<b)   #True
# print(a>=b)  #False
# print(a<=b)  #True

# 3.Logical Operators: and,or,not

#AND:
# a=False
# b=True
# print(a and a)
# print(a and b)
# print(b and a)
# print(b and b)

#OR:
# print(a or a)
# print(a or b)
# print(b or a)
# print(b or b)

#NOT:
# print(not a)
# print(not b)
# print(not True)
# print(not False)
a=10
b=20
c=30
# print((a<b) and (b<c))  #True
# print((a<b) or (b>c))   #True
# print(not(a<b))         #False
# print(not(b>c))         #True
# print((a>b) and (b<c or c>b))  #False

# 4.Bitwise Operators: &,|,^,~,>>,<<
# a=10  # 1010
# b=4   # 0100
# AND(&):
# print(a & b)  # 0000 =>0
# OR(|):
# print(a | b)  # 1110 =>14
# XOR(^):
# print(a ^ b)  # 1110 =>14
# NOT(~):
# print(~a)     # -(a+1) =>-11
# print(~b)     # -(b+1) =>-5
# LEFT SHIFT(<<):
# print(a << 2) # 101000 =>40
# print(b << 2) # 10000 =>16
# RIGHT SHIFT(>>):
# print(a >> 2) # 0010 =>2
# print(b >> 2) # 0001 =>1

# 5.Assignment Operators:=,+=,-=,*=,/=,//=,%=,**=
# x=10
# x+=5  # x=x+5
# print(x)  #15

# x-=3 # x=x-3
# print(x)  #7

# x*=2 # x=x*2
# print(x)  #20

# x/=2 # x=x/2
# print(x)  #10.0

# x//=2 # x=x//2
# print(x)  #5

# x**=3 # x=x**3
# print(x)  #1000

# x%=3 # x=x%3
# print(x)  #1

# 6.Membership Operators: in, not in
# a="Hello World"
# print('H' in a)        #True
# print('Hello' not in a) #False
# print('W' in a)    #True
# print('world' not in a) #True

# 7.Identity Operators: is, is not
# a=10
# b=10
# print(a is b)      #True
# print(a is not b)  #False

# x=[1,2,3]
# y=[1,2,3]
# print(x is y)      #False

# print(x is not y)  #True
