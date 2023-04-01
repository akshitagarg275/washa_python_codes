'''
DRY -> Don't Repeat Yourself
functions:

We simply wrap a certain set of code inside a function
which we can excute any no of times.

def function_name ():
    //function statements

A function will not get executed until and unless it is called.

Staic function -> A function whose output will remain always same, no 
matter when it is called.
'''

# print("Hello," , "john")
# print("Hello,", "Akshita")
# print("Hello")
# print("Hello")
# print("Hello")

# function declaration
# This greet function is a static function
def greet():
    print("Hello")


# calling
# greet()

# print("Kuch aur code hai....")

# greet()

def say_hello (uname) :
    print("Hello,", uname)

# uname = input("Enter youe username: ")
# say_hello(uname)

# name = "Jane"
# say_hello(name)


# sing function
def sing():
    msg = '''Happy Birth Day to you
    Happy Birth Day to you
    Happy Birth Day to Dear you
    Happy Birth Day to you
    '''
    print(msg)

# sing()

# lst = [2,5,6,7]

# length = len(lst)
# print(length)
# print(len(lst))

def add(a , b):
    # print(a + b)
    return a+b

# res = add(5,6)
# print(res)

# print(add(1,2))


def square_num (num) :
    sq = num * num
    return sq
    print("Heghj")

# n = int(input("Enter a num : "))

# res = square_num(n)
# print(res)

def check_even (num):
    # print(num % 2 == 0)
    return num % 2 == 0

# res = check_even(4)

# if res:
#     print("Num is even")
# else:
#     print("Num is odd")


# generating even nums b/w 1-50

def generate_even():
    even = []
    for num in range(1,50):
        if num % 2 == 0:
            even.append(num)
    
    return even

# print(generate_even())

# TODO: Default parameters
# def profile(name ="NA" , age = "NA"):
#     print(f"Hi, {name}. Your age is {age}")

# NOTE: non-default arguments do not follow default arguments
# first : non-default
# second : default arguments
def profile(name , age = "NA"):
    print(f"Hi, {name}. Your age is {age}")

# profile("John")
# profile("Jane" , 12)
# profile("Rahul")


# TODO: Positional arguments

# def profile(name, age):
#     print(f"Hi, {name}. Your age is {age}")

# profile(age= 13 , name="john")


# TODO: variable length arguments

# def func (a, b, *args):
#     print("a is :",a)
#     print("b is :",b)
#     print(args)
#     print(type(args))

# func(1,2,3,4,5,6)
# func(44,34)

# def sumOfAll(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i

#     return sum

# res = sumOfAll(1,2,3,4,5,6)
# res = sumOfAll(1)
# print(res)

# TODO: variable length keyword arguments

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# func(name = "John" , age = "20")

def profile(**kwargs):

    for k,v in kwargs.items():
        print(f"key is {k} and value is {v}")
    

# profile(name = "John" , age = "20")


# TODO: anonymous function / lambda function
#  variable_name = lambda parameters : expression

def add(a , b):
    return a+b


# lambda_add = lambda a ,b : a+b

# print(lambda_add(2,3))

def square_num (num) :
    sq = num * num
    return sq


sq_lambda = lambda num : num * num
# print(sq_lambda(5))


# TODO: Applications of lambda functions

# TODO: map -> It creates a new list from the exisiting one on the basis of certain computation
lst = [1,2,3,4,5]

# sq_lst = list(map(lambda num : num**2, lst))
# print(sq_lst)

# TODO: filter

even = list(filter(lambda num : num % 2 ==0 , lst))
odd = list(filter(lambda num : num % 2 !=0 , lst))
# print(even)
# print(odd)

# TODO: reduce
from functools import reduce

add = reduce(lambda a,b : a+b , lst)
print(add)
