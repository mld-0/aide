#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import numpy as np
import pandas as pd
#   {{{2
#   See: OReilly Python for Data Analysis Ch 10

#   groupby: split-apply-combine

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'], 'key2' : ['one', 'two', 'one', 'two', 'one'], 'data1' : np.random.randn(5), 'data2' : np.random.randn(5)})
print(df)

grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())
print()

#   grouped the data using two keys, and the resulting Series now has a hierarchical index consisting of the unique pairs of keys observed
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)
print(means.unstack())
print()

#   The grouping keys can be any arrays of the right length
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())
print()

#   Where grouping information is found in the same df as the data - pass column names (whether those are strings, numbers, or other Python objects) as the group keys
print(df.groupby('key1').mean())
print()

print(df.groupby(['key1', 'key2']).mean())
print()

print(df.groupby(['key1', 'key2']).size())
print()

#   any missing values in a group key will be excluded from the result

#   Iterating Over Groups
#       The GroupBy object supports iteration, generating a sequence of 2-tuples containing the group name along with the chunk of data.
for name, group in df.groupby('key1'): 
    print(f"name=({name})")
    print(f"group=({group})")
print()

#   In the case of multiple keys, the first element in the tuple will be a tuple of key values
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(f"k1=({k1}), k2=({k2})")
    print(f"group=({group})")
print()

#   computing a dict of the data pieces as a one-liner
pieces = dict(list(df.groupby('key1')))
print(pieces)
print()

#   By default groupby groups on axis=0, but you can group on any of the other axes
#   Group the columns of df by dtype
grouped = df.groupby(df.dtypes, axis=1)
for dtype, group in grouped:
    print(f"dtype=({dtype})")
    print(f"group=({group})")
print()

#   Selecting a Column or Subset of Columns
#       Indexing a GroupBy object created from a DataFrame with a column name or array of column names has the effect of column subsetting for aggregation.
#   Ongoing: 2021-03-06T15:33:32AEDT effect of double-brackets [[]] <?>
df.groupby('key1')['data1']
df.groupby('key1')[['data1']] 
df.groupby('key1')[['data2']]
#   or
df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])

#   The object returned by this indexing operation is a grouped DataFrame if a list or array is passed or a grouped Series if only a single column name is passed as a scalar

#   To compute means for just the data2 column and get the result as a DataFrame
print(df.groupby(['key1', 'key2'])[['data2']].mean())
print()

#   Grouping with Dicts and Series
people = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = np.nan  # Add a few NA values
print(people)
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f' : 'orange'}
print(mapping)
by_column = people.groupby(mapping, axis=1)
print(by_column.sum())
print()

#   The same functionality holds for Series, which can be viewed as a fixed-size mapping
map_series = pd.Series(mapping)
print(people.groupby(map_series, axis=1).count())
print()

#   Grouping with Functions
#   Using Python functions is a more generic way of defining a group mapping compared with a dict or Series. Any function passed as a group key will be called once per index value, with the return values being used as the group names.

#   grop by the length of names
print(people.groupby(len).sum())
print()

#   Mixing functions with arrays, dicts, or Series is not a problem as everything gets con‐ verted to arrays internally
key_list = ['one', 'one', 'one', 'two', 'two']
print(people.groupby([len, key_list]).min())
print()

#   Grouping by Index Levels
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'], [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
print(hier_df)

#   To group by level, pass the level number or name using the level keyword
print(hier_df.groupby(level='cty', axis=1).count())
#   or
#>%     print(hier_df.groupby('cty', axis=1).count())
print()


#   Data Aggregation
#       Aggregations refer to any data transformation that produces scalar values from arrays.

#   groupby methods
#           count               Number of non-NA values in group
#           sum                 Sum of non-NA values
#           mean                Mean of non-NA values
#           median              Median of non-NA values
#           std, var            standard deviation and variance
#           min, max            minimum and maximum non-NA values
#           prod                product of non-NA values
#           first, last         first and last non-NA values

#   quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear')
#       Return values at the given quantile over requested axis.
grouped = df.groupby('key1')
print(grouped['data1'].quantile(0.9))
print(grouped['data1'].quantile(0.1))
print()

#   agg(func=None, axis=0, *args, **kwargs)
#       Aggregate using one or more operations over the specified axis. To use your own aggregation functions, pass any function that aggregates an array to the aggregate or agg method
def peak_to_peak(arr):
    return arr.max() - arr.min()
print(grouped.agg(peak_to_peak))
print()

#   some functions, ie: describe(), may be used on a group despite not strictly speaking being aggregations
print(grouped.describe())
print()


#   Column-Wise and Multiple Function Application
tips = pd.read_csv('data/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips)
print()

grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.agg('mean'))
#   or
#>%     print(grouped_pct.agg(np.mean))
print()

#   If you pass a list of functions or function names instead, you get back a DataFrame with column names taken from the functions
print(grouped_pct.agg(['mean', 'std', peak_to_peak]))
#   or
#>%     print(grouped_pct.agg([np.mean, np.std, peak_to_peak]))
print()

#   if you pass a list of (name, function) tuples, the first element of each tuple will be used as the DataFrame column names (you can think of a list of 2-tuples as an ordered mapping)
print(grouped_pct.agg([('foo', np.mean), ('bar', np.std)]))
print()

#   suppose we wanted to compute the same three statistics for the tip_pct and total_bill columns
functions = [('count', 'count'), ('mean', np.mean), ('max', np.max)]
result = grouped[['tip_pct', 'total_bill']].agg(functions)
print(result)
print()

#   suppose you wanted to apply potentially different functions to one or more of the columns
print(grouped.agg({'tip' : np.max, 'size' : 'sum'}))
print()

