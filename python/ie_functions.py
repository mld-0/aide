#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
#   LINK: https://realpython.com/defining-your-own-python-function/#functions-in-python

#   Function interface
#       arguments (if any) taken by the function
#       values (if any) returned by the function

#   def <function_name>([<parameters>]):
#       <statement(s)>

#       def	                    The keyword that informs Python that a function is being defined
#       <function_name>	        A valid Python identifier that names the function
#       <parameters>	        An optional, comma-separated list of parameters that may be passed to the function
#       :	                    Punctuation that denotes the end of the Python function header (the name and parameter list)
#       <statement(s)>	        A block of valid Python statements


#   Positional arguments 
#       must agree in order and number with the parameters declared in the function definition.
def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')
f(6, 'bananas', 1.74)

#   Keyword arguments 
#       must agree with declared parameters in number, but they may be specified in arbitrary order.
f(qty=6, item='bananas', price=1.74)
f(item='bananas', price=1.74, qty=6)

#   When positional and keyword arguments are both present, all the positional arguments must come first

#   Default parameters 
#       allow some arguments to be omitted when the function is called.
def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')
f(4, 'apples', 2.24)
f(4, 'apples')
f(4)
f()
f(item='kumquats', qty=9)
f(price=2.29)
print()

#   Mutable default parameter values
#   In Python, default parameter values are defined only once when the function is defined (that is, when the def statement is executed). The default value isn’t re-defined each time the function is called. Thus, each time you call f() without a parameter, you’re performing .append() on the same list.
#   As a workaround, consider using a default argument value that signals no argument has been specified. Most any value would work, but None is a common choice. When the sentinel value indicates no argument is given, create a new empty list inside the function:
def f(my_list=[]):
    my_list.append('###')
    return my_list
print(f())
print(f())
print(f())
print()

#   Pass-by-value vs Pass-by-reference
#   Argument passing in Python can be summarized as follows. Passing an immutable object, like an int, str, tuple, or frozenset, to a Python function acts like pass-by-value. The function can’t modify the object in the calling environment.
#   Passing a mutable object such as a list, dict, or set acts somewhat—but not exactly—like pass-by-reference. The function can’t reassign the object wholesale, but it can change items in place within the object, and these changes will be reflected in the calling environment.

#    As soon as f() executes the assignment x = 'foo', the reference is rebound, and the connection to the original object is lost.
iter_list = [ 40, dict(foo=1, bar=2), {1, 2, 3}, 'bar', ['foo', 'bar', 'baz']]
def f(x):
    x = 'foo'
for i in iter_list:
    f(i)
    print(i)
print()

#   updating a mutable object passed as argument in-place changes the origional object
my_dict = {'foo': 1, 'bar': 2, 'baz': 3}
def f(x):
    x['bar'] = 22
f(my_dict)
print(my_dict)
print()

#   A Python function is said to cause a side effect if it modifies its calling environment in any way. Changing the value of a function argument is just one of the possibilities.


#   Variable-Length Argument Lists

#   Tuple Packing 
#       Any arguments in the function call preceded by (*) are packed into a tuple that the function can refer to by the given parameter name.
def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
            print(x)
f(1, 2, 3)
f('foo', 'bar', 'baz', 'qux', 'quux')
print()

#   Tuple unpacking
#       When an argument in a function call is preceded by an asterisk (*), it indicates that the argument is a tuple that should be unpacked and passed to the function as separate values:
def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')
t = ('foo', 'bar', 'baz')
f(*t)
print()

#   Combined tuple packing and unpacking
def f(*args):
    print(type(args), args)
a = ['foo', 'bar', 'baz', 'qux']
f(*a)
print()


#   Argument Dictionary Packing
#       Preceding a parameter in a Python function definition by a double asterisk (**) indicates that the corresponding arguments, which are expected to be key=value pairs, should be packed into a dictionary
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)
f(foo=1, bar=2, baz=3)
print()

#   Argument Dictionary Unpacking
def f(a, b, c):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')
d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)
print()

#   Combined dictionary packing/unpacking
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)
d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)
print()

#   Putting (unpacking) together
def f(a, b, *args, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'args = {args}')
    print(F'kwargs = {kwargs}')
f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
print()

#   Multiple list unpackings in a single call (python3.5+)
def f(*args):
    for i in args:
            print(i)
a = [1, 2, 3]
t = (4, 5, 6)
s = {7, 8, 9}
f(*a, *t, *s)
print()

#   Multiple dictionary unpackings in a single call (python 3.5+)
def f(**kwargs):
    for k, v in kwargs.items():
            print(k, '->', v)
d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}
f(**d1, **d2)
print()

#   Keyword only parameter
#   In the function definition, specify *args to indicate a variable number of positional arguments. Each subsiquent argument becomes a keyword only parameter
def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')
concat('a', 'b', 'c')
concat('a', 'b', 'c', prefix='//')
concat('a', 'b', 'c', prefix='//', sep='-')
print()

#   The bare variable argument parameter * indicates that there aren’t any more positional parameters. This behavior generates appropriate error messages if extra ones are specified. It allows keyword-only parameters to follow.
def oper(x, y, *, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    else:
        return None
print(oper(3, 4, op='+'))
print(oper(3, 4, op='/'))
print()

#   Positional only arguments (python 3.8+)
#       To designate some parameters as positional-only, specify a bare slash (/) in the parameter list of a function definition. Any parameters to the left of the slash (/) must be specified positionally. 
def f(x, y, /, z):
    print(f'x: {x}')
    print(f'y: {y}')
    print(f'z: {z}')
f(1, 2, 3)
f(1, 2, z=3)
print()

#   Combining positional/keyword-only designators
def f(x, y, /, z, w, *, a, b):
    print(x, y, z, w, a, b)
f(1, 2, z=3, w=4, a=5, b=6)
f(1, 2, 3, w=4, a=5, b=6)
print()

#   docstring example
def avg(*args):
    """Returns the average of a list of numeric values."""
    return sum(args) / len(args)
print(avg.__doc__)
print()

#   Python function annotations
#       Annotations don’t impose any semantic restrictions on the code whatsoever. They’re simply bits of metadata attached to the Python function parameters and return value. Python dutifully stashes them in a dictionary, assigns the dictionary to the function’s __annotations__ dunder attribute, and that’s it. Annotations are completely optional and don’t have any impact on Python function execution at all.
def f(a: int = 12, b: str = 'baz') -> float:
    print(a, b)
    return(3.5)
print(f.__annotations__)
print(f())
print()

#   Using function annotations for type checking
def f(a: int, b: str, c: float):
    import inspect
    args = inspect.getfullargspec(f).args
    annotations = inspect.getfullargspec(f).annotations
    for x in args:
        print(x, '->', 'arg is', type(locals()[x]), ',', 'annotation is', annotations[x], '/', (type(locals()[x])) is annotations[x])
f(1, 'foo', 3.3)
f('foo', 4.3, 9)
f(1, 'foo', 'bar')
print()


#   Continue: 2021-02-11T17:04:39AEDT Python function annotations


#   }}}1
