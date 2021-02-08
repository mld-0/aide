#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
#   LINK: https://realpython.com/python-sets/

#   x = set(<iter>)
#       Sets are unordered.
#       Set elements are unique. Duplicate elements are not allowed.
#       A set itself may be modified, but the elements contained in the set must be of an immutable type.
x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)
x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
print(x)
x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)
print()

#   strings are iterable, just as list(<str>) generates a list of characters of <str>, set(<str>) produces a set of characters of <str>
print(set('foo'))
print()

#   An empty set is falsy
x = set()
if (x):
    print("true")
else:
    print("false")
print()

#   Elements of a set can be different types (so long as they are immutable)
x = {42, 'foo', (1, 2, 3), 3.14159}
print(x)
print()

#   Set size
x = {'foo', 'bar', 'baz'}
print(len(x))
print()

#   Set membership
print('bar' in x)
print('qux' in x)
print()


#   Set union (items either set)
#       x1.union(x2[, x3 ...])
#       x1 | x2 [| x3 ...]
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.union(x2))
print(x1 | x2)
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = {'baz', 'foo', 'qwerty'}
print(x1.union(x2, x3))
print(x1 | x2 | x3)
print()

#   Set intersection (items in both sets)
#       x1.difference(x2[, x3 ...])
#       x1 - x2 [- x3 ...]
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
print(a.intersection(b, c, d))
print(a & b & c & d)
print()

#   Set difference (items in the first set only)
#       x1.difference(x2[, x3 ...])
#       x1 - x2 [- x3 ...]
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
print(a.difference(b, c))
print(a - b - c)
print()

#   Symmetric difference (xor, items in one set or the other, but not both)
#       x1.symmetric_difference(x2)
#       x1 ^ x2 [^ x3 ...]
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.symmetric_difference(x2))
a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}
print(a ^ b ^ c)
print()

#   isdisjoint (True if both sets have no elements in common)
#       x1.isdisjoint(x2)
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.isdisjoint(x2))
print(x1.isdisjoint(x2 - {'baz'}))
print()

#  issubset (True if first set contains every element of the second) 
#       x1.issubset(x2)
#       x1 <= x2
x0 = {'foo', 'bar', 'baz', 'qux', 'quux'}
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.issubset(x0))
print(x1 <= x2)
print()

#   Proper subset, True if x1 is a subset of x2, but not equal to x2
#       x1 < x2
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2)
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2)
print()

#   issuperset
#       x1.issuperset(x2)
#       x1 >= x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
print(x1.issuperset(x2))
x2 = {'baz', 'qux', 'quux'}
print(x1 >= x2)
print()

#   Proper superset, True if x2 contains every element of x1, but x2 != x1
#       x1 > x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
print(x1 > x2)
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
print(x1 > x2)
print()

#   Modify a set by union.(add elements in x2 not in x1 to x1)
#       x1.update(x2[, x3 ...])
#       x1 |= x2 [| x3 ...]
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x1 |= x2
print(x1)
print()

#   Modify a set by intersection (set x1 equal to elements in both x1 and x2)
#       x1.intersection_update(x2[, x3 ...])
#       x1 &= x2 [& x3 ...]
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x1 &= x2
print(x1)
print()

#   Modify a set by difference.
#       x1.difference_update(x2[, x3 ...])
#       x1 -= x2 [| x3 ...]
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x1 -= x2
print(x1)
print()

#   Modify a set by symmetric difference.
#       x1.symmetric_difference_update(x2)
#       x1 ^= x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x1 ^= x2
print(x1)
print()

#   Add element
#       x.add(<element>)
x = {'foo', 'bar', 'baz'}
x.add('qux')
print(x)
print()

#   Remove element (raises exception if element not in set)
#       x.remove(<element>)
x = {'foo', 'bar', 'baz'}
x.remove('baz')
print(x)
print()

#   Remove element from set, with no exception for object not found
#       x.discard(<element>)
x = {'foo', 'bar', 'baz'}
x.discard('baz')
print(x)
print()

#   Remove random element
x = {'foo', 'bar', 'baz'}
x.pop()
print(x)
print()

#   Clear (remove all elements)
x = {'foo', 'bar', 'baz'}
x.clear()
print(x)
print()

#   Frozen Set (immutable set)
x = frozenset(['foo', 'bar', 'baz'])
print(x)
print()

#   Augmented assigment operators work on frozen sets, since 'x &= s' => 'x = x & s', which has the effect of creating a new object which is assigned to x
f = frozenset(['foo', 'bar', 'baz'])
s = {'baz', 'qux', 'quux'}
f &= s
f

#   being immutable, frozensets can be used as dictionary keys
x = frozenset({1, 2, 3})
y = frozenset({'a', 'b', 'c'})
d = {x: 'foo', y: 'bar'}
print(d)

#   }}}1
