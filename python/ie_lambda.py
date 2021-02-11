#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
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


#   Lambdas and decorators
#   Continue: 2021-02-12T01:30:33AEDT lambdas and trace


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




#   }}}1
