# Integer to another type conversions:
# int---->float
a = 10
print(float(a))  # Output: 10.0
# int---->complex
print(complex(a))  # Output: (10+0j)
# int---->str
print(str(a))  # Output: '10'
# int---->bool
print(bool(0))  # Output: False
print(bool(5))  # Output: True
# int---->list
print(list(str(a)))  # Output: ['1', '0']
# int---->tuple
print(tuple(str(a)))  # Output: ('1', '0')
# int---->set
print(set(str(a)))  # Output: {'0', '1'}
# Float to another type conversions:
b = 10.5
# float---->int
print(int(b))  # Output: 10
# float---->complex
print(complex(b))  # Output: (10.5+0j)
# float---->str
print(str(b))  # Output: '10.5'
# float---->bool
print(bool(1))  # Output: True
print(bool(0))  # Output: False
# float---->list
print(list(str(b)))  # Output: ['1', '0', '.', '5']
# float---->tuple
print(tuple(str(b)))  # Output: ('1', '0', '.', '5')
# float---->set
print(set(str(b)))  # Output: {'.', '0', '1', '5'}
# string to another type conversions:
c = "123"
# str---->int
print(int(c))  # Output: 123
# str---->float
print(float(c))  # Output: 123.0
# str---->complex
print(complex(c)) # Output: (123+0j)
# str---->bool
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
# str---->list
print(list(c))  # Output: ['1', '2', '3']
# str---->tuple
print(tuple(c))  # Output: ('1', '2', '3')
# str---->set
print(set(c))  # Output: {'1', '2', '3'}
# Boolean:
bool(1)  # True
bool(0)  # False
bool("Hello")  # True
bool("")  # False
bool([-11])  # True
bool([])  # False
bool([True])  # True
bool([False])  # True
bool({1, 2, 3})  # True
bool(set())  # False
bool((1, 2))  # True
bool(())  # False
# list to other type conversions:
L= [1, 2, 3]
# list---->str
print(str(L))  # Output: '[1, 2, 3]'
print(tuple(L))  # Output: (1, 2, 3)
# list---->set
print(set(L))  # Output: {1, 2, 3}
# Tuple to other type conversions:
t= (4, 5, 6)
# tuple---->str
print(str(t))  # Output: '(4, 5, 6)'
# tuple---->list
print(list(t))  # Output: [4, 5, 6]
# tuple---->set
print(set(t))  # Output: {4, 5, 6}
# Set to other type conversions:
s= {7, 8, 9}
# set---->str
print(str(s))  # Output: '{8, 9, 7}'
# set---->list
print(list(s))  # Output: [8, 9, 7]
# set---->tuple
print(tuple(s))  # Output: (8, 9, 7)

#String---doesn't convert into float values to int directly
a="99.88"
print(int(float(a)))  # Output: 99