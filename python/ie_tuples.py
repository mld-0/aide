#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2

#   LINK: https://realpython.com/python-lists-tuples/

#   Tuples differ from lists in that:
#       Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
#       Tuples are immutable (unmodifiable)

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
print(t[1::2])
print()

#   Advantages vs lists:
#       Tuples are faster than lists,
#       Protection against modification of data
#       Can be used as dictionary keys

#   A tuple of length 1, declared (see below) becomes said value, to declare a tuple of length 1, affix the item with ','
t = (2)
print(type(t))
t = (2,)
print(type(t))

#   Tuple packing:
t = ('foo', 'bar', 'baz', 'qux')
#   Tuple unpacking
(s1, s2, s3, s4) = t
#   Combined packing/unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')

#   Tuple packing is implicit when '()' are left out
t = 1, 2, 3
print(t)

#   }}}1
