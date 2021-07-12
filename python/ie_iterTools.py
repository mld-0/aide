#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import itertools
import operator
import random
import functools
from collections import namedtuple
import csv
import datetime
import statistics
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
#       create an iterator that returns the object either infinitely, or a given number of times
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
_zero_one = itertools.cycle([1,2,3])
ones_list = list(next(_ones) for loop_i in range(10))
zero_ones_list = list(next(_zero_one) for loop_i in range(9))
print(ones_list)
print(zero_ones_list)
print()

#   itertools.accumulate(iterable[, func=operator.add])
#       return series of accumulated sums (or other binary function results)
#       or, alternatively: itertools.accumulate(iterable[, func, *, inital=None])
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values_sum = list(itertools.accumulate(values, operator.add))
print(values_sum)
print()

values = [9, 21, 17, 5, 11, 12, 2, 6]
values_max = list(itertools.accumulate(values, max))
values_min = list(itertools.accumulate(values, min))
print(values_max)
print(values_min)
print()

#   First order sequence definition
def first_order(p, q, initial_val):
    """Return sequence defined by: s(n) = p * s(n-1) + q"""
    return itertools.accumulate(itertools.repeat(initial_val), lambda s, x: p*s + q)

#   defining various sequences in terms of first_order()
_odds = first_order(p=1, q=2, initial_val=0)
_evens = first_order(p=1, q=2, initial_val=1)
_all_ones = first_order(p=1, q=0, initial_val=1)
_alternating_ones = first_order(p=-1, q=0, initial_val=1)
odds_list = list(next(_odds) for loop_i in range(5))
evens_list = list(next(_evens) for loop_i in range(5))
all_ones_list = list(next(_all_ones) for loop_i in range(5))
alternating_ones_list = list(next(_alternating_ones) for loop_i in range(5))
print(odds_list)
print(evens_list)
print(all_ones_list)
print(alternating_ones_list)
print()

#   Second order sequence definition
def second_order(p, q, r, initial_values):
    """Return sequence defined by: s(n) = p * s(n-1) + q * s(n-2) + r"""
    _func_intermediate = lambda s, x: (s[1], p*s[1] + q*s[0] + r)
    intermediate = itertools.accumulate(itertools.repeat(initial_values), _func_intermediate)
    return map(lambda x: x[0], intermediate)

#   defining fibonachi sequence with second_order()
_fibs = second_order(p=1, q=1, r=0, initial_values=(0, 1))
_pell = second_order(p=2, q=1, r=0, initial_values=(0, 1))
_lucas = second_order(p=1, q=1, r=0, initial_values=(2, 1))
fib_seq = list(next(_fibs) for loop_i in range(10))
pell_seq = list(next(_pell) for loop_i in range(10))
lucas_seq = list(next(_lucas) for loop_i in range(10))
print(fib_seq)
print(pell_seq)
print(lucas_seq)
print()



#   Continue: 2021-02-10T23:27:17AEDT deck of cards with examples, 
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['♥', '♦', '♣', '♠']

#   cards as a generator function
def cards():
    """Return a generator that yields playing cards."""
    for rank in ranks:
        for suit in suits:
            yield rank, suit

#   cards as a generator expression
cards = ((rank, suit) for rank in ranks for suit in suits)

#   itertools.product(*iterables, repeat=1)
#       product(A, B) returns the same as ((x,y) for x in A for y in B).
#       Roughly equivalent to nested for-loops in a generator expression. 
#   cards defined with itertools.product
cards = itertools.product(ranks, suits)

#   note that shuffling a sequence requires creating a copy (via list())
def shuffle(deck):
    """Return iterator over shuffled deck."""
    deck = list(deck)
    random.shuffle(deck)
    return iter(tuple(deck))

cards = shuffle(cards)

#   itertools.tee(iterable, n=2)
#       Create a number of independent iterators from a single input iterable
iter_0 = iter(range(10))
iter_1, iter_2 = itertools.tee(iter_0, 2)
#   converting an iterator ot a list consumes it
print(list(iter_1))
#   however, because iter_2 and iter_1 are independent, iter_2 is still available
print(list(iter_2))
print()

#   itertools.islice(iterable, stop)
#   itertools.islice(iterable, start, stop[, step=1])
#       Works like splice() on a list, but returns an iterator
print(list(itertools.islice([1, 2, 3, 4], 3)))
print(list(itertools.islice([1, 2, 3, 4], 1, 2)))
print()

#   itertools.chain(*iterables)
print(list(itertools.chain('abc', [1, 2, 3])))
print()

def cut(deck, n):
    """Return an iterator over a deck of cards cut at index n."""
    deck1, deck2 = itertools.tee(deck, 2)
    top = itertools.islice(deck1, n)
    bottom = itertools.islice(deck2, n, None)
    return itertools.chain(bottom, top)

cards = cut(cards, 26)

def deal(deck, num_hands=1, hand_size=5):
    iters = [iter(deck)] * hand_size
    return tuple(zip(*(tuple(itertools.islice(itr, num_hands)) for itr in iters)))

p1_hand, p2_hand, p3_hand = deal(cards, num_hands=3)
#   hands of 3 players,
print(p1_hand)
print(p2_hand)
print(p3_hand)
#   and number of remaining cards in deck
print(len(tuple(cards)))
print()

#   flatern a list of lists
#       using itertools.chain.from_iterable()
#       requires that each element of list to be flattered be an iterable
list_a = [[1, 2, 3], [4, 5, 6]]
list_b = itertools.chain.from_iterable(list_a)
print(list(list_b))
print()

#   functools.reduce(function, iterable[, initalizer])
#       For a binary function, and iterable, apply function to pairs of objects in iterable, and return final result
#       as if itertools.accumulate() returned only final value in resulting sequence
print(functools.reduce(operator.add, [1, 2, 3, 4, 5]))

