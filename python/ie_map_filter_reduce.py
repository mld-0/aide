#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import functools
import operator
import itertools
import math
import re
#   {{{2

#   LINK: https://realpython.com/python-map-function/

#   Functional Programming
#       Combining lists, arrays, or itterables, along with a set of functions, and returning the result the list of results for each item of the list passed to the function. Consisting of:
#           Mapping         Apply transformation function to an itterable to produce a new variable
#           Filtering       list of items which cause the filter function to return false
#           Reducing        applying a reduction function to an iterable to produce a single cumulative value.

#   map(function, iterable[, iterable1, iterable2, ...])
#       loops over items of input iterable(s) and returns an iterator that results from applying a transformation function to each item in the iterable
#       'function' can be a built-in function, class, method, lambda function, or user-defined function

def func_square(number):
    return number ** 2
#   get squares of x as y 
x = range(1, 6)
#   list-compression implementation
y = [ func_square(loop_x) for loop_x in x ]
print(y)
#   sequence-generator implementation (note, the inner set of '()' are redundent)
y = list( ( func_square(loop_x) for loop_x in x ) )
print(y)
#   map implementation, returns an iterator object, from which we create a list 
y = list(map(func_square, x))
print(y)
#   map implementation with lambda
y = list(map(lambda loop_x: loop_x ** 2, x))
print(y)
print()

#   Examples uses of map, 
#       int()
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))
#       abs()
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print(abs_values)
#       len()
words = ["Welcome", "to", "Real", "Python"]
words_lower = list(map(len, words))
print(words_lower)
print()

#   multi-iterable map
#       The transformation function must take as many arguments as iterables are supplied to map()
#       If the iterables are different lengths, the shortest is used
list_a = [1, 2, 3]
list_b = [4, 5, 6, 7]
list_c = list(map(pow, list_a, list_b))
print(list_c)
list_c = list(map(lambda x,y: x**y, list_a, list_b))
print(list_c)
list_c = [ x**y for x, y in zip(list_a, list_b) ]
print(list_c)
print()

#   Example, capitalise first letter of strings in list
string_it = ["processing", "strings", "with", "map"]
string_cap_it = list(map(str.capitalize, string_it))
print(string_cap_it)

with_spaces = ["processing ", "  strings", "with   ", " map   "]
without_spaces = list(map(str.strip, with_spaces))
print(without_spaces)

with_dots = ["processing..", "...strings", "with....", "..map.."]
without_dots = list(map(lambda s: s.strip('.'), with_dots))
print(without_dots)
print()


text = """Some people, when confronted with a problem, think "I know, I'll use regular expressions." Now they have two problems. Jamie Zawinski"""
words = text.split()
func_removepunc = lambda loop_word: re.sub(r'[!?.:;,"()-]', "", loop_word)
words_nopunct = list(map(func_removepunc, words))
print(words_nopunct)
print()

#   Implementing a Caesar Cipher
def rotate_chr(c, rot_by):
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

#   itertools.repeat    utility for passing constants to map function
secret_msg = "antidisestablishmentarianism"
enc_msg = "".join(map(rotate_chr, secret_msg, itertools.repeat(3)))
print(enc_msg)
dec_msg =  "".join(map(rotate_chr, enc_msg, itertools.repeat(-3)))
print(dec_msg)
print()

#   Factorials
numbers = list(range(0, 8))
numbers_fact = list(map(math.factorial, numbers))
print(numbers_fact)
#   Fahrenheit to/from celsius
to_fahrenheit = lambda c: 9 / 5 * c + 32
to_celsius = lambda f: (f - 32) * 5 / 9
celsius_temps = [100, 40, 80]
fahr_temps = list(map(to_celsius, celsius_temps))
print(fahr_temps)
celsius_temps = list(map(to_fahrenheit, fahr_temps))
print(celsius_temps)
print()


#   filter(<func>, <iterable>)
#       loops over items of input iterable(s) and returns an iterator containing those items of the input for which the function is True

#   get positive numbers in list
is_positive = lambda x: x > 0
numbers = list(range(-5,10))
print(numbers)
numbers_positive = list(filter(is_positive, numbers))
print(numbers_positive)
print()

#   Continue: 2021-02-08T23:33:29AEDT reduce()
#   reduce(function, iterable))
#       applies function to all items in iterable and add to produce final value. function must accept two arguments and return a value

#   sum numbers [0,10]
values = range(0, 11)
values_sum = functools.reduce(operator.add, values)
print(values_sum)
values_sum = sum(values)
print(values_sum)
print()

#   itertools.starmap
#   starmap is (roughtly) equivelent to
#   def starmap(function, iterable):
#       for args in iterable:
#           yield function(*args)
from itertools import starmap
list_a = (2, 7)
list_b = (4, 3)
list_c = list(starmap(pow, [list_a, list_b]))
print(list_c)
#   note the swapped lists
list_a = (2, 4)
list_b = (7, 3)
list_c = list(map(pow, list_a, list_b))
print(list_c)

#   Generating a list with map
#       list(map(function, iterable))
#   Generating a list with a list comprehension
#       [function(x) for x in iterable]
#   Genrating a generator expresssion
#       (function(x) for x in iterable)


#   }}}1
