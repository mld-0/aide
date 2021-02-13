#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
#   LINK: https://realpython.com/any-python/

#   any() vs or syntax
print(True or False)
print(any(False, True))
print()

#   any() vs or return syntax
#       any returns a Boolean
#       or returns the first Truthy values, or the last value 
print(1 or False)
print(None or 0)
print()

print(any([0, 0, 1, 0]))
print(any(set((True, False, True))))
print(any(map(str.isdigit, "hello world")))
print()

print(1 and True)
print(None and 0)

#   all() 
#       as per any, for and intead of or

#   operator.or_(a, b)
#       Returns bitwise or of a,b

#   }}}1
