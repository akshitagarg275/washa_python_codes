'''
recursion -> self calling method/function

bigger problem -> we try to break it into simpler problem and find a solution for it

base condition
simpler problem solution

'''

# WAP to find sum of nums
# iterative approach

def sum_of_num (num):
    sum = 0
    for i in range(1 , num+1):
        sum += i
    return sum

# print(sum_of_num(5))

'''
# recursive approach
sum(num) = num + sum(num-1)
sum(5) = 5 + sum(4)
sum(4) = 4 + sum(3)
sum(3) = 3 + sum(2)
sum(2) = 2 + sum(1)
sum(1) = 1 #base condition

'''

# def sum_rec (num):
#     # base condition
#     if num == 1:
#         return num #1
    
#     return num + sum_rec(num - 1)

# print(sum_rec(5))


# factorial
# 5 = > 5*4*3*2*1 = 120

'''
# recursive approach
sum(num) = num * sum(num-1)
sum(5) = 5 * sum(4)
sum(4) = 4 * sum(3)
sum(3) = 3 * sum(2)
sum(2) = 2 * sum(1)
sum(1) = 1 #base condition

'''

def fact (num):
    # base condition
    if num == 1:
        return num #1
    
    return num * fact(num - 1)

# print(fact(5))

# fibonacci series
# 0 1 1 2 3 5 8 13

def fib_rec(num):
    # base condition
    if num == 0 or num == 1:
        return num
    
    return fib_rec(num - 1 ) + fib_rec(num-2)

print(fib_rec(6))