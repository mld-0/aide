#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import pandas as pd
import numpy as np

#   Hierarchical Indexing
#   Enables you to have multiple (two or more) index levels on an axis. Somewhat abstractly, it provides a way for you to work with higher dimensional data in a lower dimensional form
data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1,2,3,1,3,1,2,2,3]])
print(data)
print()

#   With a hierarchically indexed object, so-called partial indexing is possible, enabling you to concisely select subsets of the data
print(data['b'])
print(data['b':'c'])
print(data[:, 2])
print()

print(data.loc['b'])
print(data.loc[['b', 'c']])
print(data.loc[:, 2])
print()

#   Hierarchical indexing plays an important role in reshaping data and group-based operations like forming a pivot table

#   data.unstack()
#       rearrange data into a DataFrame
print(data.unstack())
print()

#   data.stack()
#       inverse of unstack()
print(data.unstack().stack())
print()

#   With a DataFrame, either axis can have a hierarchical index
frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
#   The hierarchical levels can have names
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print()

#   With partial column indexing you can similarly select groups of columns:
print(frame['Ohio'])
print()

#   Creating a MultiIndex instance
_multi = pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])
print(_multi)
print()


#   Reordering and Sorting Levels

#   swaplevel(,i, j, axis)     
#       Takes two level numbers or names and returns a new object with the levels interchanged, that is, Swap levels i and j in a MultiIndex on a particular axis.
print(frame.swaplevel('key1', 'key2'))
print()

#   sort_index(axis[, level, ascending, inplace, kind, na_position, sort_remaining, ignore_index, key])
#       Sort object by labels (along an axis), only the values in a single level
print(frame.sort_index(level=1))
print()

print(frame.swaplevel(0, 1).sort_index(level=0))
print()


#   Summary Statistics by Level
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))
print()

#   Indexing with a DataFrame's columns
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd':[0,1,2,0,1,2,3]})
print(frame)
print()

#   set_index(keys, [drop=True, append=False, inplace=False, verify_integrity=False])
#       create a new DataFrame using one or more of its columns as the index
print(frame.set_index('d'))
frame2 = frame.set_index(['c', 'd'])
print(frame2)
print()

#   By default the columns are removed from the DataFrame, though you can leave them in
print(frame.set_index(['c', 'd'], drop=False))
print()

#   reset_index()
#       does the opposite of set_index; the hierarchical index levels are moved into the columns
print(frame2.reset_index())
print()


#   Combining and Merging Datasets
#   Data contained in pandas objects can be combined together in a number of ways
#           pandas.merge            connects rows based on one or more keys (like db join)
#           pandas.concat           concatenates or 'stacks' together objects along an axis
#           combine_first           enables splicing together overlapping data to fill missing values

#   Database-Style DataFrame Joins
#       Merge or join operations combine datasets by linking rows using one or more keys.
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print(df2)
print()

#   LINK: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
#   LINK: https://stackoverflow.com/questions/53645882/pandas-merging-101

#   merge(left, right[, how='inner', left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate])
#       Merge DataFrame or named Series objects with a database-style join.
#       merge is a many-to-one join. If column name is not specified, overlapping columns are used as keys. 
#               left            merge df LHS
#               right           merge df RHS
#               how             inner, outer, left, right (default=inner)
#               on              column names to join on, must be found in both tables, if not given use columns in both df
#               left_on         columns in left df to join on
#               right_on        columns in right df to join on
#               left_index      use index in left as join key (or keys if a multiindex)
#               right_index     use index in right as join key (or keys if a multiindex)
#               sort            sort merged data by join keys (default=True)
#               suffixes        tuple of string values to append to column names in case of overlap (default _x, _y)
#               copy            If False, avoid copying data into resulting structure, (default=True)
#               indicator       Add special column _merge that indicates source of each row,
#                               either 'left_only', 'right_only', or 'both'
print(pd.merge(df1, df2))
#   or
#>%     print(pd.merge(df1, df2, on='key'))
print()

#   By default merge does an 'inner' join; the keys in the result are the intersection, or the common set found in both tables
#   Different types of joins
#           inner           Use only the key combinations observed in both tables
#           outer           Use keys observed in either table
#           left            Use all key combinations found in the left table
#           right           Use all key combinations found in the right table
print(pd.merge(df1, df2, how='outer'))
print()

#   If the column names are different in each object, you can specify them separately
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
print()

#   Continue: 2021-03-04T23:51:02AEDT merge examples

#   Merging on index

#   Concatenating Along an Axis

#   Combining Data with Overlap

#   Reshaping and Pivoting
