# from random import random

# val = int(random()*10)
# print(val)

# if (val < 5):
#     print("Tail")
# else:
#     print("HEAD")

# def upperCase (st) :
#     caps = ''

#     for i in st:
#         caps += chr(ord(i) - 32)
    
#     return caps

# print(upperCase("mango"))

# def f(x):
#     def g(y):
#         return x + y
#     return g

# a = f(2)
# b = f(3)
# print(a(1) + b(1))


# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print ("None")
# print (fizzbuzz(5))

def function1(numbers):
    return [number ** 2 for number in numbers]

# print(function1(2,3,4))

def bar(a, b):
    return a + b, a * b

x, y = bar(3, 4)
# print(x, y)

def f(x):
    return x + 1

def g(x):
    return x * 2

def h(x):
    return x - 3

x = 2
# print(h(g(f(x))))

def f(x):
    try:
        return int(x)
    except ValueError:
        return 'invalid'

print(f('123'))
print(f('abc'))