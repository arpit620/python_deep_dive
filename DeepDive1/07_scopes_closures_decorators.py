

"""
Single Dispatch = Overloading as in other languages
which means depending no type of arguments function call might change

"""

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

##################################################

# Decorator class 

# Applications

# Monkey patch
# Add method to existing object/classes

# Debug / create logs


from fractions import Fraction
def dec_speak(cls):
    cls.speak = lambda self: 'This is a very late parrot.'
    return cls


Fraction = dec_speak(Fraction)
f = Fraction(10, 2)
print(f.speak())


#####

from datetime import datetime, timezone

def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    
    if vars(self):
        for k, v in vars(self).items():
            results.append('{0}: {1}'.format(k, v))
    
    # we have not covered lists, the extend method and generators,
    # but note that a more Pythonic way to do this would be:
    #if vars(self):
    #    results.extend('{0}: {1}'.format(k, v) 
    #                   for k, v in vars(self).items())
        
        return results


def debug_info(cls):
    cls.debug = info    
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def say_hi():
        return 'Hello there!'


p1 = Person('John', 1939)
print(p1.debug())



@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0
    
    @property
    def speed(self):
        return self.current_speed
    
    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed

s = Automobile('Ford', 'Model T', 1908, 45)
print(s.debug())


"""
from functools import total_ordering

# Above create dunder functions from equality and less than for other 
comparison dunder methods
"""



#$end

###################################################################

# Decorator class

# Decorator factory example
def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print('hello {0}'.format(s))

print(my_func('world'))


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func(s):
    print('Hello {0}!'.format(s))

@MyClass(b=10, a=20)
def my_func2(s):
    print('Hello {0}!'.format(s))

my_func('Python')
my_func2('Python2')


# $end

##################

# Decorators with parameters

from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)

def fib(n):
    return calc_fib_recurse(n)


@timed(5)
def fib(n):
    return calc_fib_recurse(n)


fib(30)

# $end

##################



"""

# Memoization:

# Use decorators to create cache and remember the results.
# Creates a dictionary for 
(args) -> results for that call

LRU Cache: Least recently used
Keeps a limit on memory usage.

function.__wrapped__
Above will always call the actual function and not the memoized one
https://www.youtube.com/watch?v=K0Q5twtYxWY

"""
from functools import wraps
def memoize(fn):
    cache = dict()
    
    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    
    return inner


@memoize
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(6)
fib(7)

from functools import lru_cache

@lru_cache()
def fact(n):
    print("Calculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)

print(fact(5))
print(fact(4))

# $end

######################################

# Decorators

"""

We can have Classes or Decorators for the same kind of functionality.



# Application 1
Timer decorator: Calculates how much time the function takes to run

Finbonacci: Three methods:
- Recursion
- Loop
- Reduce method

# Application 2
Logger: Logs function time, parameters and other stuff.
Stacked Decorators: Have multiple decorators.

# CHeck if stacked decorators runs the function multiple times?




"""


# $end

######################################


# Closures

"""
You can think of closures as a function plus an extended scope that
contains the free variables.
"""


# Application 2
# Get count of how many times a fn was called

def add(a, b):
    return a + b

def mult(a, b, c):
    return a * b * c

counters = dict()

def counter(fn, counters):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is nonlocal
        return fn(*args, **kwargs)
    
    return inner

func_counters = dict()
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)




# Application 1
# Get timer

from time import perf_counter
class Timer:
    def __init__(self):
        self._start = perf_counter()
    
    def __call__(self):
        return (perf_counter() - self._start)

a = Timer()
print(a())
print(a())

# Using Closures

def timer():
    start = perf_counter()
    
    def elapsed():
        # we don't even need to make start nonlocal 
        # since we are only reading it
        return perf_counter() - start
    
    return elapsed


x = timer()
print(x())
print(x())
print(x())

# $end

######################################################

def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
    inner()
    print(x)

outer()

# $end

######################################################

# print(True)
"""
print(True)
python first try to find print and True in local scope.
If not found, then it will look in built-in python modules.

local -> global -> built-in

"""

a = 0

# a not found in local scope so checks in global scope
def func():
    print(a)

func()

a = 0

# have access to only local variable
def func():
    a = 100 
    print(a)

func()
print(a)

###

a = 0

# Modifies global variable
def func():
    global a
    a = 100 
    print(a)

func()
print(a)

####

a = [1,2,3]

# If global variable is mutable, we dont' want to declare it as global
def func2():
    a.append(4)

func2()
print(a)


print("End")
