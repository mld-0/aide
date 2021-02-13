#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import functools
import time
import math
import random
#   {{{2
#   LINK: https://realpython.com/primer-on-python-decorators/

#   Functions are first class objects - that is, they can be passed as arguments
def greet_bob(greeter_func):
    return greeter_func("Bob")
def say_hello(name):
    print(f"Hello {name}")
def be_awesome(name):
    print(f"Yo {name}, together we are the awesomest!")
greet_bob(say_hello)
greet_bob(be_awesome)
print()

#   Inner functions - a function declared inside another function
#       the inner function is locally scoped to the parent function
def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the first_child() function")
    def second_child():
        print("Printing from the second_child() function")
    second_child()
    first_child()
parent()
print()

#   Returning functions from functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"
    def second_child():
        return "Call me Liam"
    if num == 1:
        return first_child
    else:
        return second_child
first = parent(1)
second = parent(2)
print(first)
print(first())
print(second)
print(second())
print()

#   decorators wrap a function, modifying its behavior.
#       example using function syntax
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
def say_whee():
    print("Whee!")
say_whee = my_decorator(say_whee)
print(say_whee)
say_whee()
print()

#   example using pie syntax
#       @my_decorator is equivelent to say_whee = my_decorator(say_whee)
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_whee():
    print("Whee!")
print(say_whee)
say_whee()
print()

#   another example, do_twice
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
@do_twice
def say_whee():
    print("Whee!")
say_whee()
print()

#   using arguments with decorator functions
def do_twice(func):
    @functools.wraps(func)  # preserve information about origional function 
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
@do_twice
def say_hello(name):
    print(f"Hello {name}")
say_hello("World")
print()

#   decorator boilerplate
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

#   example - function timer, print execution time
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
waste_some_time(1)
waste_some_time(99)
print()

#   example - debugger, print arguments and return value
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
make_greeting("Benjamin")
make_greeting("Richard", age=112)
make_greeting(name="Dorrisile", age=116)
print()

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))
print(approximate_e(5))
print()

#   example - sleep(0.1) before function calls
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(0.1)
        return func(*args, **kwargs)
    return wrapper_slow_down
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
countdown(3)
print()

#   Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:
PLUGINS = dict()
def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func
@register
def say_hello(name):
    return f"Hello {name}"
@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"
def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
print(PLUGINS)
randomly_greet("Alice")
print()


#   @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class
#   @property decorator is used to customize getters and setters for class attributes
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        """Get value of radius"""
        return self._radius
    #   .radius is a mutable property: it can be set to a different value. However, by defining a setter method, we can do some error testing to make sure it’s not set to a nonsensical negative number. Properties are accessed as attributes without parentheses.
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    #   .area is an immutable property: properties without .setter() methods can’t be changed. Even though it is defined as a method, it can be retrieved as an attribute without parentheses.
    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2
    #   .cylinder_volume() is a regular method.
    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 2
print(c.area)
try:
    c.area = 100
except Exception as e:
    print(e)
c.cylinder_volume(height=4)
try:
    c.radius = -1
except Exception as e:
    print(e)
c = Circle.unit_circle()
print(c.radius)
print(c.pi())
print(Circle.pi())
print()

#   class decorators - dataclass
#       alternatively: PlayingCard = dataclass(PlayingCard
from dataclasses import dataclass
@dataclass
class PlayingCard:
    rank: str
    suit: str


#   applying timer decorator to class measures to to initalise class
#       shorthand for 'TimeWaster = timer(TimeWaster)'
@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
tw = TimeWaster(1000)
tw.waste_time(999)
print()

#   Nested decorators
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
greet("Eva")
print()

#   changing order of do_twice / debug decorators
@do_twice
@debug
def greet(name):
    print(f"Hello {name}")
greet("Eva")
print()


#   extending do_twice to repeat a given number of times
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
greet("World")
print()

#   decorator that can be used both with and without arguments
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
@repeat
def say_whee():
    print("Whee!")
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
say_whee()
greet("Penny")
print()

#   decorator that can keep track of state
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
@count_calls
def say_whee():
    print("Whee!")
say_whee()
say_whee()
print(say_whee.num_calls)
print()


#   using classes as decorators
#       a typical implementation of a decorator class needs to implement .__init__() and .__call__()
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
@CountCalls
def say_whee():
    print("Whee!")
say_whee()
say_whee()
print(say_whee.num_calls)
print()


#   slow_down with optional rate argument
def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down
    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)
@slow_down(rate=0.1)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
countdown(3)
print()


#   singletons
#       a singleton is a class with only one instance (examples include None, True, and False)
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton
@singleton
class TheOne:
    pass
first_one = TheOne()
another_one = TheOne()
print(id(first_one))
print(id(another_one))
print(first_one is another_one)
print()


#   Continue: 2021-02-13T21:10:28AEDT catching return values

#   Continue: 2021-02-13T21:10:51AEDT set_unit

#   Continue: 2021-02-13T21:11:21AEDT validating json


#   }}}1
