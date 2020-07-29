

"""
Python keeps a cache for [-5, 256] numbers.
Anything outside that will create a new memory address

For strings it keeps single word in cache. 
Anything with space in it goes in new memory.
use sys.intern in case of string memory optimization.

Sets are faster to search in as compared to lists and tuples

Peephole:
python pre computes the variables in fn/ classes and stores it beforehand.

"""

import string
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)

########################################################


# Memory comparison
# Variable Equality

# is / is not : compares the memory address
# == / !- : compares data value

# Everything is an object

########################################################

a = [1,2,3]
b = a

print(a)
b.append(100)
print(a)


#$end

########################################################


# List is a mutable object
def process(lst):
    lst.append(100)

a = [1,2,3]
print(a)
process(a)
print(a)


"""
Immutable objects:
Numbers (int, float, boolean)
String
Tuples
Frozen sets
User Defined Classes

Mutable:
List 
Dictionaries
Sets
User Defined Classes
"""

# $end

########################################################


# v1 is not equal to 10
# v1 is a reference to a memory address which have the value 10
v1 = 10
print(id(v1))
print(hex(id(v1)))
print("End..")


v2 = v1
print(id(v2))

v1 = 8
print(id(v1))

# Reference Counting
# When nothing is pointing to specific address, python memory manager
# throws that away.

# Garbage collector handles the memory leak in case we have 
# circular referencing


# Statically typed langauge
# String myVar = "Hello"

# Dyncamically Typed
# myVar = "hello"
# myVar = 10

print(type(v1))


