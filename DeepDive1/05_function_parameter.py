
##################################################

# Factorial Example


#Type 3
# Internal cache


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result

print(factorial(3))
print(factorial(5))


#$end

# Type 2
# Using explicit cache


def factorial(n,*, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result

cache = {}
print(factorial(3, cache=cache))
print(factorial(3, cache=cache))


# $end

# Type 1
# Normal way of writing
def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)

factorial(3)
factorial(3)

# $end

##################################################

# IF you want to force user to pass keyword argument, use:
# b is a forced keyword argument.
def fun2(a, * , b):
    pass


# Catch / Flaws / Beware - Pt2 


# Don't keep default value as a mutable object in a function parameter
def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list

# Instead do it like this
def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


##################################################

# Catch / Flaws / Beware

from datetime import datetime


def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # above is equivalent to:
    #if not dt:
    #    dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1')
log('message 2')
log('message 3', dt='2001-01-01 00:00:00')


# value of a is created at the time of func defination 
# and not at the time of fn call
def func(a=10):
    print(a)



# $end

##################################################################

import time

def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))

print(compute_powers_1(2, end=5))
print(compute_powers_2(2, end=5))
print(compute_powers_3(2, end=5))
print(list(compute_powers_3(2, end=5)))

# time_it(compute_powers_1, n=2, end=20000, rep=4)
# time_it(compute_powers_2, 2, end=20000, rep=4)
# time_it(compute_powers_3, 2, end=20000, rep=4)


# $end


##################################################################

##### Keyword arguments
# Positional arguemnts depends on position/ order of arguemnts
# Keyword args depends on key value pair. Order doesnt matter
# **kwargs : parameter name could be anything. Gives Dictionary

# CHeckout documentation of print
help(print)


# We can force no positional arguments
# * indicates the end of posiitonal arguments
def fun(*, d):
    pass



### *args

"""
1. While calling func you cannot pass more positional arguemnts after *args


"""

def func2(a,b,*args):
    print(a,b,args)

def func1(a,b,*c):
    print(a,b,c)

def func3(a,b,c):
    print(a,b,c)

func1(1,2,3,4)
func2(1,2,3,4)
l = [1,2,3, 4, 5]
func2(*l)


# $end

# Extending unpacking

# ** used for unpacking key value pair
# Can only be used on right hand side 

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}

# We are adding d2 later so key 2 would be overwritten by d2
print({**d1, **d2})

# $end

# * can be used both on LHS & RHS
l = [1, 2, 3, 4, 5, 6]
a, *b = l
a, *b, c  = l
a, *b, c, d  = l

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [*l1, *l2]





#############################################

a, b = 1,2 
a,b = (1,2)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for i in d:
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)


# $end

"""
1. Dictionary and sets are unordered types
2. No guarantee the the returned results will be in order.


"""

a = 1
b = 2

# Swapping
a,b = b,a





# Unpacking
# a,b,c = [1,2,3]
a,b,c = 10,20,30

a,b,c, = 1,2, "Hello"

for x in "Hello":
    print(x)

# $end


##################################################################

"""
1. If a positional parameter is defined with a value, every positional 
parameter afte rit must also be given default value.
2. Once you use a named arguement, all argument thereafter must also be named
3. 
"""


# While defining the function its called parameters
def func(a,b):
    return a+b


a = 2
b = 3
# While calling the function its called arguments.
func(a,b)