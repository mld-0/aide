
def super_function(num1, num2, *args, callback=None, msg=[], **kwargs):
    print("num1=(%s)" % num1)
    print("num2=(%s)" % num2)
    print("args=(%s)" % str(args))
    print("callback=(%s)" % str(callback))
    print("msg=(%s)" % str(msg))
    print("kwargs=(%s)" % str(kwargs))
    print("")

def some_function(num1, num2):
    print("num1=(%s), num2=(%s)" % (num1, num2))
    print("")

def cat_function():
    print("meow")
    print("")

def outer_func(*args, **kwargs):
    print("args=(%s)" % str(args))
    print("kwargs=(%s)" % str(kwargs))
    print("")

var_num1 = 1
var_num2 = 2
var_args = [3, 4, 5]
var_callback = 6
var_msg = [7]
var_kwargs = { '9': 9, '10': 10 }  # cannot use dictionary keys that match names of other arguments, *if* we are also providing those arguments (if not, then the corresponding dict values are used arguments to function

#   Note that {'var_x': 3} is included in **kwargs dict in superfunction()
super_function(var_num1, var_num2, *var_args, callback=True, msg=var_msg, **var_kwargs, var_x=3)
#   or
super_function(var_num1, var_num2, *var_args, **var_kwargs, callback=True, msg=var_msg, var_x=3)


super_function(var_num1, var_num2, *var_args, msg=var_msg, **var_kwargs)

var_nums = { 'num1': var_num1, 'num2': var_num2 }
super_function(**var_nums)
some_function(**var_nums)

outer_func(a=3, b=4, **var_nums)

#   cannot pass **var_kwargs, since some_function() does not have a **kwargs, or other arguments named '9' or '10'
#some_function(**var_kwargs)

#   cannot pass **var_nums, since it contains keys 'num1' and 'num2' corresponding to positional arguments we are giving values for
#super_function(var_num1, var_num2, **var_nums)

#   cannot pass **var_nums (or **var_kwargs), to cat_function(), as it takes no arguments
#cat_function(**var_num1)

