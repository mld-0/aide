#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import pandas as pd
import numpy as np
import re
#   {{{2
#   See: Ch7 OReilly Python for Data Analysis 2nd Edition 

#   Handling missing data
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())
print()

#   NA handling methods
#       dropna()            Filter axis labels based on whether values for each label have missing data (with specified threshold)
#                           default: drop any row containing a missing value
#       fillna()            Fill in missing data with value, or interpolation method such as ffill / bfill
#       isnull()            return boolean values indicating which values are missing/NA
#       notnull()           Negation of isnull


#   Filtering out Missing Data
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
#   or
#>%     print(data[data.notnull()])
print()

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data.dropna(how='all'))  # only drop rows that are all NA
print(data.dropna(axis=1, how='all'))  # drop columns that are all NA
print()

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna(thresh=2))  # keep only rows containing at least a given number of observations
print()

#   Filling in Missing Data
print(df.fillna(0))  # replace all missing values with 0
print(df.fillna({1: 0.5, 2: 0}))  # replace missing values in specified columns with values
print()

#   fillna() returns a new object, but can modify existing object in-place with
#>%     df.fillna(0, inplace=True)

#   fillna arguments
#       value       scalar value or dict-like object to use to fill missing values
#       method      Interpolation, by (default='ffill')
#       axis        Axis to fill on (default=0)
#       inplace     modify the calling object in-place
#       limit       for foward and back filling, maximum number of consecutive period to fill

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))  # interpolate up to 2 values for each NA
print()

data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))  # fill with mean value
print()

#   Removing duplicates
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())  # boolean Series, has each row been observed previously

#   drop_duplicates()   return a df where duplicated() is false
print(data.drop_duplicates())

#   filtering based on column
data['v1'] = range(7)
print(data['k1'].drop_duplicates())

print(data.drop_duplicates(['k1', 'k2'], keep='last'))  # filter based on columns [k1, k2], keeping last (instead of first) duplicate
print()


data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
meat_to_animal = {
      'bacon': 'pig',
      'pulled pork': 'pig',
      'pastrami': 'cow',
      'corned beef': 'cow',
      'honey ham': 'pig',
      'nova lox': 'salmon'
}

#   map(arg, na_action)   accepts function or dict (like) object
#       Using map is a convenient way to perform element-wise transformations and other data cleaning–related operations.
#           arg             mapping correspondence (function or series)
#           na_action       if 'ignore', propogate NaN values without passing to mapper
lowercased = data['food'].str.lower()  # convert to lower-case
data['animal'] = lowercased.map(meat_to_animal)
#   or
data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data)
print()

#   replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')
#       Replace values given in to_replace with value.  Values of the DataFrame are replaced with other values dynamically.
#           to_replace          How to find values that will be replaced (str, regex, list, dict, Series, int, float, or None)
#           value               Values to replace any values matching to_replace (scalar, dict, list, str, regex) 
#                               (dict specifys values per column)
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data.replace([-999, -1000], np.nan))
print(data.replace([-999, -1000], [np.nan, 0]))  # To use a different replacement for each value, pass a list of substitutes
#   or
#>%     data.replace({-999: np.nan, -1000: 0})
print()


#   Renaming Axis Indexes
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
data.index = data.index.map(lambda x: x[:3].upper())
#   or
#>%     data = data.rename(index=lambda x: x[:3].upper())
print(data)
print()

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data.rename(index={'Ohio': 'INDIANA'}, columns={'three': 'peekaboo'}))
print()


