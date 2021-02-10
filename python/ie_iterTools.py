#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import itertools
#   {{{2
#   LINK: https://realpython.com/python-itertools/
#   LINK: https://docs.python.org/3.6/library/itertools.html#itertools-recipes

#   The functions in itertools “operate” on iterators to produce more complex iterators

#   Basic iterator functions:
#   iter(object[, sentinel])
#       provides an iterator for object, if object is iterable 
#       if optional argument sentinel is given, then object must be a callable object, and the iterator will call object (with no arguments) for each call to __next__(), until the value returned is equal to sentinel, returning the value at each stage
example_iter = list(iter([1, 2, 3, 4]))
print(example_iter)
print()

#   zip(*iterables)
#       returns an iterator, which generates a series of tuples, containing elements from each iterable, until the length of the shortest of *iterables is reached
example_zip = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(example_zip)
example_zip_undo = list(zip(*example_zip))
print(example_zip_undo)
print()

#   map(function, iterable[, iterable1, iterable2,..., iterableN])
#       aplies function to each item in iterable, and returns iterator that yields transformed items
#       the argument function must accept as many arguments as iterables are supplied
example_map = list(map(len, ['abc', 'de', 'fghi']))
print(example_map)
example_mapzip = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
print(example_mapzip)
print()

#   Iterators are more memory efficient, since they make use of lazy evaluation

#   Example problem: naive_grouper(inputs, n)
#   Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n. For simplicity, assume that the length of the input list is divisible by n. For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)]
#   better_grouper() is substantially more memory efficent than naive_grouper()
def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = naive_grouper(nums, 2)
print(result)
result = list(better_grouper(nums, 2))
print(result)
print()

#   Now, consider the case where len(inputs) is not evenly divisible by n - the resulting list is only 8 elements long
result = list(better_grouper(nums, 4))
print(result)

#   One solution is to replace zip() with itertools.zip_longest()
def grouper(inputs, n, fillValue=None):
    iters = [iter(inputs)] * n
    return itertools.zip_longest(*iters, fillvalue=fillValue)

result = list(grouper(nums, 4))
print(result)
print()

#   itertools.combinations(iterable, n)
#   Brute force and combinations without replacement
#   You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills. How many ways can you make change for a $100 dollar bill?
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

#   all combinations of bills of length 3
combinations_3 = list(itertools.combinations(bills, 3))
print(len(combinations_3))

#   solution to change problem
makes_100 = []
for loop_n in range(1, len(bills)+1):
    for loop_combination in itertools.combinations(bills, loop_n):
        if sum(loop_combination) == 100:
            makes_100.append(loop_combination)
makes_100 = set(makes_100)
print(makes_100)

#   itertools.combinations_with_replacement(iterable, n)
#   Brue force with replacement
#   How many ways are there to make change for a $100 bill using any number of $50, $20, $10, $5, and $1 dollar bills?
#   This problem involves 96,560,645 combinations, and takes about 1.5m to run
if (False):
    bills = [50, 20, 10, 5, 1]
    makes_100 = []
    for loop_n in range(1, 101):
        for loop_combination in itertools.combinations_with_replacement(bills, loop_n):
            if sum(loop_combination) == 100:
                makes_100.append(loop_combination)
    makes_100 = set(makes_100)
    print(len(makes_100))

#   itertools.permutations(iterable, n=None)
#       return all possible combinations of an iterable (optionally, limited to a given number of output characters)
values = ['a', 'b', 'c']
permutations = list(itertools.permutations(values))
print(permutations)
print()


#   define 'evens' and 'odds' as generators
#   using conventional functions:
def evens():
    n=0
    while True:
        yield n
        n += 2
def odds():
    n = 1
    while True:
        yield n
        n += 2
_odds = odds()
_evens = evens()
odds_list = list(next(_odds) for loop_i in range(5))
evens_list = list(next(_evens) for loop_i in range(5))
print(odds_list)
print(evens_list)

#   itertools.count(start, [step]) implementation
#       count() is similar to range(), but returns an infinite sequence
_odds = itertools.count(1, step=2)
_evens = itertools.count(step=2)
odds_list = list(next(_odds) for loop_i in range(5))
evens_list = list(next(_evens) for loop_i in range(5))
print(odds_list)
print(evens_list)
print()

#   using count() as enumerator
values = ['a', 'b', 'c']
enum_values = list(enumerate(values))
print(enum_values)
enum_values = list(zip(itertools.count(), values))
print(enum_values)
print()

#   Recurrence Relations
#   i.e: The fibonachi sequence, F[n] = F[n-1] + F[n-2]; F[0]=0, F[1]=1
def fibs():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
_fibs = fibs()
fib_seq = list(next(_fibs) for loop_i in range(10))
print(fib_seq)
print()

#   itertools.repeat(object, [times])
#       create a generator that returns an object either infinitely, or a given number of times
_ones = itertools.repeat(1)
_twos = itertools.repeat(2)
ones_list = list(next(_ones) for loop_i in range(10))
twos_list = list(next(_twos) for loop_i in range(10))
print(ones_list)
print(twos_list)
print()

#   itertools.cycle(iterable)
#       creates a generator that repeats a repeating series of values from an iterable
_ones = itertools.cycle([1])
_zero_one = itertools.cycle([0,1])
ones_list = list(next(_ones) for loop_i in range(10))
zero_ones_list = list(next(_zero_one) for loop_i in range(10))
print(ones_list)
print(zero_ones_list)
print()

#   itertools.accumulate(iterable[, func])
#   or, alternatively: itertools.accumulate(iterable[, func, *, inital=None])

#   Continue: 2021-02-10T23:25:57AEDT accumulate() examples, first/second order sequences with accumulate

#   Continue: 2021-02-10T23:27:17AEDT deck of cards with examples, flattening a list with examples, ect.

#   }}}1
