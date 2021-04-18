#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2

#   dir()
#       Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
#   Get attributes unique to given object variable:
var_list = [1, 2, 3]
print(set(dir(var_list)) - set(dir(object)))
print()

#   type()  
#       If only one parameter is specified, the type() function returns the type of this object
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33
print(type(a))
print(type(b))
print(type(c))
print()

#   vars()
#       returns the __dict__ attribute of the given object. Acts like the locals() function if no argument is provided.
class Foo:
    x = 10
    y = 20
print(vars(Foo))
print()

#   id()
#       returns a unique id for the specified object

#   help()
#       The help() method is used for interactive use. View documentation related to a specific topic/function/class

#   hasattr(object, name)
#       object - object whose named attribute is to be checked
#       name - name of the attribute to be searched
#       returns True if object has the given named attribute
class Person:
    age = 23
    name = 'Adam'
person = Person()
print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
print()

#   getattr(object, name[, default])
#       object - object whose named attribute's value is to be returned
#       name - string that contains the attribute's name
#       default (Optional) - value that is returned when the named attribute is not found
#   getattr(object, 'x') is completely equivalent to object.x
class Person:
    age = 23
    name = "Adam"
person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
print()

#   repr(obj)
#       returns a printable representation of the given object
#   str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable
class Person:
    name = 'Adam'
    def __repr__(self):
        return repr('Hello ' + self.name )
print(repr(Person()))
print()

#   callable(object)
#       Returns
#       True - if the object appears callable
#       False - if the object is not callable.


#   isinstance(object, type)
#       Returns True if the specified object is of the specified type, otherwise False
print(isinstance("Hello", (float, int, str, list, dict, tuple)))
class myObj:
  name = "John"
y = myObj()
print(isinstance(y, myObj))
print()

#   issubclass()
#       Return True if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked.
marks = 90
print(isinstance(marks, int))
print()

#   __doc__
#       (attribute) access docstring of method or object

#   __name__


#   Get Parent classes of class
import inspect
print(inspect.getmro(object))
print(inspect.getmro(str))
print(isinstance(str, object))
print(issubclass(str, object))



#   Methods of an object
print([x for x in dir(str) if callable(getattr(str, x))])

#   Doesn't work?
#print(inspect.getmembers(str, inspect.isfunction))

#   }}}1
