#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
#   LINK: https://realpython.com/python-sort/#when-to-use-sorted-and-when-to-use-sort

#   Sorts in python are stable

#   sorted() returns a sorted copy of the list, leaving the origional list unchanged
numbers = [6, 9, 3, 1]
print(sorted(numbers))
print(numbers)
print()

#   sort() as a method of a list modifies the list in-place and returns None
numbers = [6, 9, 3, 1]
print(numbers.sort())
print(numbers)
print()

#   sorted() is generally prefered to sort(), due to the fact it leaves the origional order inplace

#   reverse is an optional argument of sorted()
names = ['Harry', 'Suzy', 'Al', 'Mark']
print(sorted(names))
print(sorted(names, reverse=True))
print()

#   strings of identical characters are sorted by length
different_lengths = ['hhhh', 'hh', 'hhhhh','h']
print(sorted(different_lengths))
print()

#   sorted() with key argument
#       key argument function must take exactly one argument, and must handle all values in itterable in question
words = ['banana', 'pie', 'Washington', 'book']
print(sorted(words, key=len))
print()

#   case insensitive sorting
names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case, key=str.lower))
print()

#   sort strings by reverse order
#       by definining function reverse_word
words = ['banana', 'pie', 'Washington', 'book']
def reverse_word(word):
    return word[::-1]
print(sorted(words, key=reverse_word))
#       using lambda function
print(sorted(words, key=lambda x: x[::-1]))
print()

#   lambda functions and namedtuples
from collections import namedtuple
StudentFinal = namedtuple('StudentFinal', 'name grade')
bill = StudentFinal('Bill', 90)
patty = StudentFinal('Patty', 94)
bart = StudentFinal('Bart', 89)
students = [bill, patty, bart]
print(sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True))
print()

#   }}}1
