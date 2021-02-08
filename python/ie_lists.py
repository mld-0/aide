#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2

#   LINK: https://realpython.com/python-lists-tuples/

#   Characteristics of python lists
#       Lists are ordered.
#       Lists can contain any arbitrary objects.
#       List elements can be accessed by index.
#       Lists can be nested to arbitrary depth.
#       Lists are mutable.
#       Lists are dynamic.

#   Lists can contain a number of objects, from 0, to as many as memory permits
a = []
print(a)
print(len(a))
a = ['foo', 'bar', 'baz', 'qux']
print(a)
print(len(a))
print()

#   '==' to compare values of lists
#   'is' to check if lists are the same object

#   '=' assigns list object
print(a == a)
print(a is a)
print()

#   splices assign list values
print(a == a[:])
print(a is a[:])
print()

#   Lists that have the same elements in different order are not the same
print([1, 2, 3, 4] == [4, 1, 3, 2])
print()

#   Lists can contain any assortment of objects
print([21.42, 'foobar', 3, 4, 'bark', False, 3.14159])
print()

#   Indexing lists:
#       Elements of list can be accessed by index
a = [0, 1, 2, 3, 4, 5]
print(a)
print(a[0])
print(a[2])
print(a[5])
#       a[-1] is equivelent to a[len(a)-1]
print(a[len(a)-1])
print(a[-1])

#   splices
#       a[m:n], from a[m], to (but not including) a[n]
print(a[2:2])
print(a[2:3])
#       either positive or negative indexes can be used
print(a[1:4])
print(a[-5:-2])
#       a[:n] is equivelent to a[0:n]
print(a[:4])
#       a[m,:] is equivelent to a[m,len(a)]
print(a[2:])

#   strides
#       a slice is a stride of 1
#       a[m:n] = a[m:n:1]
#       specify stride = 2 prints from m,n, printing only every 2nd character
print(a[::1])
print(a[::2])
print(a[::3])
#       reverse a list with a stride of -1
print(a[::-1])
print(a[::-2])
print(a[::-3])
print()

#   Is element in list:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print('qux' in a)
print('thud' in a)
print()

#   '+' concatination:
print(a + ['grault', 'garply'])
#   '*' replication:
print(a * 2)
print()

#   min(), max(), provided all elements support greater/less-than comparisions
print(min(a))
print(max(a))
print()

#   Nested lists
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
#   len(), and 'in' are non-recursive 
len(x)
print('ddd' in x)
print('ddd' in x[1][1])
#   (non-recursively) Flatten nested list
import itertools
flat = list(itertools.chain(*x))
flat = [item for sublist in x for item in sublist]
print(flat)
#   recursively flatten a nested list
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
rec_flat = flatten(x)
print(rec_flat)
print()

#   Modifying single list elements
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)
#   delete list element
del a[3]
print(a)
print()

#   Modifying multiple list values
#       a[m:n] = <iterable>
#   note that list_ins is not 3 elements, as the slice 1:4 is 
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(len(a))
list_ins = [1.1, 2.2, 3.3, 4.4, 5.5]
a[1:4] = list_ins
print(a)
print(len(a))
#   insert elements at list at 'm' without replacing current elements by specifyin splice [m:m]
a = [1, 2, 3, 4]
print(a)
a[2:2] = [5, 6, 7, 8]
print(a)
#   delete elements by splice
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[1:5] = []
print(a)
del a[1:5]
print(a)
print()

#   list methods:
#   a.index(<element>[, <start>, <end>])    get index of (first instance of) <element>, beginning at <start> and ending at <end>
#       raises ValueError exception if <element> is not in a
#   get the index of the <n>-th occurence of <element> in <list>
#       [i for i, n in enumerate(<list>) if n == <element>][<n>]
x = ['w', 'e', 's', 's', 's', 'z','z', 's']
print(x)
loc_s = [i for i, element in enumerate(x) if element == 's']
print(loc_s)
print()
#   a.append(<obj>)         append <obj> to end of list a
a = ['a', 'b']
a.append([1, 2, 3])
print(a)
a = ['a', 'b']
a.append('foo')
print(a)
print()
#   a.extend(<iterable>)    add items in <iterable> indervidually to list
#       equivelent to: a += <iterable>
a = ['a', 'b']
a.extend([1, 2, 3])
print(a)
print()
#   a.insert(<index>, <obj>)
#       equivelent to a[<index>:<index>] = [ <obj> ]
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.insert(3, 3.14159)
print(a)
print()
#   a.remove(<obj>)         remove <obj> from list
a  = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.remove('baz')
print(a)
#   a.pop(<index>)
#       (unlike remove), specify index of item, to be removed, which is then returned
#       <index> defaults to -1

#   }}}1
