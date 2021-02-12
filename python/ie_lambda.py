#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import functools
import unittest
import doctest
#   {{{2
#   LINK: https://realpython.com/python-lambda/

identity = lambda x: x
print(identity(2))
plusone = lambda x: x + 1
print(plusone(2))

#   Calling a lambda as a function
print((lambda x: x + 1)(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

#   Anonymous Functions
#       The following terms may be used interchangeably depending on the programming language type and culture:
#           Anonymous functions
#           Lambda functions
#           Lambda expressions
#           Lambda abstractions
#           Lambda form
#           Function literals


addnums = lambda x, y: x + y
print(addnums(2,3))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))
print()

#   Traceback
#       if an execption occurs in a lambda, python traceback shows only 'lambda' instead of the name as with a function

#   Lambda syntax
#       It can only contain expressions and can't include statements in its body.
#           In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception
#       It is written as a single line of execution.
#       It does not support type annotations.
#       It can be immediately invoked (IIFE).

#   Arguments:
#       Lambdas support all forms of arguments that a function defined with 'def' does
print((lambda x, y, z: x + y + z)(1, 2, 3))
print((lambda x, y, z=3: x + y + z)(1, 2))
print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *args: sum(args))(1,2,3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
print()


#   Decorators
#       a decorator is the implementation of a pattern that allows adding a behavior to a function or a class.
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps
@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")
decorated_function("Python")
print()

#   Lambdas and decorators
#   Continue: 2021-02-12T01:30:33AEDT lambdas and trace
#   Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap
#   Applying decorator to a function
@trace
def add_two(x):
    return x + 2
add_two(3)
#   Applying decorator to a lambda
#       Although it's not possible to decorate a lambda with the @decorator syntax, a decorator is just a function, so it can call the lambda function:
add_two = lambda x: x + 2
print(trace(add_two(3)))
print()
#   Using trace(lambda) with map
print(list(map(trace(lambda x: x*2), range(3))))
print()


#   Closure:
#       closure as a function
def outer_func(x):
    y = 4
    def inner_func(z):
        #print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func
for i in range(3):
    closure = outer_func(i)
    loop_x = i
    loop_y = closure(loop_x)
    print("loop_x=(%s), loop_y=(%s)" % (str(loop_x), str(loop_y)))
print()
#   Implemented with lambda
def outer_func(x):
    y = 4
    return lambda z: x + y + z
for i in range(3):
    closure = outer_func(i)
    loop_x = i
    loop_y = closure(loop_x)
    print("loop_x=(%s), loop_y=(%s)" % (str(loop_x), str(loop_y)))
print()


#   Unexpected lambda behaviour
#      the free variable n, as implemented, is bound at the execution time of the lambda expression. The Python lambda function on line 4 is a closure that captures n, a free variable bound at runtime. 
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))
for f in funcs:
    f()
print()
#   to obtain the desired result, assign 'n' in the definition
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))
for f in funcs:
    f()
print()



#   Testing lambdas
#   unittest
#addtwo = lambda x: x + 2
#class TestLambdaAddTwo(unittest.TestCase):
#    def test_add_two(self):
#        self.assertEqual(addtwo(2), 4)
#    def test_add_twoPointTwo(self):
#        self.assertEqual(addtwo(2.2), 4.2)
#    @unittest.expectedFailure
#    def test_add_three(self):
#        self.assertEqual(addtwo(3), 6)
#if __name__ == '__main__':
#    unittest.main(verbosity=2)
#
##   doctest
#addtwo = lambda x: x + 2
#addtwo.__doc__ = """Add 2 to number.
#    >>> addtwo(2)
#    4
#    >>> addtwo(2.2)
#    4.2
#    """
#if __name__ == '__main__':
#    doctest.testmod(verbose=True)
#print()

#   Lambda abuses
#       class methods can, but should not, be defined as lambdas

#   Lambdas and map(), filter(), functools.reduce()
list_a = ['cat', 'dog', 'cow']
print(list(map(lambda x: x.upper(), list_a)))
print(list(filter(lambda x: 'o' in x, list_a)))
print(functools.reduce(lambda acc, x: f'{acc} | {x}', list_a))
print()

#   Key functions
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
print(sorted_ids)
print()


#   Monkey Patching
from contextlib import contextmanager
import secrets
def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'
@contextmanager
def mock_token():
   """Context manager to monkey patch the secrets.token_hex function during testing.""" 
   default_toxen_hex = secrets.token_hex
   secrets.token_hex = lambda x: 'feedfacecafebeef'
   yield
   secrets.token_hex = default_toxen_hex
def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"
test_gen_key()

#   Monkey patching using pytest
import secrets
def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'
def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"




#   }}}1