#   Discretization and Binning
ages = [7, 20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [0, 18, 25, 35, 60, 100]
group_names = ['Child', 'Youth', 'YoungAdult', 'MiddleAged', 'Senior']

#   cut(x, bins, [...])
#       Use cut when you need to segment and sort data values into bins. This function is also useful for going from a continuous variable to a categorical variable.
#           x           array to be binned (must be 1-dimensional)
#           bins        if int, define number of equal width bins the range of x, 
#                       if sequence, define the bin edges 
#                       IntervalIndex
cats = pd.cut(ages, bins, right=False)  # closed on LHS of interval 
cats = pd.cut(ages, bins, labels=group_names)
print(cats)
print(cats.categories)
print(cats.codes)
print(pd.value_counts(cats))
print()

#   If you pass an integer number of bins to cut instead of explicit bin edges, it will com‐ pute equal-length bins based on the minimum and maximum values in the data
#   The precision=2 option limits the decimal precision to two digits.
data = np.random.rand(20)
cats = pd.cut(data, 4, precision=2)
print(cats)
print(pd.value_counts(cats))
print()

#   qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')
#   Quantile-based discretization function. Discretize variable into equal-sized buckets based on rank or based on sample quantiles. 
#       x               1d ndarray or series
#       q               int or list of float
#       labels          use as labels for resulting bins (must be same length as bins)
#       retbins         whether to return the (bins, labels) or not <?>
#       precision       precision at which to store and display labels
#       duplicates      behaviour for duplicate bin edges
data = np.random.randn(1000)  # Normally distributed
cats = pd.qcut(data, 4)
print(cats)
print(pd.value_counts(cats))
print()

print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))
print()


#   Detecting and Filtering Outliers
data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
print()

#   any(axis=0, bool_only=None, skipna=True, level=None, **kwargs)
#       Return whether any element is True, potentially over an axis

#   Select all rows exceding +/-3
#   Ongoing: 2021-03-01T23:36:47AEDT purpouse of arg 1
print(data[(np.abs(data) > 3).any(1)])

#       np.abs()
#       np.sign()
#   Cap values at max/min of +/-3
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())
print()


#   Permutations and Random Sampling
#       numpy.random.permutation()
#   Calling permutation with the length of the axis you want to permute produces an array of integers indicating the new ordering
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
print(df)
print(sampler)
print(df.take(sampler))
print()

#   To select a random subset without replacement, you can use the sample method on Series and DataFrame
print(df.sample(n=3))
print()

#   To generate a sample with replacement (to allow repeat choices), pass replace=True to sample
choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=5, replace=True)
print(draws)
print()

#   Continue: 2021-03-01T23:59:38AEDT Indicator/Dummy Variables
#   Indicator/Dummy Variables
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
print(df)
print(pd.get_dummies(df['key']))
print()
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)
print()

#   Movies dataset - adding indicator variables for each genre
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('data/movielens/movies.dat', sep="::", header=None, names=mnames, engine='python')  # use engine='python' to prevent error about unsupported regex seperator
print(movies)
all_genres = []
for x in movies['genres']:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
print(genres)
zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)
for i, gen in enumerate(movies.genres):
    indicies = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indicies] = 1
dummies = dummies.add_prefix('Genre_')
movies_windic = movies.join(dummies)
print(movies_windic.iloc[0])
print()

#   A useful recipe for statistical applications is to combine get_dummies with a discreti‐ zation function like cut
np.random.seed(12345)
values = np.random.rand(10)
print(values)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
intermediate = pd.cut(values, bins)
print(intermediate)
result = pd.get_dummies(intermediate)
print(result)
print()


#   String Manipulation
#   splitting a comma-seperated string into pieces
val = 'a,b,  guido'
pieces = [x.strip() for x in val.split(',')]
print(pieces)
print('::'.join(pieces))
print()

#   Using Python's in keyword is the best way to detect a substring, though index and find can also be used
#       the difference between find and index is that index raises an exception if the string isn’t found (versus returning –1)
print('guido' in val)
print(val.index(','))
print(val.find(':'))
#   count returns the number of occurrences of a particular substring
print(val.count(','))
#   replace will substitute occurrences of one pattern for another. It is commonly used to delete patterns, too, by passing an empty string
print(val.replace(',', '::'))
print()

