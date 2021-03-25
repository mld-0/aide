#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2

#   LINK: https://realpython.com/python-dicts/

#   Lists vs Dicts
#   {{{
#   Similarities
#       Both are mutable.
#       Both are dynamic. They can grow and shrink as needed.
#       Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.
#   Differences
#       List elements are accessed by their position in the list, via indexing.
#       Dictionary elements are accessed via keys.
#   }}}

#   Defining a dictionary
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}
print(MLB_team)
#   alternative syntax:
#   {{{
MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])
MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)
#   }}}

#   Item in dictionary
print('Milwaukee' in MLB_team)
print('Toronto' in MLB_team)

#   Length of a dictionary
print(len(MLB_team))
print()

#   Itterate over dictionary by key and value
#       d.keys()        list of keys
#       d.values()      list of values
#       d.items()       list of key-value tuple pairs
d = { 'a': 1, 'b': 2 }
print(type(d.keys()))
print(type(d.values()))
print(type(d.items()))
for loop_key, loop_value in zip(d.keys(), d.values()):
    print("k=(%s), v=(%s)" % (loop_key, loop_value))
for loop_kv in d.items():
    print(loop_kv)
print()

#   Add entry to dict
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
del MLB_team['Seattle']
print(MLB_team)
print()

#   Any immutable (hashable) type can be used as a key
d = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', }
print(d)
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(d)

#   Declare empty dictionary
person = dict()
person = {}

#   Keys of a dictionary do not need to be the same type
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
print(foo)
d = {int: 1, float: 2, bool: 3}
print(d)
print()

#   clear dictionary
d = {'a': 10, 'b': 20, 'c': 30}
print(d)
d.clear()
print(d)
print()

#   d.get(<key>[, <default>])
#   get returns None if <key> is not in d, unless <default> is specified
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))
print(d.get('z'))
print(d.get('z', -1))
print()

#   d.pop(<key>[, <default>])
#   pop raises a KeyError exception if <key> is not in d, unless <default> is specified
d = {'a': 10, 'b': 20, 'c': 30}
print(d.pop('b'))
try:
    print(d.pop('z'))
except Exception:
    pass
print(d.pop('z', -1))
print()

#   d.popitem()
#   removes and returned last key-value pair as a tuple, if d is empty it raises KeyError exeception
d = {'a': 10, 'b': 20, 'c': 30}
print(d.popitem())
print(d)
print()

#   d.update(<obj>)
#   merge a dictionary with another dictionary, (or with an itterable of key-value pairs, or keyword arguments)
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update({'b': 200, 'd': 400})
d1.update([('b', 200), ('d', 400)])
d1.update(b=200, d=400)
print(d1)
print()


#   Merging dictionaries
a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {1:'fish', 2:'chips'}
c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}

#   default behaviour keeps last seen value for duplicate keys
print(a | b)  # python 3.9+
print({**a, **b})
x = a.copy(); x.update(b); print(x);

#   ChainMap requires dicts be in opposite order to other methods for the same behaviour
from collections import ChainMap
x = dict(ChainMap({}, b, a)); print(x);

print()


#   Merge c and d, appending values for duplicate keys
e = { **c }
for k, v in e.items():
    if k in e:
        e[k].extend(v)
    else:
        e[k] = v
print(e)
print()    



#   }}}1