#   A DataFrame will have hierarchical columns only if multiple functions are applied to at least one column
print(grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'], 'size' : 'sum'}))
print()


#   Returning Aggregated Data Without Row Indexes
print(tips.groupby(['day', 'smoker']).mean())
print(tips.groupby(['day', 'smoker'], as_index=False).mean())
print()


#   Apply: General split-apply-combine
#   apply(func, axis=0, raw=False, result_type=None, args=(), *kwargs)
#       Apply a function along an axis of the dataframe. The most general-purpose GroupBy method.

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

print(top(tips, n=6))
print()

#   The top function is called on each row group from the DataFrame, and then the results are glued together using pandas.concat, labeling the pieces with the group names. The result therefore has a hierarchical index whose inner level contains index values from the original DataFrame.
print(tips.groupby('smoker').apply(top))
print()

#   Including arguments to apply() function
print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))
print()

result = tips.groupby('smoker')['tip_pct'].describe()
#   or
#>%     result = tips.groupby('smoker')['tip_pct'].apply(lambda x: x.describe())
print(result)
print()


#   Suppressing the Group Keys
#       disable forming of hierachical index with group_keys=False
print(tips.groupby('smoker', group_keys=False).apply(top))
print()


#   Quantile and Bucket Analysis
frame = pd.DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)
print(quartiles)
print()
#   The Categorical object returned by cut can be passed directly to groupby.
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}
grouped = frame.data2.groupby(quartiles)
print(grouped.apply(get_stats).unstack())
print()

#   to compute equal-size buckets based on sample quantiles, use qcut.
grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
print(result)
result = grouped.apply(get_stats).unstack()
print(result)
print()


#   Filling Missing Values with Group-Specific Values
states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data)
print()
#   fill the NA values using the group means
fill_mean = lambda g: g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean))
print()
#   predefined fill values for each group
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
print(data.groupby(group_key).apply(fill_func))
print()


#   Random Sampling and Permutation
#       Suppose you wanted to draw a random sample (with or without replacement) from a large dataset. There are a number of ways to perform the “draws”; here we use the sample method for Series.
# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4 
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q'] 
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)
print(deck[:13])
print()

#   sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
#       Return a random sample of items from an axis of object

#   drawing a hand of five cards
def draw(deck, n=5):
    return deck.sample(n)
print(draw(deck))
print()

#   two random cards from each suit
get_suit = lambda card: card[-1]  # last letter is suit
result = deck.groupby(get_suit).apply(draw, n=2)
print(result)
print()


#   Group Weighted Average and Correlation
df = pd.DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], 'data': np.random.randn(8), 'weights': np.random.rand(8)})
print(df)
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
result = grouped.apply(get_wavg)
print(result)
print()

close_px = pd.read_csv('data/stock_px_2.csv', parse_dates=True, index_col=0)
print(close_px.info())
print(close_px)
print()

#   compute a DataFrame consisting of the yearly correlations of daily returns (computed from percent changes) with SP500
spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
print(by_year.apply(spx_corr))
print()
#   annual correlation between Apple and Microsoft
print(by_year.apply(lambda g: g['AAPL'].corr(g['MSFT'])))
print()

#   Group-Wise Linear Regression
#       you can use groupby to perform more complex group-wise statistical analysis, as long as the function returns a pandas object or scalar value.
#       using the statsmodels econometrics library

#>%     import statsmodels.api as sm
#>%     def regress(data, yvar, xvars):
#>%         Y = data[yvar]
#>%         X = data[xvars]
#>%         X['intercept'] = 1.0
#>%         result = sm.OLS(Y, X).fit()
#>%         return result.params
#>%     result = by_year.apply(regress, 'AAPL', ['SPX'])
#>%     print(result)
#>%     print()


#   Pivot Tables and Cross-Tabulation
#       A pivot table is a data summarization tool frequently found in spreadsheet programs and other data analysis software. It aggregates a table of data by one or more keys, arranging the data in a rectangle with some of the group keys along the rows and some along the columns.
#       Pivot tables in Python with pandas are made possible through the groupby facility described in this chapter combined with reshape opera‐ tions utilizing hierarchical indexing.

#   pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)
#           or
#   df.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)
#       Create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.
#               values              columns to aggregate
#               index               keys to group by on the pivot table index. If given, must be same length as data
#               columns             Keys to group by on the pivot table column. If given, must be same length as the data
#               aggfunc             Aggregation function or list of functions ('mean' by default); can be any function valid 
#                                   in a groupby context
#               fill_value          value to replace missing values in resulting pivot table
#               margins             add all row/columns (subtotals / grand-totals)
#               dropna              do not include columns whose entries are all NaN
#               margins_name        Name of the row/column that will contain 'margin' totals 
#               observed            If True: only show observed values for categorical groupers. If False: show all values 
#                                   for categorical groupers.

#   Returning to the tipping dataset, suppose you wanted to compute a table of group means (the default pivot_table aggregation type) arranged by day and smoker on the rows
print(tips.pivot_table(index=['day', 'smoker']))
print()

#   suppose we want to aggregate only tip_pct and size, and additionally group by time.
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'))
print()

#   To use a different aggregation function, pass it to aggfunc (and replace NaN with 0)
print(tips.pivot_table('tip_pct', index=['time', 'smoker'], columns='day', aggfunc=len, margins=True, fill_value=0))
print()


#   Cross-Tabulations
#       A cross-tabulation (or crosstab for short) is a special case of a pivot table that com‐ putes group frequencies.

#   The first two arguments to crosstab can each either be an array or Series or a list of arrays
print(pd.crosstab([tips.time, tips.day], tips.smoker, margins=True))

#   Continue: 2021-03-06T17:02:34AEDT nationality / handedness data -> source?

#>%     pd.crosstab(data.Nationality, data.Handedness, margins=True)


#   }}}1
