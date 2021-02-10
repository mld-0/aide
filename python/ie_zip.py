#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import itertools
#   {{{2
#   LINK: https://realpython.com/python-zip-function/

#   zip(*iterables)
#       Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)
print(type(zipped))
print(list(zipped))
print()

#   Using unordered sequences, such as sets, with zip, can produce results of random order
s1 = {1, 2, 3}
s2 = {'a', 'b', 'c'}
print(list(zip(s1, s2)))
print()

#   using next() to force the empty iterator to yield an element produces a StopIteration exception
zipped = zip()
try:
    print(next(zipped))
except Exception as e:
    print(e)
print()

#   zip with no arguments
#       returns an empty iterator, which becomes an empty list
zipped = zip()
print(zipped)
print(list(zipped))
print()

#   zip with one argument:
#       returns an iterator that yields a series of 1-item tuples
a = [1, 2, 3]
zipped= zip(a)
print(list(zipped))
print()

#   with two or more arguments, the tuples yieled by the iterator created by zip will have the same length as number of arguments to zip
integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats) 
print(list(zipped))
print()

#   arguments of unequal length
#       The number of elements in the zipped object is equal to the length of the shortest iterable given as argument
zipped = zip(range(5), range(100))
#   note that getting the length of the iterator zipped consumes it
print(len(list(zipped)))
print()

#   itertools.zip_longest(*iterables[, fillvalue=None])
#       yields an iterator with the length of the longest iterable. Missing values are set to fillvalue (which defaults to None)
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
print()

#   zip() in python2
#       in python2, zip returns a list of tuples. That is, python2's 'zip()' is equivelent to 'list(zip())'
#       itertools.izip() in python2 is equivelent to python3's zip()

#   Iterating through multiple iterables
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print("l=(%s), n=(%s)" % (str(l), str(n)))
print()

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print("l=(%s), n=(%s), o=(%s)" % (str(l), str(n), str(o)))
print()

#   In python3.6+, dictionaries are ordered collections
#   meaning they can be iterated through in a consistent way
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print("k1=(%s), v1=(%s), k2=(%s), v2=(%s)" % (str(k1), str(v1), str(k2), str(v2)))
print()

#   inverse of zip()
#       zip(*zipped)
numbers = (1, 2, 3, 4)
letters = ('a', 'b', 'c', 'd')
zipped = zip(numbers, letters)
numbers, letters = zip(*zipped)
print(numbers)
print(letters)
print()

#   creating dictionaries with zip()
#       dict(zip(keys, values))   requires exactly 2 arguments
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
person_dict = dict(zip(fields, values))
field = ['job']
new_job = ['Python Consultant']
person_dict.update(zip(field, new_job))
print(person_dict)
print()


#   duplicating an iterator
#   LINK: https://stackoverflow.com/questions/42132731/how-to-create-a-copy-of-python-iterator
#   Use the itertools.tee() function to produce copies; these use a buffer to share results between different iterators:
#   Note that you should no longer use the original iterator; use only the tees.
my_list = [5, 4, 3,2]
first_it = iter(my_list)
first_it, second_it = itertools.tee(first_it)
print(next(first_it))   # prints 5
print(next(second_it))  # prints 5
print(next(first_it))   # prints 4


#   }}}1
