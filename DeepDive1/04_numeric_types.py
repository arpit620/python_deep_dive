import sys
from math import isclose
import string

help(string)


"""
Comparison Operators:

Identity Operator: is, is not : compare memory address , any type
Value comparison : ==, != : compares value, different types OK, value must be compatible
Ordering comparison: <, <=, > , >= : Doesn't work for all types
Membership Operations: in , not in : used with iterables items

"""

################################################################


# help(sys)
a = 2
b = 1
# equivalent to: if b = 0 , then 0 else a/b
print(b and a/b)

"""
Boolean:
Single ton object
True : 1
False : 0

Every object has True value, except:
- None
- False
- 0 
- Empty ( list, tuple, dict, string)
- custom class method __bool__, __len__ that returns False or 0
"""

print(issubclass(bool, int))

print("...")
#$end

################################################################


"""
General concept:
n = d * (n // d) + (n % d)
"""


"""
Decimals are used (instead of Float) for banking like transactions,
where we want exact transactions.
Decimals have a lot more memory footprint than float.
"""

################################################################



# Round function
# rounds to the nearest value, with ties round to the nearest value with 
# an even significant digit
print(round(1.25,1))
print(round(1.35,1))
print(round(1.45,1))
print(round(1.55,1))

print(round(5,-1))
print(round(15,-1))
print(round(25,-1))
print(round(35,-1))
print(round(45,-1))
print(round(55,-1))

# Rounding away from zero
def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))

# $end

################################################################

# Float

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)

print('0.1 --> {0:.25f}'.format(0.1))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))

print("{:.25f}".format(1/10))

x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)
print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))


x = 0.1 + 0.1 + 0.1
y = 0.3
print(round(x, 5) == round(y, 5))

print("IsClose")
x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))

x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01))

print(isclose(x, y, abs_tol=0.0001, rel_tol=0))

x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))

a = 5
print(sys.getsizeof(a))
print("End........")