#   string methods (built-in)
#           count           number of non-overlapping occurences of substring in string
#           endswith        True if string ends with suffix
#           startswith      True if string begins with suffix
#           join            Use string as delimiter for concatenating a sequence of other strings
#           index           position of first character of first occurence of substring in string, raises ValueError if not found
#           find            position of first character of first occurence of substring in string, -1 if not found
#           rfind           position of first character of last occurence of substring in string, -1 if not found
#           replace         replace occurences of substring with another string
#           strip           trim whitespace, including newlines
#           rstrip          trim whitespace (including newlines) from RHS of string
#           lstrip          trim whitespace (including newlines) from LHS of string
#           split           break string into list of substrings by given delimiter
#           lower           convert alphabetical characters to lower case
#           upper           convert alphabetical characters to upper case
#           casefold        convert characters to lowercase, including region-specific characters <?>
#           ljust           Left or right justfify (respectively) pad opposite side of string with fill characters 
#           rjust               (default space) to return string with a given minimum widht


#   Regular Expressions
#       The re module functions fall into three categories: pattern matching, substitution, and splitting.

#   To avoid unwanted escaping with \ in a regular expression, use raw string literals like r'C:\x' instead of the equivalent 'C:\\x'.

#   re.search(regex, text, flags=0)
#      Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. 

#   re.split(regex, text, maxsplit=0, flags=0)
#       Split string by the occurrences of pattern (up to maxsplit times). If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list.

#   re.findall(regex, text, flags=0)
#       Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result.

#   re.finditer()
#       Like findall, but return an iterator of match objects

#   re.sub(regex_search, regex_replace, text, count=n, flags=0)
#       Return the string obtained by replacing the leftmost non-overlapping occurrences of regex_search with regex_replace. String is returned unchanged if regex_search is not found. Replace backreferences (ie: \1) with corresponding match group.

#   suppose we wanted to split a string with a variable number of whitespace characters
text = "foo bar\t baz \tqux"
print(re.split('\s+', text))
#   or
#>%     regex = re.compile('\s+')
#>%     print(regex.split(text))

#   get list of patterns matching regex
print(re.findall('\s+', text))
print()

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))
print(regex.sub('REDACTED', text))

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')
print(m.groups())

print(regex.findall(text))

print(list(regex.finditer(text)))
print()


#   Vectorized string functions
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(data)
print(data)
print(data.isnull())
print(data.str.contains('gmail'))
print()

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
print(data.str.findall(pattern, flags=re.IGNORECASE))
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
print(data.str[:5])
print()

#   Pandas vectorized string methods
#           cat                 concatenate strings element wise (with optional delimiter)
#           countains           boolean array, whether each string contains pattern/regex
#           count               count occurences of pattern
#           extract             Use a regular expression with groups to extract one or more strings from a Series of strings; 
#                               the result will be a DataFrame with one column per group
#           endswith            Equivelent to x.endswith(pattern) for each element
#           startswith          Equivelent to x.startswith(pattern) for each element
#           findall             Compute list of all occurences of pattern/regex for each string
#           get                 Index into each element (i-th element)
#           isalnum             Equivelent to str.alnum
#           isalpha             Equivelent to str.isalpha
#           isdecimal           Equivelent to str.isdecimal
#           isdigit             Equivelent to str.isdigit
#           islower             Equivelent to str.islower
#           isnumeric           Equivelent to str.isupper
#           join                Join strings in each element of the series with given seperator
#           len                 Compute lenght of each string
#           lower, upper        Convert case, equivelent to x.lower(), x.upper() for each element
#           match               Use re.match with passed regex on each element, return matched groups as list
#           pad                 Add whitespace to left, right, or both sides of each string
#           center              Equivelent to pad(sides='both')
#           repeat              Duplicate values (str.repeat(3) is equivelent to x * 3 for each string)
#           slice               slice each string in the series
#           split               split strings on delimiter or regex
#           strip               Trip whitespace from both sides
#           rstrip              Trim whitespace on RHS
#           lstrip              Trip whitespace on LHS

#   }}}1
