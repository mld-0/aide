#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import random
import pprint
#   {{{2
#   https://realpython.com/list-comprehension-python/

#   list comprehension is (marginally) faster than generator sequences, while generators are more memory efficent, and can handle infinite sequences

#   new_list = [expression for member in iterable (if conditional)]
#       or
#   new_list = [expression (if conditional else expression) for member in iterable]


sentence = 'the rocket came back from mars'
sentence_vowels = [i for i in sentence if i in 'aeiou']
print(sentence_vowels)

is_consonant = lambda x: x.isalpha() and x.lower() not in 'aeiou'
sentence_consonants = [i for i in sentence if is_consonant(i)]
print(sentence_consonants)
print()

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
fixed_prices = [i if (i > 0) else 0 for i in original_prices]
print(fixed_prices)
print()

#   Set comprehension
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

#   Dictionary comprehension
squares = {i: i * i for i in range(10)}
print(squares)
print()

#   Nested comprehensions
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
city_temps = {city: [0 for i in range(7)] for city in cities}
pprint.pprint(city_temps)
matrix = [[j for j in range(5)] for i in range(6)]
pprint.pprint(matrix)
print()

#   Flaterning list of lists
#       loops which would be nested top->bottom become nested left->right, ie:
matrix = [[x for i in range(3)] for x in range(3)]
pprint.pprint(matrix)
matrix_flat = [num for row in matrix for num in row]
#   matrix_flat = [num for row in matrix for num in row if not print("num=(%s), row=(%s)" % (str(num), str(row)))]
print(matrix_flat)
print()


#   Basic function of the assignment (or walrus) operator :=
#       (a := b) == True     has the effect of setting a = b, then comparing b == True
a = False
b = True
if (a := b) == True:
    print("a=(%s)" % str(a))
#       this operator allows assignment where it would otherwise be forbidden. This can greatly simplify some loop structures,
get_weather_data = lambda: random.randrange(90,110)
hot_temps = [temp for loop_temp in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)
#   {{{
#       while (loop_item := input()) != EOF
#           print(loop_item)
#   or
#       filtered_data = [y for x in data if (y := f(x)) is not None]
#   }}}
some_list = [1, 2, 3]
if (some_list_len := len(some_list)) > 2:
    print("List some_list_len=(%s)" % str(some_list_len))
print()


#   }}}1
