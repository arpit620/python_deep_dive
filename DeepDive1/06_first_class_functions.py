
# Partial Functions


from functools import partial

def my_func(a, b, c):
    print(a, b, c)

f = partial(my_func, 10)
f(20, 30)

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(4))
print(cube(3))
print()


#$end

################################


l = [5, 8, 6, 10, 9]
_max = lambda a, b: a if a > b else b
def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l))

from functools import reduce


print(reduce(lambda a, b: a if a > b else b, l))

#factorial
n=5
print(reduce(lambda a, b: a * b, range(1, n+1)))

#initializer
l = []
print(reduce(lambda x, y: x*y, l, 1))


# $end

################################

# Map , filters ,zip and list comprehensions

# map(func, *iterables)

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(4))
print(list(map(fact, [1, 2, 3, 4, 5])))


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x+y

m = map(f, l1, l2)
print(list(m))

# Filter
# filter(func, iterable)

def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))

result = filter(lambda x: x % 2 == 0, l)
print(list(result))

# zip
# zip(*iterables)

l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
print(list(zip(l1, l2)))

# List comprehension
# [<expression> for <varname> in <iterable>]

print(list(filter(lambda y: y < 25, map(lambda x: x**2, range(10)))))
print([x**2 for x in range(10) if x**2 < 25])
print()

# $end

################################
 
# Callables

print(callable(print))

class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0
    
    def __call__(self, x=1):
        self.counter += x
        print(self.counter)


my_obj = MyClass()
print(my_obj())
print(my_obj())
print(my_obj(10))

# $end

################################

# Function Introspection

def func(a,b):
    pass

func.c = "hello"
func.d = "world"

#dir returns list of valid attributes
print(dir(func))


"""
__name__: returns name of func
__defaults__: returns positional arguments
__kwdefaults__: returns kwrds args

__code__: gives a code object which further has properties
- co_varnames: parameters and local variables
- co_argcount: num of parameters

import inspect
ismethod(Obj): check if its a method
isfunction(Obj): check if its a function
isroutine(Obj): check if its either a method/ function

inspect.getsource(my_func): Gives you sourcecode
inspect.getmodule(my_func): gives module of func
inspect.getcomments(my_func): gives out all comments. Used for TODO



"""

# $end

################################################################

# sorted func with lambda

l = ['a', 'B', 'c', 'D']
print(sorted(l))
print(sorted(l, key=str.upper))
print(sorted(l, key = lambda s: s.upper()))


d = {'def': 300, 'abc': 200, 'ghi': 100}
print(d)
print(sorted(d))
print(sorted(d, key=lambda k: d[k]))

def dist(x):
    return (x.real)**2 + (x.imag)**2

l = [3+3j, 1+1j, 0]
print(sorted(l, key=dist))
print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))

import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted(l, key=lambda x: random.random()))
print(sorted('abcdefg', key = lambda x: random.random()))
print(''.join(sorted('abcdefg', key = lambda x: random.random())))


# $end

############################################################


# Lambda func

# Anonymous funcs
# lambda [parameter list]: expression
# lambda: keyword
# [parameter list]: parameters to pass, (Optional)
# expresssion : body of the func.

a = lambda x: x**2
lambda x,y : x+y
lambda: 'hello'

print(a(2))
print(a(3))

# $end

############################################################


def fact(n):
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    
    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)

# help(fact)

print(fact.__doc__)


def my_func(a:'annotation for a', 
            b:'annotation for b')->'annotation for return':
    
    return a*b

help(my_func)
print(my_func.__annotations__)


