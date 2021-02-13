#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
#   LINK: https://realpython.com/python-namespaces-scope/

#   Assignment statements create symbolic names for referencing an object
#       x = 'foo'       creates a symbolic name 'x' referencing string object 'foo'

#   Namespaces are a collection of currently defined symbolic names with corresponding object references
#   Python has 4 namespaces:
#       Built-in
#       Global
#       Enclosing
#       Local

#   Built-in namespace:
#       contains the name of all of python's built-in objects 
#   listed with:
print(dir(__builtins__))
print()

#   Global namespace
#       contains names defined at the level of the main program
#       seperate global namespaces are created for each module imported with the 'import' statement

#   Enclosing namespace
#       The namespace of another function, from which the current function was called (if applicable)

#   Local namespace
#       Python defines a new local namespace whenever a function is called, until said function terminates

#   LEGB - Local, Enclosing, Global, Bultin-in
#       order which python searches namespaces for a given variable name
#       if the name is not found in any of these namespaces, a NameError is produced

#   Example:
#       following the LEGB rule, the output is 'local'
x = 'global'
def f():
    x = 'enclosing'
    def g():
        global x
        print(x)
        x = 'local-1'
        print(x)
    def h():
        nonlocal x
        print(x)
        x = 'local-2'
        print(x)
    g()
    h()
f()
print()

#   globals()
#       returns a reference to the current global namespace dictionary
print(globals())
print(globals()['x'])
print()

#   locals()
#       when called outside a function, locals() returns a dictionary with the same values as globals()
#       unlike globals(), locals() contains a copy of the namespace, not a reference to it. Therefore, unlike globals()['var'], locals()['var'] cannot be used to modify variable 'var'
print(locals())
print()

#   Modify Variables Out of Scope
#       An immutable argument can never be modified by a function.
x = 20
def f():
     # print(x)    # variable referenced before assignment, cant be printed
     x = 40
     print(x)
f()
print(x)
print()

#       A function can modify an object of mutable type that’s outside its local scope if it modifies the object in place
my_list = ['foo', 'bar', 'baz']
def f():
    print(my_list)
    my_list[1] = 'quux'
    print(my_list)
f()
print(my_list)
print()

for i in range(10):
    square = i * i
print(square)
print()
    


#   }}}1