#   itertools.filterfalse(pred, iterable)
#       return those items in iterable for which pred(item) is false. If pred=None, return items that are False
print(list(itertools.filterfalse(bool, [1, 0, 1, 0, 0])))

#   itertools.takewhile(pred, iterable)
#       return sucessive entries from an iterable so long as pred evaluates to True for each entry
print(list(itertools.takewhile(bool, [1, 1, 1, 0, 0])))

#   itertools.dropwhile(pred, iterable)
#       drop items from iterable while pred(item) is True, then return each remaining element
print(list(itertools.dropwhile(bool, [1, 1, 1, 0, 0, 1, 1, 0])))
print()


#   S&P500 Analysis
class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
    __slots__ = ()
    def __le__(self, other):
        return self.value <= other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

def read_prices(csv_file, _strptime=datetime.datetime.strptime):
    with open(csv_file) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            yield DataPoint(date=_strptime(row['Date'], '%Y-%m-%d').date(), value=float(row['Adj Close']))

def consecutive_positives(sequence, zero=0):
    def _consecutives():
        for itr in itertools.repeat(iter(sequence)):
            yield tuple(itertools.takewhile(lambda p: p > zero, itertools.dropwhile(lambda p: p <= zero, itr)))
    return itertools.takewhile(lambda t: len(t), _consecutives())

path_sp500csvdata = "data/sp500.csv"
prices = tuple(read_prices(path_sp500csvdata))
gains = tuple(DataPoint(day.date, 100*(day.value/prev_day.value - 1)) for day, prev_day in zip(prices[1:], prices))

zdp = DataPoint(None, 0)  # zero DataPoint
max_gain = functools.reduce(max, itertools.filterfalse(lambda p: p <= zdp, gains))
print(max_gain)
max_loss = functools.reduce(min, itertools.filterfalse(lambda p: p > zdp, gains), zdp)
print(max_loss)

growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))
longest_growth_streak = functools.reduce(lambda x, y: x if len(x) > len(y) else y, growth_streaks)

print('Longest growth streak: {num_days} days ({first} to {last})'.format( num_days=len(longest_growth_streak), first=longest_growth_streak[0].date, last=longest_growth_streak[-1].date))
print()


#   itertools.groupby(iterable, key=None)
#       Make an iterator that returns consecutive keys and groups from the iterable. The key is a function computing a key value for each element. If not specified or is None, key defaults to an identity function and returns the element unchanged. Generally, the iterable needs to already be sorted on the same key function.
data = [{'name': 'Alan', 'age': 34},
        {'name': 'Catherine', 'age': 34},
        {'name': 'Betsy', 'age': 29},
        {'name': 'David', 'age': 33}]
#grouped_data = itertools.groupby(data, key=lambda x: x['age'])
data = sorted(data, key=lambda x: x['age'])
grouped_data = itertools.groupby(data, key=lambda x: x['age'])
for key, grp in grouped_data:
    #print(type(grp))
    #print(list(grp))
    #print(grp)
    print('{}: {}'.format(key, list(grp)))
print()


#   Swiming teams problem
#   Each stroke should have an 'A' and a 'B' relay team with four swimmers each. The 'A' team should contain the four swimmers with the best times for the stroke and the 'B' team the swimmers with the next four best times.
path_swimmingdata = "data/swimmers.csv"

class Event(namedtuple('Event', ['stroke', 'name', 'time'])):
    __slots__ = ()
    def __lt__(self, other):
        return self.time < other.time

def read_events(csvfile, _strptime=datetime.datetime.strptime):
    def _median(times):
        return statistics.median((_strptime(time, '%M:%S:%f').time() for time in row['Times']))
    fieldnames = ['Event', 'Name', 'Stroke']
    with open(csvfile) as infile:
        #   restkey is the field which data fields not specified are added to
        reader = csv.DictReader(infile, fieldnames=fieldnames, restkey='Times')
        next(reader)  # skip header
        for row in reader:
            yield Event(row['Stroke'], row['Name'], _median(row['Times']))

def sort_and_group(iterable, key=None):
    """Group sorted `iterable` on `key`."""
    return itertools.groupby(sorted(iterable, key=key), key=key)

def grouper(iterable, n, fillvalue=None):
    iters = [iter(iterable)] * n
    return itertools.zip_longest(*iters, fillvalue=fillvalue)

events = tuple(read_events(path_swimmingdata))
print("len(events)=(%s)" % len(events))
print("events[0]=(%s)" % str(events[0]))

#   Group the events by stroke.
#   For each stroke:
#   Group its events by swimmer name and determine the best time for each swimmer.
#   Order the swimmers by best time.
#   The first four swimmers make the 'A' team for the stroke, and the next four swimmers make the 'B' team.
results_teams = []
for stroke, events in sort_and_group(events, key=lambda event: event.stroke):
    print("stroke=(%s), len(events)=(%s)" % (str(stroke), len(str(events))))
    events_by_name = sort_and_group(events, key=lambda event: event.name)
    best_times = (min(event) for _, event in events_by_name)
    sorted_by_time = sorted(best_times, key=lambda event: event.time)
    loop_team_members = itertools.islice(grouper(sorted_by_time, 4), 2)
    teams = zip(('A', 'B'), loop_team_members)
    results_teams.append(teams)

for teams in results_teams:
    for team, swimmers in teams:
        loop_names = ', '.join(swimmer.name for swimmer in swimmers)
        loop_output = '{stroke} {team}: {names}'.format(stroke=stroke.capitalize(), team=team, names=loop_names)
        print(loop_output)
print()


#   }}}1
