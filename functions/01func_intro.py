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

print(generate_even())